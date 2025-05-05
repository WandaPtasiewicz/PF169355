import datetime
import unittest

from src.movie import Movie, MovieGenre
from src.user import User, UserRole


class TestMovie(unittest.TestCase):

    def setUp(self):
        self.valid_movie = Movie(2, "Rambo", "Adam Nowak", 2000, MovieGenre.ACTION,
                                 10)
        self.test_user = User("Maria", "Kowal", 123456789,
                              datetime.date(2000,1,13), UserRole.CLIENT)

    def test_movie_initialization(self):
        self.assertEqual(self.valid_movie.id, 2)
        self.assertEqual(self.valid_movie.title, "Rambo")
        self.assertEqual(self.valid_movie.director, "Adam Nowak")
        self.assertEqual(self.valid_movie.release_year, 2000)
        self.assertEqual(self.valid_movie.genre, MovieGenre.ACTION)
        self.assertTrue(self.valid_movie.available)
        self.assertIsNone(self.valid_movie.rent_date)
        self.assertIsNone(self.valid_movie.rented_by)

    def test_creation_positive(self):
        movie1 = Movie(1,"Indiana Jones", "John Bon",2002, MovieGenre.ACTION,12)
        self.assertIsInstance(movie1, Movie)

    def test_setter_id_positive(self):
        self.valid_movie.id = 2
        self.assertEqual(2, self.valid_movie.id)

    def test_setter_id_negative(self):
        self.valid_movie.id = 2
        self.assertNotEqual(self.valid_movie.title, 3)

    def test_setter_title_positive(self):
        self.valid_movie.title = "Avengers"
        self.assertEqual("Avengers", self.valid_movie.title)

    def test_setter_title_negative(self):
        self.valid_movie.title = "Avengers"
        self.assertNotEqual("Garfild", self.valid_movie.title)

    def test_setter_director_positive(self):
        self.valid_movie.director = "Avengers"
        self.assertEqual("Avengers", self.valid_movie.director)

    def test_setter_director_negative(self):
        self.valid_movie.title = "Avengers"
        self.assertNotEqual("Garfild", self.valid_movie.director)

    def test_setter_genre_positive(self):
        self.valid_movie.genre = MovieGenre.FANTASY
        self.assertEqual(MovieGenre.FANTASY, self.valid_movie.genre)

    def test_setter_genre_negative(self):
        self.valid_movie.genre = MovieGenre.FANTASY
        self.assertNotEqual(MovieGenre.COMEDY, self.valid_movie.genre)

    def test_setter_release_year_positive(self):
        self.valid_movie.release_year = 2000
        self.assertEqual(2000, self.valid_movie.release_year)

    def test_setter_release_year_negative(self):
        self.valid_movie.genre = MovieGenre.FANTASY
        self.assertNotEqual(1999, self.valid_movie.release_year)

    def test_setter_age_limit_positive(self):
        self.valid_movie.age_limit = 20
        self.assertEqual(20, self.valid_movie.age_limit)

    def test_setter_age_limit_negative(self):
        self.valid_movie.age_limit = 2
        self.assertNotEqual(1999, self.valid_movie.age_limit)

    def test_error_not_int_id(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie.id = "jedynka"
        self.assertEqual(str(context.exception), "id must be an integer")

    def test_error_creation_not_int_id(self):
        with self.assertRaises(ValueError) as context:
            test_movie2 = Movie("dwa", "Kokos", "Kot", 2002, MovieGenre.FANTASY, 7)
        self.assertEqual(str(context.exception), "id must be an integer")

    def test_error_creation_id_less_than_zero(self):
        with self.assertRaises(ValueError) as context:
            test_movie2 = Movie(-3, "Kokos", "Kot", 2002, MovieGenre.FANTASY, 7)
        self.assertEqual(str(context.exception), "id must be greater than zero")

    def test_error_id_less_than_zero(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie.id = -7
        self.assertEqual(str(context.exception), "id must be greater than zero")

    def test_error_creation_old_release_year(self):
        with self.assertRaises(ValueError) as context:
            movie1 = Movie(1,"Indiana Jones", "John Bon",2,MovieGenre.ACTION,12)
        self.assertEqual(str(context.exception), "Invalid release year: 2")

    def test_error_too_old_release_year(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie.release_year = 2
        self.assertEqual(str(context.exception), "Invalid release year: 2")

    def test_error_creation_not_int_release_year(self):
        with self.assertRaises(ValueError) as context:
            movie1 = Movie(1,"Indiana Jones", "John Bon","dwa",MovieGenre.ACTION,12)
        self.assertEqual(str(context.exception), "Release year must be a number")

    def test_error_not_int_release_year(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie.release_year = "dwa"
        self.assertEqual(str(context.exception), "Release year must be a number")

    def test_error_release_year_from_future(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie.release_year = 2222
        self.assertEqual(str(context.exception), "Invalid release year: 2222")

    def test_error_creation_release_year_from_future(self):
        with self.assertRaises(ValueError) as context:
            movie1 = Movie(1,"Indiana Jones", "John Bon",2222,MovieGenre.ACTION,12)
        self.assertEqual(str(context.exception), "Invalid release year: 2222")

    def test_creation_error_genre(self):
        with self.assertRaises(ValueError) as context:
            movie1 = Movie(1,"Indiana Jones", "John Bon",2000,"fajny",12)
        self.assertEqual(str(context.exception), "Invalid genre")

    def test_error_change_genre(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie.genre = "fajny"
        self.assertEqual(str(context.exception), "Invalid genre")

    def test_not_integer_age_limit(self):
        with self.assertRaises(ValueError):
            self.valid_movie.age_limit = "dwanascie"

    def test_creation_error_not_integer_age_limit(self):
        with self.assertRaises(ValueError) as context:
            movie1 = Movie(1,"Indiana Jones", "John Bon",2000,MovieGenre.FANTASY,"dwa")
        self.assertEqual(str(context.exception), "Age limit must be a number")

    def test_error_creation_age_limit_negative(self):
        with self.assertRaises(ValueError) as context:
            movie1 = Movie(1,"Indiana Jones", "John Bon",2000,MovieGenre.FANTASY,-3)
        self.assertEqual(str(context.exception), "Age limit can't less than 0")

    def test_error_age_limit_negative(self):
        with self.assertRaises(ValueError) as context:
           self.valid_movie.age_limit = -4
        self.assertEqual(str(context.exception), "Age limit can't less than 0")

    def test_error_age_limit_null(self):
        with self.assertRaises(ValueError) as context:
            movie1 = Movie(1,"Indiana Jones", "John Bon",2000,MovieGenre.FANTASY, "")
        self.assertEqual(str(context.exception), "Age limit must be a number")

    def test_creation_error_title_null(self):
        with self.assertRaises(ValueError) as context:
            movie1 = Movie(1,"", "John Bon",2000,MovieGenre.FANTASY,2)
        self.assertEqual(str(context.exception), "Title must be a non-empty string")

    def test_error_title_null(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie.title = ""
        self.assertEqual(str(context.exception), "Title must be a non-empty string")

    def test_creation_error_title_not_string(self):
        with self.assertRaises(ValueError) as context:
            movie1 = Movie(1,4.12, "John Bon",2000,MovieGenre.FANTASY,2)
        self.assertEqual(str(context.exception), "Title must be a non-empty string")

    def test_error_title_not_string(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie.title = 8
        self.assertEqual(str(context.exception), "Title must be a non-empty string")

    def test_creation_error_title_not_capital(self):
        with self.assertRaises(ValueError) as context:
            movie1 = Movie(1,"osiem", "Kiki",2000,MovieGenre.FANTASY,2)
        self.assertEqual(str(context.exception), "Title must start with capital letter")

    def test_error_title_not_capital(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie.title = "osiem"
        self.assertEqual(str(context.exception), "Title must start with capital letter")

    def test_creation_error_director_null(self):
        with self.assertRaises(ValueError) as context:
            movie1 = Movie(1,"K", "",2000,MovieGenre.FANTASY,2)
        self.assertEqual(str(context.exception), "Director must be a non-empty string")

    def test_error_director_null(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie.director = ""
        self.assertEqual(str(context.exception), "Director must be a non-empty string")

    def test_creation_error_director_not_string(self):
        with self.assertRaises(ValueError) as context:
            movie1 = Movie(1,"Cztery", 2,2000,MovieGenre.FANTASY,2)
        self.assertEqual(str(context.exception), "Director must be a non-empty string")

    def test_error_director_not_string(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie.director = 8
        self.assertEqual(str(context.exception), "Director must be a non-empty string")

    def test_creation_direction_title_not_capital(self):
        with self.assertRaises(ValueError) as context:
            movie1 = Movie(1,"Jsiem", "viki",2000,MovieGenre.FANTASY,2)
        self.assertEqual(str(context.exception), "Director must start with capital letter")

    def test_error_director_not_capital(self):
        with self.assertRaises(ValueError) as context:
            self.valid_movie.director = "osiem"
        self.assertEqual(str(context.exception), "Director must start with capital letter")

    def test_rent_movie(self):
        self.valid_movie.rent_movie(self.test_user)
        self.assertFalse(self.valid_movie.available)
        self.assertEqual(self.valid_movie.rented_by, self.test_user)
        self.assertIsNotNone(self.valid_movie.rent_date)

    def test_error_movie_is_rented(self):
        self.valid_movie.rent_movie(self.test_user)
        with self.assertRaises(ValueError):
            self.valid_movie.rent_movie(self.test_user)

    def test_error_too_young_to_rent_movie(self):
        young_user = User("Michał", "Kot", 123111222,
                          datetime.date(2010,12,11), UserRole.CLIENT)
        adult_movie = Movie(3, "Krwawa masakra", "John Miller", 2002, MovieGenre.HORROR, 18)

        with self.assertRaises(ValueError):
            adult_movie.rent_movie(young_user)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()