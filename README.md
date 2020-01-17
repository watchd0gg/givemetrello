# givemetrello developed by watchdogg
# you can see the guide around this tool at my blog medium.com/@watchdogg

Dependency required:
```python -m pip install google ```

```HELP:
usage: givemetrello.py [-h] -l  -s  [-C] [-T]

Trello Credentials Scraper

  -h, --help            show this help message and exit
  -l , --limit          Limit the number of search
  -s , --sleep_time     Sleep time between requests
  -C , --company        OPTIONAL: Search for a specific company board
  -T , --typeof_credential 
                        OPTIONAL: Search for a specific credential, it might
                        be FTP, SSH or GMAIL accounts (DEFAULT IS FOR GMAIL)
                        ej: -T SSH or -T FTP
```
