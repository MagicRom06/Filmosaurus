import imdb
import requests
from bs4 import BeautifulSoup


class Rating:

    """
    class used to get rating from a movie
    """
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def request(self, url):
        """
        make request to an url and return json
        """
        search = url
        response = requests.get(search)
        return response.json()

    def get_allocine(self):
        """
        get allocine rating
        """
        allocine = Allocine(self.title, self.year)
        allocine.load()
        return allocine.rating()

    def get_imdb(self):
        """
        get imdb rating
        """
        return Imdb(self.title, self.year).rating()

    def get(self):
        """
        get final json that will be used in view
        to display rating
        """
        response = dict()
        response['ratings'] = [
            self.get_allocine(),
            self.get_imdb()
        ]
        return response


class Allocine(Rating):
    """
    class used to get allocine rating
    """
    def __init__(self, title, year):
        Rating.__init__(self, title, year)
        self.movie_requested = list()

    def load(self):
        """
        load data from allocine site with title
        """
        req = Rating(
            self.title,
            self.year).request(
                f"""https://www.allocine.fr/_/autocomplete/{self.title.capitalize()}"""
            )
        for elt in req['results']:
            if elt['entity_type'] == 'movie' and \
               (elt['data']['year'] == self.year or
               elt['data']['year'] == str(int(self.year) - 1)):
                self.movie_requested.append(elt['entity_id'])

    def rating(self):
        """
        get rating
        """
        if len(self.movie_requested) > 0:
            url = """https://www.allocine.fr/film/fichefilm_gen_cfilm={}.html""".format(
                self.movie_requested[0]
            )
            html_page = requests.get(url)
            soup = BeautifulSoup(html_page.text, 'html.parser')
            type_critic = soup.find_all("span", "rating-title")
            notes = soup.find_all("span", "stareval-note")
            if len(type_critic) > 1:
                return {
                    "allocine": {
                        "press": f"{notes[0].get_text()}/5",
                        "spectator": f"{notes[1].get_text()}/5",
                        "id": self.movie_requested[0]
                    }
                }
            elif len(type_critic) == 1:
                return {
                    "allocine": {
                        "press": "no data",
                        "spectator": f"{notes[0].get_text()}/5",
                        "id": self.movie_requested[0]
                    }
                }
            else:
                return {
                    "allocine": {
                        "press": "no data",
                        "spectator": "no data",
                    },
                    "id": self.movie_requested[0]
                }
        else:
            return {
                "allocine": {
                    "press": "no data",
                    "spectator": "no data",
                },
            }

    def requested_movie(self):
        return self.movie_requested


class Imdb(Rating):
    """
    get rating from imdb
    """
    def __init__(self, title, year):
        Rating.__init__(self, title, year)

    def rating(self):
        """
        get rating
        """
        ia = imdb.IMDb()
        movie_requested = list()
        search = ia.search_movie(self.title)
        for elt in search:
            if elt['kind'] == 'movie':
                if "year" in elt.keys():
                    if elt['year'] == int(self.year) or \
                       elt['year'] == (int(self.year) - 1) or \
                       elt['year'] == (int(self.year) + 1):
                        movie_requested.append(elt.getID())
        if len(movie_requested) > 0:
            movie = ia.get_movie(movie_requested[0])
            return {
                "imdb": f"{movie['rating']}/10",
                "id": movie_requested[0]
            }
        else:
            return {
                "imdb": "No data",
                "id": movie_requested[0]
            }


# flake8: noqa
