import datetime
import unittest

from parameterized import parameterized

from src.movie import Movie, MovieGenre
from src.movie_rental_shop import MovieRentalShop
from src.user import User, UserRole


class TestMovieRentalShop(unittest.TestCase):

    def setUp(self):
        self.valid_movie_rental_shop = MovieRentalShop("Best Movies in Town",
                                                       "Olsztyn")
        self.test_client = User("Mariusz", "Ser", 123456789,
                                datetime.date(2006, 1, 23), UserRole.CLIENT)
        self.test_employee = User("Wanda", "Ser", 123456788,
                                  datetime.date(2000, 11, 23),
                                  UserRole.EMPLOYEE)
        self.valid_movie_rental_shop.add_user(self.test_client)
        self.valid_movie_rental_shop.add_user(self.test_employee)
        self.test_movie = Movie(1, "Garfild", "Pedro Pascal",
                                2024, MovieGenre.COMEDY)
        self.valid_movie_rental_shop.add_movie(self.test_movie)

    def test_movie_rental_shop_initialization(self):
        self.assertEqual(self.valid_movie_rental_shop.name,
                         "Best Movies in Town")
        self.assertEqual(self.valid_movie_rental_shop.location, "Olsztyn")
        self.assertEqual(self.valid_movie_rental_shop.creation_date,
                         datetime.date.today())
        self.assertIn(self.test_client, self.valid_movie_rental_shop.users)
        self.assertIn(self.test_employee, self.valid_movie_rental_shop.users)
        self.assertIn(self.test_movie, self.valid_movie_rental_shop.movies)

    @parameterized.expand([
        Movie(12, "Harry Potter 1", "J.K.Rowling", 2000, MovieGenre.FANTASY),
        Movie(13, "Harry Potter 2", "J.K.Rowling", 2002, MovieGenre.FANTASY),
        Movie(14, "Harry Potter 3", "J.K.Rowling", 2004, MovieGenre.FANTASY)
    ])
    def test_add_movie_positive(self, movie):
        self.valid_movie_rental_shop.add_movie(movie)

    @parameterized.expand([
        ("user1", User("Wanda", "Nowak", 123123123,
                       datetime.date(2010, 7, 25), UserRole.CLIENT)),
        ("user2", User("Wanda", "Nowak", 333222333,
                       datetime.date(2010, 3, 25), UserRole.CLIENT)),
        ("user3", User("Wanda", "Nowak", 111222111,
                       datetime.date(2010, 1, 25), UserRole.CLIENT)),
    ])
    def test_add_users_positive(self, _, user):
        self.valid_movie_rental_shop.add_user(user)

    def test_add_the_same_movie_negative(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie_rental_shop.add_movie(self.test_movie)
        self.assertEqual(str(context.exception),
                         "Movie with this id is already in the shop")

    def test_negative_add_movie_with_used_id(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie_rental_shop.add_movie(
                Movie(1, "Smerfy", "George Lukas",
                      2013, MovieGenre.COMEDY))
        self.assertEqual(str(context.exception),
                         "Movie with this id is already in the shop")

    def test_add_the_same_user_negative(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie_rental_shop.add_user(
                self.test_employee)
        self.assertEqual(str(context.exception),
                         "This user is already in system")

    def test_add_user_invalid_data(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie_rental_shop.add_user("user")
        self.assertEqual(str(context.exception), "Invalid data")

    def test_add_the_same_phone_negative(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie_rental_shop.add_user(
                User("Piotr", "Piotrowski", 123456789,
                     datetime.date(2001, 1, 1), UserRole.CLIENT))
        self.assertEqual(str(context.exception),
                         "This phone number is already in use")

    def test_remove_movie(self):
        self.valid_movie_rental_shop.remove_movie(self.test_movie)
        self.assertNotIn(self.test_movie, self.valid_movie_rental_shop.movies)

    def test_remove_user(self):
        self.test_client.active = False
        self.valid_movie_rental_shop.remove_user(self.test_client)
        self.assertNotIn(self.test_client, self.valid_movie_rental_shop.users)

    def test_error_remove_active_user(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie_rental_shop.remove_user(self.test_client)
        self.assertEqual(str(context.exception),
                         "Cannot remove active account")

    def test_error_remove_user(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie_rental_shop.remove_user(
                User("Maciek", "Mydło", 333666777,
                     datetime.date(2000, 2, 12), UserRole.EMPLOYEE))
        self.assertEqual(str(context.exception), "User not found")

    def test_error_remove_rented_movie(self):
        self.test_movie.available = False
        with self.assertRaises(ValueError) as context:
            self.valid_movie_rental_shop.remove_movie(self.test_movie)
        self.assertEqual(str(context.exception),
                         "This movie is rented right now")

    def test_error_remove_movie(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie_rental_shop.remove_movie(
                Movie(4, "Minions", "Lordofon",
                      2022, MovieGenre.ADVENTURE))
        self.assertEqual(str(context.exception), "Movie not found")

    def test_positive_find_movie_by_id(self):
        find_movie = self.valid_movie_rental_shop.find_movie_by_id(1)
        self.assertEqual(self.test_movie, find_movie)

    def test_negative_find_movie_by_id(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie_rental_shop.find_movie_by_id(3)
        self.assertEqual(str(context.exception), "Movie not found")

    def test_positive_find_movie_by_title(self):
        find_movies = (self.valid_movie_rental_shop.
                       find_movie_by_title("Garfild"))
        self.assertIn(self.test_movie, find_movies)

    def test_negative_find_movie_by_title(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie_rental_shop.find_movie_by_title("Shrek")
        self.assertEqual(str(context.exception), "Movie not found")

    def test_positive_find_movies_by_title(self):
        test_movie2 = Movie(2, "Garfild", "Lolek", 2024,
                            MovieGenre.COMEDY)
        self.valid_movie_rental_shop.add_movie(test_movie2)
        find_movies = (self.valid_movie_rental_shop.
                       find_movie_by_title("Garfild"))
        self.assertEqual(find_movies, [self.test_movie, test_movie2])

    def test_positive_find_movie_by_director(self):
        find_movies = (self.valid_movie_rental_shop.
                       find_movies_by_director("Pedro Pascal"))
        self.assertIn(self.test_movie, find_movies)

    def test_negative_find_movie_by_director(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie_rental_shop.find_movies_by_director("Shrek")
        self.assertEqual(str(context.exception), "Movie not found")

    def test_positive_find_movies_by_director(self):
        test_movie2 = Movie(2, "Garfild", "Pedro Pascal", 2024,
                            MovieGenre.COMEDY)
        test_movie3 = Movie(8, "Garfild", "Lolek", 2024,
                            MovieGenre.COMEDY)
        self.valid_movie_rental_shop.add_movie(test_movie3)
        self.valid_movie_rental_shop.add_movie(test_movie2)
        find_movies = (self.valid_movie_rental_shop.
                       find_movies_by_director("Pedro Pascal"))
        self.assertEqual(find_movies, [self.test_movie, test_movie2])

    def test_positive_find_movie_by_genre(self):
        find_movies = self.valid_movie_rental_shop.find_movies_by_genre(
            MovieGenre.COMEDY)
        self.assertIn(self.test_movie, find_movies)

    def test_negative_find_movie_by_genre(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie_rental_shop.find_movies_by_director(
                MovieGenre.HORROR)
        self.assertEqual(str(context.exception), "Movie not found")

    def test_positive_find_movies_by_genre(self):
        test_movie2 = Movie(2, "Garfild", "Pedro Pascal", 2024,
                            MovieGenre.COMEDY)
        test_movie3 = Movie(8, "Garfild", "Lolek", 2024,
                            MovieGenre.ADVENTURE)
        self.valid_movie_rental_shop.add_movie(test_movie3)
        self.valid_movie_rental_shop.add_movie(test_movie2)
        find_movies = (self.valid_movie_rental_shop.
                       find_movies_by_genre(MovieGenre.COMEDY))
        self.assertEqual(find_movies, [self.test_movie, test_movie2])

    def test_positive_find_movie_by_release_year(self):
        find_movies = (self.valid_movie_rental_shop.
                       find_movies_by_release_year(2024))
        self.assertIn(self.test_movie, find_movies)

    def test_negative_find_movie_by_release_year(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie_rental_shop.find_movies_by_release_year(2002)
        self.assertEqual(str(context.exception), "Movie not found")

    def test_positive_find_movies_by_release_year(self):
        test_movie2 = Movie(5, "Kot w butavh", "Pedro Pascal", 2024,
                            MovieGenre.COMEDY)
        test_movie3 = Movie(8, "Garfild", "Lolek", 2022,
                            MovieGenre.ADVENTURE)
        self.valid_movie_rental_shop.add_movie(test_movie3)
        self.valid_movie_rental_shop.add_movie(test_movie2)
        find_movies = (
            self.valid_movie_rental_shop.find_movies_by_release_year(2024))
        self.assertEqual(find_movies, [self.test_movie, test_movie2])

    def test_positive_find_movie_by_age_limit_0(self):
        find_movies = self.valid_movie_rental_shop.find_movies_by_age_limit(0)
        self.assertEqual(find_movies, [self.test_movie])

    def test_positive_find_movie_by_age_limit(self):
        test_movie2 = Movie(5, "Kot w butavh", "Pedro Pascal", 2024,
                            MovieGenre.COMEDY, 18)
        test_movie3 = Movie(8, "Garfild", "Lolek", 2022,
                            MovieGenre.ADVENTURE, 16)
        self.valid_movie_rental_shop.add_movie(test_movie3)
        self.valid_movie_rental_shop.add_movie(test_movie2)
        find_movies = self.valid_movie_rental_shop.find_movies_by_age_limit(16)
        self.assertEqual(find_movies, [self.test_movie, test_movie3])

    def test_error_find_movie_by_age_limit(self):
        self.valid_movie_rental_shop.remove_movie(self.test_movie)
        test_movie2 = Movie(4, "Rambo", "Al Pacino", 1988,
                            MovieGenre.ADVENTURE, 14)
        self.valid_movie_rental_shop.add_movie(test_movie2)
        with self.assertRaises(ValueError) as context:
            self.valid_movie_rental_shop.find_movies_by_age_limit(6)
        self.assertEqual(str(context.exception), "Movie not found")

    def test_all_movies(self):
        self.assertEqual(self.valid_movie_rental_shop.all_movies(),
                         [self.test_movie])

    def test_all_users(self):
        self.assertEqual(self.valid_movie_rental_shop.all_users(),
                         [self.test_client, self.test_employee])

    def test_find_users_by_first_name(self):
        self.assertEqual(
            self.valid_movie_rental_shop.find_users_by_first_name("Mariusz"),
            [self.test_client])

    def test_find_users_by_last_name(self):
        self.assertEqual(
            self.valid_movie_rental_shop.find_users_by_last_name("Ser"),
            [self.test_client, self.test_employee])

    def test_find_users_by_birth_name(self):
        self.assertEqual(self.valid_movie_rental_shop.find_users_by_birth(
            datetime.date(2000, 11, 23)), [self.test_employee])

    def test_find_active_users(self):
        self.assertEqual(self.valid_movie_rental_shop.find_active_users(),
                         [self.test_client, self.test_employee])

    def test_find_inactive_users(self):
        self.test_client.deactivate()
        self.assertEqual(self.valid_movie_rental_shop.find_inactive_users(),
                         [self.test_client])

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
