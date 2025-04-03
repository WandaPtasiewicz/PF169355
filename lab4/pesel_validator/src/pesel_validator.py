import re
from datetime import datetime

from attr.setters import validate


class PeselValidator:

    def validate_format(pesel):
        """
        Check if pesel have right format (11 numbers)
        Args:
            pesel (str): The pesel.
        Returns:
            bool: The product of function.
        """

        if not isinstance(pesel, str):
            pesel = str(pesel)
        return bool(re.fullmatch(r"\d{11}", pesel))

    def validate_check_digit(pesel):
        """
        Check if pesel have right control number
        Args:
            pesel (str): The pesel.
        Returns:
            bool: The product of function.
        """
        pesel = [int(digit) for digit in str(pesel)]
        wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        suma_kontrolna = sum(p * w for p, w in zip(pesel[:10], wagi))
        cyfra_kontrolna = (10 - (suma_kontrolna % 10)) % 10
        return cyfra_kontrolna == pesel[10]

    def validate_birth_date(pesel, date_birth) :
        """
        Check if date_birth is corect according to pesel
        Args:
            pesel (str): The pesel.
            date_birth (str): The date of bith.
        Returns:
            bool: The product of function.
        """
        pesel = str(pesel)
        year = int(pesel[0:2])
        month = int(pesel[2:4])
        day = int(pesel[4:6])

        if 1 <= month <= 12:
            wiek = 1900
        elif 21 <= month <= 32:
            wiek = 2000
            month -= 20
        elif 41 <= month <= 52:
            wiek = 2100
            month -= 40
        elif 61 <= month <= 72:
            wiek = 2200
            month -= 60
        elif 81 <= month <= 92:
            wiek = 1800
            month -= 80
        else:
            return False

        year += wiek
        try:
            data_z_peselu = datetime(year, month, day).strftime("%Y-%m-%d")
            return data_z_peselu == date_birth
        except ValueError:
            return False

    def get_gender(pesel):
        """
        Check what gender  according to pesel
        Args:
            pesel (str): The pesel.
        Returns:
            str: The gender from pesel.
    """
        pesel = str(pesel)
        return "M" if int(pesel[9]) % 2 == 1 else "K"

    def is_valid(pesel, date_birth, gender):
        """
        Validate pesel
        Args:
            pesel (str): The pesel.
            date_birth (str): The date of birth.
            gender (str): The gender.
        Returns:
            bool: The product of function.
        """
        if not PeselValidator.validate_format(pesel):
            return False
        if not PeselValidator.validate_check_digit(pesel):
            return False
        if not PeselValidator.validate_birth_date(pesel,date_birth):
            return False
        if not PeselValidator.get_gender(pesel) == gender:
            return False

        return True