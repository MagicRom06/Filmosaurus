import csv
import os


class Movie:

    def __init__(
        self,
        imdb_id,
        title,
        year,
        plot,
        category,
        director,
        cast,
        country
    ):
        self._imdb_id = imdb_id
        self._title = title
        self._year = year
        self._plot = plot
        self._category = category
        self._director = director
        self._cast = cast
        self._country = country

    @staticmethod
    def load():
        path = os.path.dirname(os.path.abspath(__file__))
        file = open(path + '/imdb_movies.csv')
        return csv.reader(file)

    @staticmethod
    def parse(csv_file):
        list_objects = list()
        for row in csv_file:
            imdb_id = row[0]
            title = row[1]
            year = row[3]
            plot = row[13]
            category = row[5]
            director = row[9]
            cast = row[12]
            country = row[7]
            list_objects.append(Movie.get(
                imdb_id,
                title,
                year,
                plot,
                category,
                director,
                cast,
                country
            ))
        return list_objects

    @staticmethod
    def get(imdb_id,
            title,
            year,
            plot,
            category,
            director,
            cast,
            country):
        return Movie(
            imdb_id,
            title,
            year,
            plot,
            category,
            director,
            cast,
            country
        )

    def _get_imdb_id(self):
        return self._imdb_id

    def _get_title(self):
        return self._title

    def _get_year(self):
        return self._year

    def _get_plot(self):
        return self._plot

    def _get_category(self):
        return self._category

    def _get_director(self):
        return self._director

    def _get_cast(self):
        return self._cast

    def _get_country(self):
        return self._country

    imdb_id = property(_get_imdb_id)
    title = property(_get_title)
    year = property(_get_year)
    plot = property(_get_plot)
    category = property(_get_category)
    director = property(_get_director)
    cast = property(_get_cast)
    country = property(_get_country)
