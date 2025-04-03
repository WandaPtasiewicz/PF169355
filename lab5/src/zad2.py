from unittest.mock import Mock

mock2 = Mock(autospec=True)
mock2.get_data.side_effect = [2.55, True, "egg"]

print(mock2.get_data(1))
print(mock2.get_data(2))
print(mock2.get_data(3))

def multi(args):
    return args*5


mock2.get_data.side_effect = multi
print(mock2.get_data(1))
print(mock2.get_data("milk"))

mock2.get_data.side_effect = ValueError("Wrong value")
try:
    mock2.get_data()
except ValueError as err:
    print(err)