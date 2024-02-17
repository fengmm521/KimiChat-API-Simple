def new_token():
    
    from requests import get

    with open('refresh_token.txt', 'r', encoding='utf-8') as file:
        r_token = file.read()

    url = "https://kimi.moonshot.cn/api/auth/token/refresh"
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "authorization": "Bearer " + r_token,
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin"
    }

    r = get(url, headers=headers, allow_redirects=True)
    with open('refresh_token.txt', 'w', encoding='utf-8') as file:
        file.write(r.json()['refresh_token'])
    return [r.json()['access_token'],r.json()['refresh_token']]