# uruchamiać program z Pycharma z parametrami (Edit Configurations)
# albo z konsoli pythona w pycharm z parametrem np. curr USD

import json, requests, sys
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("help", help="jako parametr programu podaj prawidłowy kod waluty np. EUR")
parser.parse_args()


if len(sys.argv) < 1:
    print('Użycie programu: curr 3-literowy kod waluty')
    sys.exit()

currency = ' '.join(sys.argv[1:])
try:
    url = 'http://api.nbp.pl/api/exchangerates/rates/a/%s/?format=jason' % currency
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(requests.exceptions)
    print('Jako parametr podaj prawidłowy kod waluty np. EUR')
    input(f'\nNaciśnij dowolny klawisz')
    sys.exit()

curr_data = json.loads(response.text)
w = curr_data
rates_str = str(w["rates"]).split(',')
rates_date = str(rates_str[1]).split(':')
rates_rate = str(rates_str[2]).split(':')
rates_float = re.findall(r"[-+]?\d*\.\d+|\d+",rates_rate[1])

print(f'Waluta: {w["currency"]}\nKod: {w["code"]}\n'
      f'Data publikacji: {rates_date[1]}\n'
      f'Śr.kurs NBP: {rates_float} zł.')
input(f'\nNaciśnij dowolny klawisz')
sys.exit()

