class Director:
    def __init__(self, *names):
        if len(names) == 0:
            print(f"Specify at least one name")
            return None
        self.name = names[0]
        self.movies = []
        if len(names) > 1:
            self.movies = list(names[1:])

    def addMovies(self, *movieNames):
        # for movie in movieNames:
        #     self.movies.append(movie)
        self.movies.extend(movieNames)

    def renameMovie(self, oldName, newName):
        for i in range(len(self.movies)):
            if self.movies[i] == oldName:
                self.movies[i] = newName
                print(f"Movie renamed")
                return True
        print(f"Movie not found")
    
    def printDetails(self):
        print(f"Director {self.name} has directed {len(self.movies)} movies")
        for movie in self.movies:
            print(f"\t{movie}")
    

dir1 = Director('Christopher Nolan')
dir1.addMovies('Inception', 'The Dark Knight')
dir1.printDetails()
print("===================")
dir2 = Director('Alfred Hitchcock', 'Psycho', 'Rear Window', 'Vertigo')
dir2.renameMovie('Vertigo', 'Vertigo 2')
dir2.printDetails()
print("===================")
dir3 = Director('Steven Spielberg','The Color Purple')
dir3.renameMovie('The Alchemist', 'The Last Days')
dir3.addMovies('The Color Purple')
dir3.printDetails()
print("===================")
    
    
