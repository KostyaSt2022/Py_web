from zeep import Settings, Client
import yaml

with open('config.yaml', 'r') as f:
    data = yaml.safe_load(f)

# bad_word = 'Масква'
# addr = 'http://speller.yandex.net/services/spellservice?WSDL'

settings = Settings(strict=False)
client = Client(wsdl=data['addr'], settings=settings)


def checktext(bad_word):
    return client.service.checkText(bad_word)[0]['s']