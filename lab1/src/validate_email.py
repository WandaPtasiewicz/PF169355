

def validate_email (string):
    if not isinstance(string,str):
        raise TypeError

    return string.find("@") >= 0