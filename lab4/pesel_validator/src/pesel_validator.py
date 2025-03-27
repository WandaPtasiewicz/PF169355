import re

class PeselValidator:

    def validate_format(pesel):
        if not isinstance(pesel, str):
            pesel = str(pesel)
        return bool(re.fullmatch(r"\d{11}", pesel))

    def validate_check_digit(pesel):
        pesel = [int(digit) for digit in str(pesel)]
        wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        suma_kontrolna = sum(p * w for p, w in zip(pesel[:10], wagi))
        cyfra_kontrolna = (10 - (suma_kontrolna % 10)) % 10
        return cyfra_kontrolna == pesel[10]
