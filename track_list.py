class Album:
    def __init__(self, artist, tracks):
        self.artist = artist
        self.tracks = tracks

    def get_title(self):
        id = 0
        print(f'{self.artist}:')
        for track in self.tracks:
            id += 1
            print(f'{id} {track}')


track_list = Album("Queen",
    ['Brighton rock', 'Killer Queen', 'Tenement funster', 'Flick of the wrist', 'Lily of the valley', "Now I'm here",
     "In the lap of the Gods", "Stone cold crazy", "Dear friends", "Misfire", "Bring back that Leroy Brown",
     "She makes me (stormtrooper in stilettos)", "In the lap of the Gods... revisited"])

track_list.get_title()



# 2. Создай класс Album у которого есть поля title artist tracks. tracks -
# это список названий треков. Реализуй у него метод get_title который возвращает title
# и get_tracklist который выводит песни (каждую на новой строке), например так
# 1 Brighton rock
# 2 Killer Queen
# 3 Tenement funster
# 4 Flick of the wrist
# 5 Lily of the valley
# 6 Now I'm here
# 7 In the lap of the Gods
# 8 Stone cold crazy
# 9 Dear friends
# 10 Misfire
# 11 Bring back that Leroy Brown
# 12 She makes me (stormtrooper in stilettos)
# 13 In the lap of the Gods... revisited
