import requests
# from twilio.rest import Client
#
# account_sid = 'AC34549d42535761bfe38ab93df0bb19ef'
# auth_token = 'dd4e131d0c29b0ac28abd14f27de4d05'
# client = Client(account_sid, auth_token)
#
# message = client.messages.create(
#     from_='+14126936366',
#     body='Dzień dobry',
#     to='+48793825614'
# )
#
# print(message.sid)

from requests.exceptions import HTTPError

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)
        response.raise_for_status()

    except HTTPError as http_err:
        print(f'Http error occured: {http_err}')
    else:
        print('Success')

