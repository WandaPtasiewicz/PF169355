
class StringManipulator:

    def reverse_string(self,string):
        return string[::-1]

    def capitalize_words(self,string):
        return string.title()

    def count_words(self,string):
        return len(string.split())