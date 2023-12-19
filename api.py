from requests import request
import json


def login(url: str):
    payload = json.dumps({
        'id': 0,
        'jsonrpc': '2.0',
        'method': 'Api.Login',
        'params': {
            'user': '5AHIT',
            'password': '5ahiT',
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = request('POST', url, headers=headers, data=payload, verify=False)
    return response.json()['result']['token']

def write(url: str, token: str, var: str, val: any):
    payload = json.dumps([
        {
            "id": 1,
            "jsonrpc": "2.0",
            "method": "PlcProgram.Write",
            "params": {
                "var": f"\"Motor\".{var}",
                "value": val
            }
        }
    ])
    headers = {
        'Content-Type': 'application/json',
        'Content-Length': str(len(payload)),
        'Host': url,
        'User-Agent': 'PostmanRuntime/7.33.0',
        'X-Auth-Token': token
    }

    response = request('POST', url, headers=headers, data=payload, verify=False)
    response_json = response.json()
    print(response_json)

    if response_json[0]["result"] is not None:
        return True
    else:
        return False
