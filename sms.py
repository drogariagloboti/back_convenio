import requests
import json

token_zenvia = 'OKXQTBWqQhQS0UZagtezJAn_RBkGp5Co0Z0b'

def sms():
    url = 'https://api.zenvia.com/v2/channels/sms/messages'

    data = {
                "from": "5510999999999",
                "to": "5586998221100",
                "contents": [
                {
                    "type": "text",
                    "text": "508970 é seu código de acesso para o convênio Médico Globo"
                }
                ]
            }

    headers = {                                                              
    "Content-Type": "application/json", # dados do headers
    "X-API-Token": f"{token_zenvia}"
    }

    response = requests.post(url, headers=headers, json=data)

    print(response)

sms()