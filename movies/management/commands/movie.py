import imdb
import csv
import os


class MovieToDB:
    """
    class used for insert
    Movies on DB
    """

    def __init__(
        self,
        title,
        year,
        plot,
        category,
        director,
        cast,
        country,
        picture
    ):
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
        """
        Load CSV file
        """
        path = os.path.dirname(os.path.abspath(__file__))
        file = open(path + '/imdb_movies.csv')
        reader = csv.reader(file)
        next(reader)
        return reader

    @staticmethod
    def parse(csv_file):
        """
        Parse CSV file and get data we need
        (title, year, plot, category, director,
        cast, country, picture)
        """
        list_objects = list()
        for row in csv_file:
            list_objects.append(MovieToDB.get(
                row[1],
                row[3],
                row[13],
                row[5],
                row[9],
                row[12],
                row[7],
                # MovieToDB.get_picture(row[0].split('tt')[1])
                None
            ))
            print(row[0].split('tt')[1])
        return list_objects

    @staticmethod
    def get(title,
            year,
            plot,
            category,
            director,
            cast,
            country,
            picture):
        """
        Instanciate movie object
        """
        return MovieToDB(
            title,
            year,
            plot,
            category,
            director,
            cast,
            country,
            picture
        )

    def display(self):
        """
        display movies in readable way
        """
        print(f"""
            ===========================
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
    def get_picture(movie_id):
        """
        get picture link from imdb python wrapper
        """
        ia = imdb.IMDb()
        movie = ia.get_movie(movie_id)
        return movie['full-size cover url']

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

    title = property(_get_title)
    year = property(_get_year)
    plot = property(_get_plot)
    category = property(_get_category)
    director = property(_get_director)
    cast = property(_get_cast)
    country = property(_get_country)
    picture = property(_get_picture)
