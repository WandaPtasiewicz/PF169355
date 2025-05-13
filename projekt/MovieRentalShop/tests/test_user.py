import datetime
import unittest
from src.movie import Movie, MovieGenre
from src.user import User, UserRole


class TestUser(unittest.TestCase):

    def setUp(self):
        self.valid_user = User("Jacek", "Placek", 123444555,
                               datetime.date(2010, 7, 25), UserRole.CLIENT)
        self.test_movie = Movie(4, "Notatnik", "Rayn Gosling",
                                1998, MovieGenre.ROMANCE)

    def test_user_initialization(self):
        self.assertEqual(self.valid_user.first_name, "Jacek")
        self.assertEqual(self.valid_user.last_name, "Placek")
        self.assertEqual(self.valid_user.phone, 123444555)
        self.assertEqual(self.valid_user.birth, datetime.date(2010, 7, 25))
        self.assertEqual(self.valid_user.role, UserRole.CLIENT)
        self.assertEqual(self.valid_user.register_date, datetime.date.today())
        self.assertEqual(self.valid_user.rented_movies, [])
        self.assertEqual(self.valid_user.all_rented_movies, [])
        self.assertEqual(self.valid_user.active, True)

    def test_creation_positive(self):
        user1 = User("Mariusz", "Gork", 999666333,
                     datetime.date(2000, 3, 12), UserRole.EMPLOYEE)
        self.assertIsInstance(user1, User)

    def test_setup_first_name_positive(self):
        self.valid_user.first_name = "Magda"
        self.assertEqual("Magda", self.valid_user.first_name)

    def test_setup_first_name_negative(self):
        self.valid_user.first_name = "Magda"
        self.assertNotEqual("Magd", self.valid_user.first_name)

    def test_setup_last_name_positive(self):
        self.valid_user.last_name = "Magda"
        self.assertEqual("Magda", self.valid_user.last_name)

    def test_setup_last_name_negative(self):
        self.valid_user.last_name = "Magda"
        self.assertNotEqual("Magd", self.valid_user.last_name)

    def test_setup_phone_positive(self):
        self.valid_user.phone = 123444757
        self.assertEqual(123444757, self.valid_user.phone)

    def test_setup_phone_negative(self):
        self.valid_user.phone = 123444757
        self.assertNotEqual(123494757, self.valid_user.phone)

    def test_setup_birth_positive(self):
        self.valid_user.birth = datetime.date(2000, 3, 22)
        self.assertEqual(datetime.date(2000, 3, 22), self.valid_user.birth)

    def test_setup_birth_negative(self):
        self.valid_user.birth = datetime.date(2000, 3, 22)
        self.assertNotEqual(datetime.date(2000, 9, 22), self.valid_user.birth)

    def test_error_creation_too_short_phone(self):
        with self.assertRaises(ValueError) as context:
            User("Mariusz", "Gork", 99966,
                 datetime.date(2000, 3, 12),
                 UserRole.EMPLOYEE)
        self.assertEqual(str(context.exception),
                         "Phone number must be 9 digits")

    def test_error_too_short_phone(self):
        with self.assertRaises(ValueError) as context:
            self.valid_user.phone = 9
        self.assertEqual(str(context.exception),
                         "Phone number must be 9 digits")

    def test_error_creation_letters_phone(self):
        with self.assertRaises(ValueError) as context:
            User("Mariusz", "Gork", "233abc",
                 datetime.date(2000, 3, 12), UserRole.EMPLOYEE)
        self.assertEqual(str(context.exception),
                         "Phone number must only contain numbers")

    def test_error_letters_phone(self):
        with self.assertRaises(ValueError) as context:
            self.valid_user.phone = "osiem"
        self.assertEqual(str(context.exception),
                         "Phone number must only contain numbers")

    def test_error_creation_too_young_user(self):
        with self.assertRaises(ValueError) as context:
            User("Mariusz", "Gork", 999666123,
                 datetime.date(2020, 3, 12), UserRole.CLIENT)
        self.assertEqual(str(context.exception),
                         "You are too young to rent movies")

    def test_error_too_young_user(self):
        with self.assertRaises(ValueError) as context:
            self.valid_user.birth = datetime.date(2022, 12, 12)
        self.assertEqual(str(context.exception),
                         "You are too young to rent movies")

    def test_error_creation_birth(self):
        with self.assertRaises(ValueError) as context:
            User("Mariusz", "Gork", 999900866,
                 "marzec", UserRole.EMPLOYEE)
        self.assertEqual(str(context.exception), "Invalid birth date")

    def test_error_birth(self):
        with self.assertRaises(ValueError) as context:
            self.valid_user.birth = 3
        self.assertEqual(str(context.exception), "Invalid birth date")

    def test_error_creation_role(self):
        with self.assertRaises(ValueError) as context:
            User("Mariusz", "Gork", 999900866,
                 datetime.date(1993, 5, 8), "klient")
        self.assertEqual(str(context.exception), "Invalid role")

    def test_error_role(self):
        with self.assertRaises(ValueError) as context:
            self.valid_user.role = "mama"
        self.assertEqual(str(context.exception), "Invalid role")

    def test_error_creation_first_name_capital(self):
        with self.assertRaises(ValueError) as context:
            User("mariusz", "Gork", 999900866,
                 datetime.date(1993, 5, 8), UserRole.CLIENT)
        self.assertEqual(str(context.exception),
                         "First name must start with capital letter")

    def test_error_first_name_capital(self):
        with self.assertRaises(ValueError) as context:
            self.valid_user.first_name = "maciek"
        self.assertEqual(str(context.exception),
                         "First name must start with capital letter")

    def test_error_creation_last_name_capital(self):
        with self.assertRaises(ValueError) as context:
            User("Mariusz", "ork", 999900866,
                 datetime.date(1993, 5, 8), UserRole.CLIENT)
        self.assertEqual(str(context.exception),
                         "Last name must start with capital letter")

    def test_error_last_name_capital(self):
        with self.assertRaises(ValueError) as context:
            self.valid_user.last_name = "macie"
        self.assertEqual(str(context.exception),
                         "Last name must start with capital letter")

    def test_error_creation_numbers_in_first_name(self):
        with self.assertRaises(ValueError) as context:
            User("M4riusz", "Gork", 999900866,
                 datetime.date(1993, 5, 8), UserRole.CLIENT)
        self.assertEqual(str(context.exception),
                         "First name must only contain letters")

    def test_error_numbers_in_first_name(self):
        with self.assertRaises(ValueError) as context:
            self.valid_user.first_name = "Maj2"
        self.assertEqual(str(context.exception),
                         "First name must only contain letters")

    def test_error_creation_numbers_in_last_name(self):
        with self.assertRaises(ValueError) as context:
            User("Mariusz", "L0rk", 999900866,
                 datetime.date(1993, 5, 8),
                 UserRole.CLIENT)
        self.assertEqual(str(context.exception),
                         "Last name must only contain letters")

    def test_error_numbers_in_last_name(self):
        with self.assertRaises(ValueError) as context:
            self.valid_user.last_name = "Ma5j"
        self.assertEqual(str(context.exception),
                         "Last name must only contain letters")

    def test_rent_movie_positive(self):
        self.valid_user.rent_movie(self.test_movie)
        self.assertFalse(self.test_movie.available)
        self.assertEqual(self.test_movie.rented_by, self.valid_user)
        self.assertIsNotNone(self.test_movie.rent_date)
        self.assertIn(self.test_movie, self.valid_user.rented_movies)

    def test_error_rent_movie_already_rented(self):
        self.test_movie.available = False
        with self.assertRaises(ValueError) as context:
            self.valid_user.rent_movie(self.test_movie)
        self.assertEqual(str(context.exception),
                         "This movie is already rented")

    def test_error_rent_movie_too_young_user(self):
        self.test_movie.age_limit = 18
        with self.assertRaises(ValueError) as context:
            self.valid_user.rent_movie(self.test_movie)
        self.assertEqual(str(context.exception),
                         "You are too young to rent this movie")

    def test_error_rent_movie_inactive_user(self):
        self.valid_user.active = False
        with self.assertRaises(ValueError) as context:
            self.valid_user.rent_movie(self.test_movie)
        self.assertEqual(str(context.exception),
                         "Your account has been deactivated")

    def test_error_rent_rented_movie(self):
        self.valid_user.rent_movie(self.test_movie)
        with self.assertRaises(ValueError) as context:
            self.valid_user.rent_movie(self.test_movie)
        self.assertEqual(str(context.exception),
                         "You already rented this movie")

    def test_error_employee_rent_movie(self):
        self.valid_user.role = UserRole.EMPLOYEE
        with self.assertRaises(ValueError) as context:
            self.valid_user.rent_movie(self.test_movie)
        self.assertEqual(str(context.exception),
                         "Only user can rent a movie")

    def test_error_return_returned_movie(self):
        with self.assertRaises(ValueError) as context:
            self.valid_user.return_movie(self.test_movie)
        self.assertEqual(str(context.exception),
                         "You already returned this movie")

    def test_return_movie_positive(self):
        self.valid_user.rent_movie(self.test_movie)
        self.valid_user.return_movie(self.test_movie)
        self.assertTrue(self.test_movie.available)
        self.assertEqual(self.test_movie.rented_by, None)
        self.assertIsNone(self.test_movie.rent_date)
        self.assertNotIn(self.test_movie, self.valid_user.rented_movies)

    def test_error_deactivate_user_with_rented_movie(self):
        self.valid_user.rent_movie(self.test_movie)
        with self.assertRaises(ValueError) as context:
            self.valid_user.deactivate()
        self.assertEqual(str(context.exception),
                         "Cannot deactivate user with rented movies")

    def test_deactivate_user_positive(self):
        self.valid_user.deactivate()
        self.assertFalse(self.valid_user.active)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
