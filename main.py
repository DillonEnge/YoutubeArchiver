from archiver import Archiver

a = Archiver()
a.scrape_page()
print('Successfully archived Youtube trending page for ' + a.date_tag)