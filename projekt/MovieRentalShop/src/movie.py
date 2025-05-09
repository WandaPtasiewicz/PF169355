import datetime
from enum import Enum, auto
from src.user import age_from_date, User


class MovieGenre(Enum):
    COMEDY = auto()
    HORROR = auto()
    THRILLER = auto()
    FANTASY = auto()
    MYSTERY = auto()
    ROMANCE = auto()
    ACTION = auto()
    ADVENTURE = auto()
    SCIENCE_FICTION = auto()


class Movie:
    def __init__(self, id, title, director, release_year,
                 genre, age_limit=0):

        self.id = id
        self.title = title
        self.director = director
        self.genre = genre
        self.age_limit = age_limit
        self.release_year = release_year

        self.available = True
        self.rent_date = None
        self.rented_by = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError("id must be an integer")
        if value < 0:
            raise ValueError("id must be greater than zero")
        self._id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Title must be a non-empty string")
        if not value[0].isupper():
            raise ValueError("Title must start with capital letter")
        self._title = value

    @property
    def director(self):
        return self._director

    @director.setter
    def director(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Director must be a non-empty string")
        if not value[0].isupper():
            raise ValueError("Director must start with capital letter")
        self._director = value

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        if not value or not isinstance(value, MovieGenre):
            raise ValueError("Invalid genre")
        self._genre = value

    @property
    def age_limit(self):
        return self._age_limit

    @age_limit.setter
    def age_limit(self, value):
        if not isinstance(value, int):
            raise ValueError("Age limit must be a number")

        if value < 0:
            raise ValueError("Age limit can't less than 0")
        self._age_limit = value

    @property
    def release_year(self):
        return self._release_year

    @release_year.setter
    def release_year(self, value):
        if not isinstance(value, int):
            raise ValueError("Release year must be a number")

        if value < 1888 or value > datetime.datetime.now().year:
            raise ValueError(f"Invalid release year: {value}")
        self._release_year = value

    def rent_movie(self, user):
        if not isinstance(user, User):
            raise ValueError("User not found")
        if not self.available:
            raise ValueError("This movie is already rented")

        if age_from_date(user.birth) < self.age_limit:
            raise ValueError("You are too young to rent this movie")

        self.available = False
        self.rent_date = datetime.datetime.now()
        self.rented_by = user

    def return_movie(self):
        if self.available:
            raise ValueError("This movie is already returned")

        self.available = True
        self.rent_date = None
        self.rented_by = None
