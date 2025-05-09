import datetime
from src.user import User


class MovieRentalShop:
    def __init__(self, name, location):

        self.name = name
        self.location = location
        self.movies = list()
        self.users = list()
        self.creation_date = datetime.date.today()

    def add_movie(self, new_movie):
        if any(movie.id == new_movie.id for movie in self.movies):
            raise ValueError("Movie with this id is already in the shop")

        self.movies.append(new_movie)

    def remove_movie(self, movie):
        if movie not in self.movies:
            raise ValueError("Movie not found")

        if not movie.available:
            raise ValueError("This movie is rented right now")

        return self.movies.remove(movie)

    def remove_user(self, user):
        if user not in self.users:
            raise ValueError("User not found")

        if user.active:
            raise ValueError("Cannot remove active account")

        return self.users.remove(user)

    def add_user(self, new_user):
        if not isinstance(new_user, User):
            raise ValueError("Invalid data")
        if new_user in self.users:
            raise ValueError("This user is already in system")
        if any(user.phone == new_user.phone for user in self.users):
            raise ValueError("This phone number is already in use")
        self.users.append(new_user)

    def find_movie_by_id(self, movie_id):
        for movie in self.movies:
            if movie.id == movie_id:
                return movie
        raise ValueError("Movie not found")

    def find_movie_by_title(self, movie_title):
        find_movies = [movie for movie in self.movies
                       if movie.title == movie_title]
        if not find_movies:
            raise ValueError("Movie not found")
        return find_movies

    def find_movies_by_director(self, movie_director):
        find_movies = [movie for movie in self.movies
                       if movie.director == movie_director]
        if not find_movies:
            raise ValueError("Movie not found")
        return find_movies

    def find_movies_by_genre(self, movie_genre):
        find_movies = [movie for movie in self.movies
                       if movie.genre == movie_genre]
        if not find_movies:
            raise ValueError("Movie not found")
        return find_movies

    def find_movies_by_release_year(self, movie_release_year):
        find_movies = [movie for movie in self.movies
                       if movie.release_year == movie_release_year]
        if not find_movies:
            raise ValueError("Movie not found")
        return find_movies

    def find_movies_by_age_limit(self, movie_age_limit):
        find_movies = [movie for movie in self.movies
                       if movie.age_limit <= movie_age_limit]
        if not find_movies:
            raise ValueError("Movie not found")
        return find_movies

    def find_user_by_phone(self, phone):
        for user in self.users:
            if user.phone == phone:
                return user
        raise ValueError("Movie not found")

    def find_users_by_first_name(self, first_name):
        find_users = [user for user in self.users
                      if user.first_name == first_name]
        if not find_users:
            raise ValueError("User not found")
        return find_users

    def find_users_by_last_name(self, last_name):
        find_users = [user for user in self.users
                      if user.last_name == last_name]
        if not find_users:
            raise ValueError("User not found")
        return find_users

    def find_users_by_birth(self, birth):
        find_users = [user for user in self.users
                      if user.birth == birth]
        if not find_users:
            raise ValueError("User not found")
        return find_users

    def find_active_users(self):
        find_users = [user for user in self.users
                      if user.active]
        if not find_users:
            raise ValueError("User not found")
        return find_users

    def find_inactive_users(self):
        find_users = [user for user in self.users
                      if not user.active]
        if not find_users:
            raise ValueError("User not found")
        return find_users

    def all_movies(self):
        return self.movies

    def all_users(self):
        return self.users
