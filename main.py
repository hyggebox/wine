import argparse
import datetime as dt

import pandas

from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


def main():
    parser = argparse.ArgumentParser(
        description='Запуск сайта по продаже вина. Подключает файл с данными для сайта.'
    )
    parser.add_argument('--data_path',
                        help='Путь к файлу с данными wines.xlsx',
                        default='wines.xlsx')
    args = parser.parse_args()

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )

    template = env.get_template('template.html')

    current_year = dt.datetime.now().year
    founding_year = 1920
    current_age = current_year - founding_year
    last_digit = str(current_age)[-1]

    if last_digit == "1":
        years_word = "год"
    elif last_digit == "2" or last_digit == "3" or last_digit == "4":
        years_word = "года"
    else:
        years_word = "лет"

    wines_df = pandas.read_excel(args.data_path, keep_default_na=False)
    categories = sorted(set(wines_df['Категория'].to_list()))

    all_beverages = {}
    for category in categories:
        all_beverages[category] = wines_df.loc[wines_df['Категория'] == category].to_dict('records')


    rendered_page = template.render(
        current_age=current_age,
        years_word=years_word,
        all_wines=all_beverages
    )

    with open('index.html', 'w', encoding='utf8') as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()