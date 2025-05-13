import datetime
from enum import Enum, auto


class UserRole(Enum):
    CLIENT = auto()
    EMPLOYEE = auto()
    ADMIN = auto()


def age_from_date(date):
    age = datetime.datetime.now().year - date.year
    if ((datetime.datetime.now().month, datetime.datetime.now().day) <
            (date.month, date.day)):
        age -= 1
    return age


class User:

    def __init__(self, first_name, last_name, phone, birth, role):

        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.phone = phone
        self.birth = birth
        self.register_date = datetime.date.today()
        self.rented_movies = []
        self.all_rented_movies = []
        self.active = True

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not value or not value[0].isupper():
            raise ValueError("First name must start with capital letter")
        if any(char.isdigit() for char in value):
            raise ValueError("First name must only contain letters")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not value or not value[0].isupper():
            raise ValueError("Last name must start with capital letter")
        if any(char.isdigit() for char in value):
            raise ValueError("Last name must only contain letters")
        self._last_name = value

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        if not isinstance(value, UserRole):
            raise ValueError("Invalid role")
        self._role = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if not isinstance(value, int):
            raise ValueError("Phone number must only contain numbers")
        if len(str(value)) != 9:
            raise ValueError("Phone number must be 9 digits")
        self._phone = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        if not isinstance(value, datetime.date):
            raise ValueError("Invalid birth date")
        if age_from_date(value) < 10:
            raise ValueError("You are too young to rent movies")
        self._birth = value

    def rent_movie(self, movie):
        if not self.active:
            raise ValueError("Your account has been deactivated")
        if movie in self.rented_movies:
            raise ValueError("You already rented this movie")
        if not self.role == UserRole.CLIENT:
            raise ValueError("Only user can rent a movie")

        movie.rent_movie(self)
        self.rented_movies.append(movie)
        self.all_rented_movies.append(movie)
        return True

    def return_movie(self, movie):
        if not self.active:
            raise ValueError("Your account has been deactivated")

        if movie not in self.rented_movies:
            raise ValueError("You already returned this movie")

        movie.return_movie()
        self.rented_movies.remove(movie)

    def deactivate(self):
        if self.rented_movies:
            raise ValueError("Cannot deactivate user with rented movies")
        self.active = False
        return True

    def activate(self):
        self.active = True
        return True
