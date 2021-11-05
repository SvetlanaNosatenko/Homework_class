class Track:
    def __init__(self, artist, title, duration):
        self.artist = artist
        self.title = title
        self.duration = duration
        self.sec = round(duration/60, 2)


rez = []


def get_sum_tracks():
    for track in track_list:
        rez.append(track.sec)
    return f'Суммарное время всех треков: {sum(rez)} мин'


track_list = [Track("Queen", "Killer Queen (Sheer Heart Attack)", 191),
              Track("Queen", "Tenement funster", 185), Track("Queen", "Flick of the wrist", 190)]


print(get_sum_tracks())


# 4. Используй класс track из первого занятия, но доработай его так чтобы длительность хранилась
# в секундах.
# Создай несколько треков в списке track.
# Посчитай суммарную длительность треков в минутах и выведи ее.
