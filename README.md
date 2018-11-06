# Youtube Archiver
## Goal
* Create a daily recurring archive generator of the youtube trending page including all the necessary data for reconstruction.

## Planning
### Data to be included in each date entry
* ~~title~~
* time posted
* ~~views~~
* ~~duration~~
* ~~description~~
* ~~user~~
* ~~video link~~

### JSON structure
```json
{
    "date": {
        "videos": [
            {
                "title": "example-title",
                "time_posted": "example-time-posted",
                "views": "example-views",
                "user": "example-user",
                "link": "example-link"
            },
            {
                "title": "example-title",
                "time_posted": "example-time-posted",
                "views": "example-views",
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