class Track:
    def __init__(self, artist: str, title: str, duration: str):
        self.artist = artist
        self.title = title
        self.duration = duration

    def __repr__(self):
        return repr(f'{self.artist} - {self.title} {self.duration}')


artist_1 = Track("Queen", "Killer Queen (Sheer Heart Attack)", "3:11")
print(artist_1)



# 1. Создай класс track, у которого есть поля artist, title, duration.
# Релизуй метод _ _ repr_ _ который выводит информацию типа Queen – Killer Queen
# (Sheer Heart Attack) 3:11,
# тип полей на твое усмотрение