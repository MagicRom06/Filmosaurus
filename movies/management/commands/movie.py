import csv
from movies.models import Movie
import os
import imdb


class MovieToDB:

    def __init__(
        self,
        imdb_id,
        title,
        year,
        plot,
        category,
        director,
        cast,
        country,
        picture
    ):
        self._imdb_id = imdb_id
        self._title = title
        self._year = year
        self._plot = plot
        self._category = category
        self._director = director
        self._cast = cast
        self._country = country
        self._picture = picture

    @staticmethod
    def load():
        path = os.path.dirname(os.path.abspath(__file__))
        file = open(path + '/imdb_movies.csv')
        reader = csv.reader(file)
        next(reader)
        return reader

    @staticmethod
    def parse(csv_file):
        list_objects = list()
        for row in csv_file:
            imdb_id = row[0].replace('tt', '')
            list_objects.append(MovieToDB.get(
                imdb_id,
                row[1],
                row[3],
                row[13],
                row[5],
                row[9],
                row[12],
                row[7],
                # Movie.get_picture(imdb_id)
                None
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
            country,
            picture):
        return MovieToDB(
            imdb_id,
            title,
            year,
            plot,
            category,
            director,
            cast,
            country,
            picture
        )

    @staticmethod
    def get_picture(movie_id):
        ia = imdb.IMDb()
        movie = ia.get_movie(movie_id)
        return movie['full-size cover url']

    def display(self):
        print(f"""
            ===========================
            imdb id: {self._imdb_id}
            title: {self._title}
            year: {self._year}
            plot: {self._plot}
            category: {self._category}
            director: {self._director}
            cast: {self._cast}
            country: {self._country}
            picture: {self._picture}
            ===========================
        """)

    @staticmethod
    def is_empty():
        try:
            Movie.objects.all()[0]
            return False
        except IndexError:
            return True

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

    def _get_picture(self):
        return self._picture

    imdb_id = property(_get_imdb_id)
    title = property(_get_title)
    year = property(_get_year)
    plot = property(_get_plot)
    category = property(_get_category)
    director = property(_get_director)
    cast = property(_get_cast)
    country = property(_get_country)
    picture = property(_get_picture)
