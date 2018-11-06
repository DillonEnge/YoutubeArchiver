import json, requests, os
from bs4 import BeautifulSoup, element
from datetime import datetime

class Archiver:
    def __init__(self):
        self.date_tag = datetime.today().strftime('%Y-%m-%d')
        self.endpoint = 'https://youtube.com'
        self.request_endpoint = 'https://www.youtube.com/feed/trending'
        if not os.path.isfile('archive.json'):
            with open('archive.json', 'w') as outfile:
                json.dump(
                    {
                        self.date_tag: {
                            'videos': []
                        }
                    }, outfile, indent=4)
    
    def scrape_page(self):
        video_object = {}
        page = requests.get(self.request_endpoint)
        soup = BeautifulSoup(page.text, 'html.parser')

        with open('soup.html', 'w') as outfile:
            outfile.write(soup.prettify())

        videos = soup.find_all(class_='yt-lockup-dismissable')

        for video in videos:
            video_object['user'] = self.endpoint + video.find(class_='yt-lockup-byline').contents[0]['href']
            description = video.find(class_='yt-lockup-description')

            if type(description.contents[0]) == element.NavigableString:
                video_object['description'] = description.contents[0]
            else:
                video_object['description'] = 'None'

            video_object['view_count'] = video.find(class_='yt-lockup-meta-info').contents[1].contents[0].split(' views')[0]

            header = video.find(class_='yt-lockup-title')

            video_object['duration'] = header.contents[1].contents[0][13:].replace('.', '')
            video_object['title'] = header.contents[0]['title']
            video_object['link'] = self.endpoint + header.contents[0]['href']
            self.append_video(video_object)

    def append_video(self, video):
        archive = self.get_archive()
        archive[self.date_tag]['videos'].append(video)
        self.write_archive(archive)

    def get_archive(self):
        formatted_archive = {}
        with open('archive.json') as archive:
            formatted_archive = json.load(archive)
        return formatted_archive

    def write_archive(self, archive):
        with open('archive.json', 'w') as outfile:
            json.dump(archive, outfile, indent=4)