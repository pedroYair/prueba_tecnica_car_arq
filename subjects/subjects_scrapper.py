import requests
from bs4 import BeautifulSoup
import pandas as pd
from subjects.models import Subject


class Scrapper(object):
    def __init__(self):
        self.url = 'https://www.ucm.es/estudios/grado-educacionprimaria-estudios-estructura'
        self.html = None
        self.data = []
        self.subjects_amount_success = 0
        self.subjects_amount_error = 0

    def get_html(self):
        if not self.html:
            response = requests.get(self.url)
            self.html = response.text
        return self.html

    def parser_html(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        tables = soup.find_all("table")
        for item in tables:
            df = pd.read_html(str(item))[0]
            self.data.append(self.clean_data(df))

    def clean_data(self, df):
        df.columns = df.iloc[1]
        df_cleaned = df[2:]
        return df_cleaned

    def save_data(self):
        for df in self.data:
            if {'CÓDIGO', 'ASIGNATURA'}.issubset(df.columns):
                for index, row in df.iterrows():
                    try:
                        Subject.objects.update_or_create(code=row["CÓDIGO"], name=row["ASIGNATURA"])
                        self.subjects_amount_success += 1
                    except Exception as e:
                        self.subjects_amount_error += 1

    def run(self):
        self.get_html()
        self.parser_html()
        self.save_data()
