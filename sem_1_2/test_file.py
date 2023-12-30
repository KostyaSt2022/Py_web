import requests
import yaml

with open('config.yaml', 'r') as f:
    data = yaml.safe_load(f)


def test_step1(take_token):
    header = {'X-Auth-Token': take_token(data['username'], data['password'])}
    out = requests.get(data['url2'], headers=header, params={'owner': 'notMe'}).json()['data']
    res = [i['title'] for i in out]