class Netflix:
    shows = []
    def __init__(self, showName, genre, episode = 10):
        self.showName = showName
        self.genre = genre
        self.episode = episode
        type(self).shows.append(self.showName)
    def __str__(self):
        return f"Show name: {self.showName}\nEpisodes: {self.episode}\nGenre: {', '.join(self.genre)}"
    @classmethod
    def printDetails(cls):
        print(f"Total number of shows: {len(cls.shows)}")
        for show in cls.shows:
            print(show)

#Driver Code
print("==========1==========")
s1= Netflix("Wednesday",["Mystery","Supernatural"],15)
print(s1)
print("==========2==========")
s2= Netflix("Dark",["Mind-Bending","Sci-fi"])
print(s2)
print("==========3==========")
Netflix.printDetails()
print("==========4==========")
s3= Netflix("Suits",["Comedy","Courtroom"],20)
print(s3)
print("==========5==========")
s4= Netflix("Demon Slayer",["Anime"],22)
print(s4)
print("==========6==========")
Netflix.printDetails()