import csv
import os


class Movie:

    def __init__(
        self,
        title,
        year,
        plot,
        category,
        director,
        cast,
        country
    ):
        self.title = title
        self.year = year
        self.plot = plot
        self.category = category
        self.director = director
        self.cast = cast
        self.country = country

    @staticmethod
    def load():
        rows = list()
        path = os.path.dirname(os.path.abspath(__file__))
        file = open(path + '/imdb_movies.csv')
        csvreader = csv.reader(file)
        for row in csvreader:
            rows.append(row)
        return rows

    @staticmethod
    def parse(csv_file):
        for row in csv_file:
            print(row)

    @staticmethod
    def get():
        pass
