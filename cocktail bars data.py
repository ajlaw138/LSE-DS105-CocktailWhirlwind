import requests
import json
import pandas as pd

page_num = 1
total_page = 332
data = []
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Authorization": "Bearer xAUKTBfFAN_7YyGyaIl0GlmiQFq-O_YJXWr2rgfYwao",
    "Content-Type": "application/json",
    "Cookie": "_TO_Canary=False; _gcl_au=1.1.1252295219.1686144347; _hjFirstSeen=1; _hjIncludedInSessionSample_380860=0; _hjSession_380860=eyJpZCI6ImExMzI3NzhlLTkyNjEtNDk5OS05YjM5LTU2ODI1ZmQzYjFkYyIsImNyZWF0ZWQiOjE2ODYxNDQzNDY4MDAsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _gid=GA1.2.125100605.1686144347; _hjSessionUser_380860=eyJpZCI6ImM0MDFkYTE3LTIzMzgtNWI4ZC05ZjZjLWMzYTIwYjg3MTM2YSIsImNyZWF0ZWQiOjE2ODYxNDQzNDY3OTIsImV4aXN0aW5nIjp0cnVlfQ==; __qca=P0-2040626597-1686144361258; DM_SitId1123=1; DM_SitId1123SecId6113=1; trc_cookie_storage=taboola%2520global%253Auser-id%3Db974dae1-f010-4bc6-b4f6-a93a08622c10-tuctb7a0aec; _parsely_session={%22sid%22:1%2C%22surl%22:%22https://www.timeout.com/london/search#/?sort=relevance&q=cocktail%2520bars&viewstate=list&page_number=2%22%2C%22sref%22:%22%22%2C%22sts%22:1686144378245%2C%22slts%22:0}; _parsely_visitor={%22id%22:%22pid=05c69d00-d4d1-4815-863e-f33fcffe3dd1%22%2C%22session_count%22:1%2C%22last_session_ts%22:1686144378245}; permutive-id=213e5d78-efc8-429e-b0e2-f68922343ff1; _TO_Newsletter_PageViewCount=9; _fbp=fb.1.1686146135940.474577174; _gahitid=21:55:59; _gat_UA-90612241-1=1; _ga=GA1.2.991766655.1686144347; _ga_D0CLQSGKB3=GS1.1.1686144347.1.1.1686146335.0.0.0",
    "Referer": "https://www.timeout.com/london/search"
}

while True:
    url = f'https://www.timeout.com/graffiti/v1/sites/uk-london/search?page_size=10&page_number={page_num}&facets=false&view=complete&exclude_closed=true&locale=en-GB&sort=relevance&q=cocktail+bars'

    response = requests.get(url, headers=headers)
    try:
        response_dict = json.loads(response.text)

        body_lst = response_dict['body']
    except:
        body_lst = []

    for body in body_lst:
        try:
            name = body['name']
            location = body['location']
            data.append({'Name': name, 'Location': location})
        except:
            print(page_num)

    page_num += 1

    if page_num > total_page:
        break

df = pd.DataFrame(data)
df.to_excel('cocktail_bars.xlsx', index=False)
