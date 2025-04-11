from src import status

class LibraryItem:
    def __init__(self):
        self.charge = 0
        self.last_borrowed = 0
        self.status = status.AVAILABLE
        self.days = 0

    def rental_days(self, int days):
        if self.status == "BORROWED":
            if days >= 0:
                self.days = days
            else:
                raise ValueError
        else:
            raise ValueError

    def change status(self, Status new_status):

