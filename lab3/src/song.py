class Song:
    def __init__(self, title, duration):
        if   duration < 0:
            raise ValueError("duration can't be negative ")

        if duration == 0:
            pass
        elif not int(duration):
            raise ValueError("duration must be int")

        if not str(title) or title == "":
            raise ValueError("wrong input")

        self.title = title
        self.duration = duration
        self.artists = []

    def calculate_royalty(self):
        return float(self.duration)*0.01

    def add_artist(self,artist):
        if artist == "" :
            raise ValueError("Artist name cannot be empty")

        if not str(artist):
            raise ValueError("Artist must be string")

        self.artists.append(artist)