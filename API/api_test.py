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

url = 'https://api.twilio.com/2010-04-01/Accounts/AC34549d42535761bfe38ab93df0bb19ef/Messages.json'
client_id = 'AC34549d42535761bfe38ab93df0bb19ef'
client_secret = 'dd4e131d0c29b0ac28abd14f27de4d05'

data = {
    'From': '+14126936366',
    'Body': 'Dzień dobry',
    'To': '+48793825614'
}
response = requests.post(url, data=data, auth=(client_id, client_secret))

response = requests.get(url, auth=(client_id, client_secret))

print(response.json())
