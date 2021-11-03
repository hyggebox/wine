from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime as dt
import pandas
import openpyxl

def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )

    template = env.get_template('template.html')


    current_year = dt.datetime.now().year
    current_age = current_year - 1920
    last_digit = str(current_age)[-1]

    if last_digit == "1":
        word_years = "год"
    elif last_digit == "2" or last_digit == "3" or last_digit == "4":
        word_years = "года"
    else:
        word_years = "лет"


    wines_df = pandas.read_excel('wine3.xlsx', keep_default_na=False)
    categories = set(wines_df['Категория'].to_list())

    data_beverages = {}
    for category in categories:
        data_beverages[category] = wines_df.loc[wines_df['Категория'] == category].to_dict('records')


    rendered_page = template.render(
        current_age=current_age,
        word_years=word_years,
        all_wines=data_beverages
    )

    with open('index.html', 'w', encoding='utf8') as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == "__main__":
    main()