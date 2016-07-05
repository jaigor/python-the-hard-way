class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

du_hast = ["du",
		   "du hast",
		   "du hast mich"]
Song(du_hast).sing_me_a_song()

trooper = ["You'll take my life but I'll take yours too",
			"You'll fire your musket but I'll run you through",
			"So when you're waiting for the next attack",
			"You'd better stand there's no turning back."]


class Metal(Song):
	def __init__(self, group):
		self.group = group

	def assign_songs(self):
		if self.group == "Rammstein":
			song = "Du Hast"
			lyrics = Song(du_hast)
		elif self.group == "Iron Maiden":
			song = "Trooper"
			lyrics = Song(trooper)
		print song
		lyrics.sing_me_a_song()

print "Grupo a elegir en la siguiente cancion?"
song_to_print = Metal(raw_input('> '))

song_to_print.assign_songs()