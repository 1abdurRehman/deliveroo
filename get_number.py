import requests

APIKEY = "VwTjgdT3upC4XfImMcdCzLerkzHotW"
SERVICE = "opt53"

url = f"https://smspva.com/priemnik.php?metod=get_number&country=UK&service={SERVICE}&apikey={APIKEY}"
def get_number():
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        data = response.json()
        print(data)
        return data['number'], data['id']


def get_sms(id):
    sms_url = f"https://smspva.com/priemnik.php?metod=get_sms&country=uk&service={SERVICE}&id={id}&apikey={APIKEY}"
    response = requests.get(sms_url)
    print(response)
    if response.status_code == 200:
        data = response.json()
        print(data)
        return data['sms']


# num, id = get_number()
# get_sms(118028660)