# Youtube Archiver
## Usage
<b>terminal</b>
```shell
pip3 install -r requirements.txt

touch main.py
```
<b>main.py</b>
```python
from archiver import Archiver

archiver = Archiver()
archiver.scrape_page()
```
<b>crontab</b>
```bash
0 12 * * * cd <working_dir> && python3 main.js >> log.txt
```
## Goal
* Create a daily recurring archive generator of the youtube trending page including all the necessary data for reconstruction.

## Planning
### Data currently present in each date entry
* title
* views
* duration
* description
* user
* video link

### Data to be included in each date entry
* time posted

### JSON structure
```json
{
    "date": {
        "videos": [
            {
                "title": "example-title",
                "views": "example-views",
                "time_posted": "example-time-posted",
                "duration": "example-duration",
                "description": "example-description",
                "user": "example-user",
                "link": "example-link"
            },
            {
                "title": "example-title",
                "views": "example-views",
                "time_posted": "example-time-posted",
                "duration": "example-duration",
                "description": "example-description",
                "user": "example-user",
                "link": "example-link"
            }
        ]
    }
}
```

### Misc
* Request URL: https://www.youtube.com/feed/trending
* Generates soup.html file upon run to get true returned html structure for future modifications

### Future additions
* crontab instructions for daily recurring use on a hosted server