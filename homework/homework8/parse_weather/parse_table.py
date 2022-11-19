import requests
import pickle
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


def request_page(month: int) -> dict:
    ua = UserAgent()
    url_address = f'https://www.gismeteo.ru/diary/4368/2021/{month}/'
    res = requests.get(url_address, headers={'User-Agent': ua.firefox})
    print(res.status_code)

    month_temperatures = {}

    if res.status_code == 200:

        soup = BeautifulSoup(res.text, 'lxml')
        table_body = soup.find("tbody")
        rows = table_body.find_all('tr')

        for row in rows:
            date = row.find('td', attrs={'class': 'first'}).text.strip()
            temperatures = [int(el.text.strip()) for el in
                            row.find_all('td', attrs={'class': 'first_in_group positive'})]
            month_temperatures[f'{date} {month} 2021'] = sum(temperatures) / len(temperatures)

    return month_temperatures


def create_weather_dict() -> dict:
    temperatures_of_year = dict()
    for month in range(5, 10):
        temperatures_of_year.update(request_page(month))

    with open('temperatures.bin', 'wb') as ouf:
        pickle.dump(temperatures_of_year, ouf)

    return temperatures_of_year


def open_weather_dict() -> dict:
    with open('temperatures.bin', 'rb') as inf:
        data = pickle.load(inf)
    return data


def find_max_min_average_temperatures(days: dict):
    dates, temperatures = [], []
    for date, temperature in days.items():
        dates.append(date)
        temperatures.append(temperature)

    max_temp = sum(temperatures[:7])
    max_start = 0

    min_temp = sum(temperatures[:7])
    min_start = 0

    for i, temperature in enumerate(temperatures[1:-7]):
        if (q := sum(temperatures[i:i + 7])) > max_temp:
            max_temp = q
            max_start = i

        elif (q := sum(temperatures[i:i + 7])) < min_temp:
            min_temp = q
            min_start = i

    print('Max temperatures in days: ')
    print(dates[max_start], dates[max_start + 7])
    print('Min temperatures in days: ')
    print(dates[min_start], dates[min_start + 7])


def main():
    days = open_weather_dict()
    find_max_min_average_temperatures(days)


if __name__ == '__main__':
    main()
