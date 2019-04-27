"""
图灵机器人模块
"""

import hashlib
import json
from typing import List

import requests

API_KEY = ''


def get_reply(msg: str, unique_id: str = '') -> List[str]:
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    payload = {
        'reqType': 0,
        'perception': {},
        'userInfo': {
            'apiKey': API_KEY,
            'userId': hashlib.md5(unique_id.encode()).hexdigest()
        }
    }

    if msg:
        payload['perception']['inputText'] = {'text': msg}
        payload['reqType'] = 0
    else:
        return []

    try:
        resp = requests.post(url, json=payload)
        if resp.ok:
            resp_payload = resp.json()
            if resp_payload.get('results'):
                return_list = []
                for result in resp_payload['results']:
                    res_type = result.get('resultType')
                    if res_type in ('text', 'url'):
                        return_list.append(result['values'][res_type])
                return return_list
        return []
    except (requests.RequestException, json.JSONDecodeError, KeyError):
        return []
