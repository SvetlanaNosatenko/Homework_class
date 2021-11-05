class Artist:
    def __init__(self, artist, genre):
        self.artist = artist
        self.genre = genre

    def artists_gen(self):
        if self.genre == "rock":
            print(self.artist)


artists = [Artist("Iron Maiden", "rock"), Artist("The Rolling Stones", "rock"), Artist("A-ha", "pop")]
for artist in artists:
    artist.artists_gen()


# 3. Создай класс artist у которого есть поля title, genre.
# Создай список из artist который будет наполнен несколькими группами.
# Затем выведи в цикле только группы с жанром rock