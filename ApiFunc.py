import requests
import json
import random
import KimiToken as kt


def chat(text):

    url = "https://kimi.moonshot.cn/api/chat"
    cookies = 'Bearer ' + kt.new_token()[0]
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "authorization": cookies,
        "content-type": "application/json",
        "r-timezone": "Asia/Shanghai",
        "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin"
    }
    data = {
        "name": "KimiChat API",
        "is_example": False
    }

    r = requests.post(url, headers=headers, json=data)

    if r.status_code == 200:
        chatid = r.json()['id']

        data2 = {
            "messages": [
                {
                    "role": "user",
                    "content": text
                }
            ],
            "refs": [],
            "use_search": True
        }
        url2 = 'https://kimi.moonshot.cn/api/chat/' + str(chatid) + '/completion/stream'
        r2 = requests.post(url=url2,json=data2,headers=headers)
        if r2.status_code == 200:

            url3 = 'https://kimi.moonshot.cn/api/chat/' + str(chatid) + '/segment/scroll'
            headers3 = {
                "accept": "*/*",
                "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "authorization": cookies,
                "content-type": "application/json",
                "r-timezone": "Asia/Shanghai",
                "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "referrer": "https://kimi.moonshot.cn/chat/cn85ml83qff4rjdhi2r0?data_source=tracer&track_id=pbaes.Pi_gb2BTHE2MNxEl7YxYIbDQyqJz5l-ly9iBqnFyBZ8aCfIjAMbPj-PIFU6A7lS3Fw4NLkI3U52eof9gDi6kIU_MjTd5FNDPNyvcdQECQIUHVHAyKTVfJe37Nzy16BXqyYTtR0RqE4SM9lF2OJOR-IxDS4fhD82jsGYCaHc81hCRfURp_sm1E81E5IztMgbd&utm_campaign=TR_ikmtSa64&utm_content=&utm_medium=B%E7%AB%A0%E7%AB%99PC%E7%AB%AF%E5%B9%BF%E5%91%8A&utm_source=bilibili&utm_term=",
                "referrerPolicy": "strict-origin-when-cross-origin"
            }
            data3 = {
                "last": 50
            }

            r3 = requests.post(url3, headers=headers3, json=data3)
            
            if r3.status_code == 200:
                result = r3.json()
                content = result['items'][-1]['content']

                url4 = "https://kimi.moonshot.cn/api/chat/" + str(chatid)
                headers4 = {
                    "accept": "*/*",
                    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                    "authorization": cookies,
                    "content-type": "application/json",
                    "r-timezone": "Asia/Shanghai",
                    "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "\"Windows\"",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin"
                }

                r4 = requests.delete(url4, headers=headers4)
                if r4.status_code == 200:
                    return content
                else:
                    exit('ERROR_Number:4')
                    return None
            else:
                exit('ERROR_Number:3')
                return None
        else:
            exit('ERROR_Number:2')
            return None
    else:
        exit('ERROR_Number:1')
        return None