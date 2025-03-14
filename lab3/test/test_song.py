import unittest
from collections import Counter

from src.song import Song

class TestSongInitialization(unittest.TestCase):

    def setup(self):
        pass

    def test_creation(self):
        song1 = Song("Bohemian Rhapsody",355)
        self.assertIsInstance(song1, Song)

    def test_creation_error(self):
        with self.assertRaises(ValueError) as context:
            song1 = Song("Bohemian Rhapsody",-3)
        self.assertEqual(str(context.exception), "duration can't be negative ")

    def test_initialization(self):
        song1 = Song("Bohemian Rhapsody",355)
        self.assertEqual(song1.title,"Bohemian Rhapsody")
        self.assertEqual(song1.duration,355)

    def test_calculate_royalty(self):
        song1 = Song("Bohemian Rhapsody",355)
        self.assertAlmostEqual(song1.calculate_royalty(),3.55)
        song2 = Song("Yesterday",125)
        self.assertAlmostEqual(song2.calculate_royalty(),1.25)

    def test_calculate_royalty_zero(self):
        song2 = Song("Yesterday",0)
        self.assertAlmostEqual(song2.calculate_royalty(),0.00)

    def test_add_artist(self):
        song1 = Song("Bohemian Rhapsody",355)
        song1.add_artist("Freddie Mercury")
        self.assertIn("Freddie Mercury", song1.artists)
        song1.add_artist("BrianMay")
        song1.add_artist("Roger Taylor")
        self.assertIn("BrianMay", song1.artists)
        self.assertIn("Roger Taylor", song1.artists)

    def test_add_artist_twice(self):
        song1 = Song("Bohemian Rhapsody",355)
        song1.add_artist("Freddie Mercury")
        self.assertIn("Freddie Mercury", song1.artists)
        song1.add_artist("Freddie Mercury")
        number_of_artists= Counter(song1.artists)
        self.assertEqual(number_of_artists["Freddie Mercury"],2)

    def test_add_artist_error(self):
        song1 = Song("Bohemian Rhapsody", 355)
        with self.assertRaises(ValueError) as context:
            song1.add_artist("")

        self.assertEqual(str(context.exception), "Artist name cannot be empty")

    def tearDown(self):
        pass

if __name__ == "__main__":
     unittest.main()

