import unittest
from unittest.mock import Mock, call

from DataService import DataService


class TestDataService(unittest.TestCase):

    def setUp(self):
        self.api_mock = Mock()
        self.service = DataService(self.api_mock)

    def test_fetch_user_data_correct_values(self):
        self.api_mock.get_data.side_effect = [{'name': 'Jan'}, {'name': 'Anna'},ConnectionError(),{'name':'Jacek'}]

        result = self.service.fetch_user_data(1)
        self.assertEqual(result,{'name': 'Jan'})
        result2 = self.service.fetch_user_data(123)
        self.assertEqual(result2, {'name': 'Anna'})

        with self.assertRaises(ConnectionError) as context:
            result3 = self.service.fetch_user_data(3)

        self.api_mock(1)
        self.api_mock(1)
        self.api_mock(1)
        self.api_mock(1)

        result4 = self.service.fetch_user_data(4)
        self.assertEqual(result4, {'name': 'Jacek'})

        self.api_mock.get_data.assert_called()
        self.api_mock.assert_has_calls([
            call.get_data((1,)),
            call.get_data((123,)),
        ])

        self.assertEqual(self.api_mock.call_count,4)


    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()