# uruchamiać program z Pycharma z parametrami (Edit Configurations)
# użycie wth nazwastacji lub wth all (pokazę wszystkie stacje z imgw)

import json, requests, sys
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("help", help="jako parametr programu podaj nazwę stacji, np. jeleniagora "
                                 "(małe litery, bez polskich znaków, pomin spację w nazwie stacji) lub napisz wth all "
                                 "aby wyświtlić wszystkie stacje")
parser.parse_args()


if len(sys.argv) < 1:
    print('Użycie programu: wth nazwa_stacji')
    sys.exit()

station = ' '.join(sys.argv[1:])
if station == 'all':
    url_all_stations = 'https://danepubliczne.imgw.pl/api/data/synop'
    response_all_stations = requests.get(url_all_stations)
    response_all_stations.raise_for_status()
    curr_data_all_stations = json.loads(response_all_stations.text)

    was = curr_data_all_stations
    print('Lista stacji:')
    station_list = []
    for i in range(len(was)):
        station_list.append(was[i]['stacja'])
    print(station_list)
    input(f'\nNaciśnij dowolny klawisz')
    sys.exit()
else:
    try:
        url = 'https://danepubliczne.imgw.pl/api/data/synop/station/%s/' % station
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(requests.exceptions)
        print('Jako parametr podaj nazwę stacji, np. jeleniagora (małe litery, bez polskich znaków, pomin spację '
              'w nazwie stacji) lub napisz wth all aby wyświtlić wszystkie stacje ')
        input(f'\nNaciśnij dowolny klawisz')
        sys.exit()

    curr_data = json.loads(response.text)
    w = curr_data
    station_id = str(w["id_stacji"]).split(',')
    station_name = str(w["stacja"]).split(',')
    measurement_date = str(w["data_pomiaru"]).split(',')
    measurement_time = str(w["godzina_pomiaru"]).split(',')
    temp = str(w["temperatura"]).split(',')
    wind_vel = str(w["predkosc_wiatru"]).split(',')
    wind_dir = str(w["kierunek_wiatru"]).split(',')
    humidity = str(w["wilgotnosc_wzgledna"]).split(',')
    precipitation = str(w["suma_opadu"]).split(',')
    pressure = str(w["cisnienie"]).split(',')


    print(f'IMGW dane synoptyczne\n'
    f'id_stacji: {station_id}\nNazwa stacji: {station_name}\n'
          f'Data pomiaru: {measurement_date}\n'
          f'Godzina pomiaru: {measurement_time}\n'
          f'Temperatura: {temp} st\n'
          f'Prędkość wiatru: {wind_vel} km/h\n'
          f'Kierunek wiatru: {wind_dir}\n'
          f'Wilgotność względna: {humidity} %\n'
          f'Suma opadu: {precipitation} mm\n'
          f'Ciśnienie: {pressure} hPa\n')

    input(f'\nNaciśnij dowolny klawisz')
    sys.exit()

