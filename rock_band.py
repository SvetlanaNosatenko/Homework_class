class Artist:
    def __init__(self, title, genre, singer, drummer, bass_player, guitar_player):
        self.title = title
        self.genre = genre
        self.singer = singer
        self.drummer = drummer
        self.bass_player = bass_player
        self.guitar_player = guitar_player


class RockBand(Artist):
    def print_band(self):
        print(f'{self.title}:\nsinger - {self.singer}, drummer - {self.drummer}, bass_player - {self.bass_player},'
              f'guitar_player - {self.guitar_player}\n')


bands = ([RockBand("Iron Maiden", "rock", "Paul Bruce Dickinson", "Michael Henry McBrain", "Stephen Percy Harris", "David Michael Murray"),
                 RockBand("The Rolling Stones", "rock", "Michael Philip Jagger", "Charles Robert Watts", "Ronald David Wood", "Keith Richards")])

for band in bands:
    band.print_band()


# 5. Наследуй класс RockBand от artist и перепиши _ _ init _ _
# так чтобы поля были title genre singer drummer bass_player guitar_player.
# Положи несколько экземпляров класса в список bands. \
# Выведи список групп в формате title: singer drummer  bass_player guitar_player