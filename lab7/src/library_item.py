from src import status

class LibraryItem:
    def __init__(self):
        self.charge = 0
        self.last_borrowed = 0
        self.status = status.AVAILABLE
        self.days = 0

    def rental_days(self, day):
        if self.status == "BORROWED":
            if day >= 0:
                self.days = day
            else:
                raise ValueError
        else:
            raise ValueError

    def changeStatus(self, new_status):
        

