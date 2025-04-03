from unittest.mock import Mock

mock3 = Mock()
mock3(25)
mock3("fiu")
mock3(2.44)
print(mock3.called)
print(mock3.call_count)
print(mock3.call_args)
print(mock3.call_args_list)


