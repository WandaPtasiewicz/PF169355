from unittest.mock import MagicMock

magic_mock = MagicMock()

magic_mock.__len__.return_value = 5
magic_mock.__add__.return_value = "wynik dodawania"
magic_mock.__getitem__.side_effect = lambda key: f"wartość dla {key}"
print(len(magic_mock))
print(magic_mock+2)
print(magic_mock["cat"])
magic_mock.__add__.return_value = "wynik dodawania"
magic_mock.__getitem__.side_effect = lambda key: f"wartość dla {key}"
magic_mock.__str__.return_value = "wow wow"
print(str(magic_mock))

mock_context = MagicMock()
mock_context.__enter__.return_value = "mur beton"
mock_context.__exit__.return_value = False

with mock_context as context:
    print(context)
