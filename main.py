import requests
import json
import sys
import requests
import threading

acc = [["username1", "password1"], 
["username2", "password2"], 
]


def getColorID(colorName):
    if (colorName == "dark red"): 
        return 1
    elif (colorName == "red"):
        return 2
    elif (colorName == "orange"):
        return 3
    elif (colorName == "yellow"):
        return 4
    elif (colorName == "dark green"):
        return 6
    elif (colorName == "green"):
        return 7
    elif (colorName == "light green"):
        return 8
    elif (colorName == "dark teal"):
        return 9
    elif (colorName == "teal"):
        return 10
    elif (colorName == "dark blue"):
        return 12
    elif (colorName == "blue"):
        return 13
    elif (colorName == "light blue"):
        return 14
    elif (colorName == "indigo"):
        return 15
    elif (colorName == "perwinkle"):
        return 16
    elif (colorName == "dark purple"):
        return 18
    elif (colorName == "purple"):
        return 19
    elif (colorName == "pink"):
        return 22
    elif (colorName == "light pink"):
        return 23
    elif (colorName == "dark brown"):
        return 24
    elif (colorName == "brown"):
        return 25
    elif (colorName == "black"):
        return 27
    elif (colorName == "gray"):
        return 29
    elif (colorName == "light gray"):
        return 30
    elif (colorName == "white"):
        return 31
    else:
        return 1

def placePixel(user, password, x, y, colorI):
    if x < 1000 and y < 1000:
        canI = 0
    elif x >= 1000 and y < 1000:
        canI = 1
        x = x % 1000
    elif x < 1000 and y >= 1000:
        canI = 2
        y = y % 1000
    elif x >= 1000 and y >= 1000:
        canI = 3
        x = x % 1000
        y = y % 1000

    URL = 'https://www.reddit.com/login'
    client = requests.session()

    r = client.get(URL)

    rcontent = str(r.content)
    rcontent = rcontent.split('<input type="hidden" name="csrf_token" value="')[1].split('">')[0]


    burp0_url = "https://www.reddit.com:443/login"
    burp0_cookies = {"csv": client.cookies["csv"], "edgebucket": client.cookies["edgebucket"], "session": client.cookies["session"], "G_ENABLED_IDPS": "google"}
    burp0_headers = {"Sec-Ch-Ua": "\"(Not(A:Brand\";v=\"8\", \"Chromium\";v=\"99\"", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Linux\"", "Content-Type": "application/x-www-form-urlencoded", "Accept": "*/*", "Origin": "https://www.reddit.com", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://www.reddit.com/login/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}
    burp0_data = {"csrf_token": rcontent, "otp": '', "password": password, "dest": "https://www.reddit.com", "username": user}
    r = client.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)



    burp0_url = "https://www.reddit.com:443/"
    burp0_cookies = {"csv": client.cookies["csv"], "edgebucket": client.cookies["edgebucket"], "G_ENABLED_IDPS": "google", "reddit_session": client.cookies["reddit_session"], "loid": client.cookies["loid"], "session": client.cookies["session"], "show_announcements": "yes"}
    burp0_headers = {"Cache-Control": "max-age=0", "Sec-Ch-Ua": "\"(Not(A:Brand\";v=\"8\", \"Chromium\";v=\"99\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Linux\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}
    r = requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)

    print(r.status_code)

    token = str(r.content).split('"session":{"accessToken":"')[1].split('",')[0]

    #usern = str(r2.content).split('nTatQ5gjKGK5OWROgaG">')[1].split('</span>')[0]

    auth = "Bearer " + token

    burp0_url = "https://gql-realtime-2.reddit.com:443/query"
    burp0_headers = {"Sec-Ch-Ua": "\"(Not(A:Brand\";v=\"8\", \"Chromium\";v=\"99\"", "Apollographql-Client-Name": "mona-lisa", "Sec-Ch-Ua-Mobile": "?0", "Authorization": auth, "Content-Type": "application/json", "Accept": "*/*", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36", "Apollographql-Client-Version": "0.0.1", "Sec-Ch-Ua-Platform": "\"Linux\"", "Origin": "https://hot-potato.reddit.com", "Sec-Fetch-Site": "same-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://hot-potato.reddit.com/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}
    burp0_json={"operationName": "setPixel", "query": "mutation setPixel($input: ActInput!) {\n  act(input: $input) {\n    data {\n      ... on BasicMessage {\n        id\n        data {\n          ... on GetUserCooldownResponseMessageData {\n            nextAvailablePixelTimestamp\n            __typename\n          }\n          ... on SetPixelResponseMessageData {\n            timestamp\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n", "variables": {"input": {"actionName": "r/replace:set_pixel", "PixelMessageData": {"canvasIndex": canI, "colorIndex": colorI, "coordinate": {"x": x, "y": y}}}}}
    response = requests.post(burp0_url, headers=burp0_headers, json=burp0_json)
    
    print("Status Code", response.status_code)
    print("JSON Response ", response.json())

#placePixel(acc[0][0], acc[0][1], 359, 894, getColorID("red"), 0)
#placePixel(acc[1][0], acc[1][1], 359, 895, getColorID("red"), 0)


#                                              username    password   x    y        color id
x1 = threading.Thread(target=placePixel, args=(acc[0][0], acc[0][1], 1980, 1617, getColorID("orange")))
x2 = threading.Thread(target=placePixel, args=(acc[1][0], acc[1][1], 1980, 1618, getColorID("orange")))

x1.start()
x2.start()