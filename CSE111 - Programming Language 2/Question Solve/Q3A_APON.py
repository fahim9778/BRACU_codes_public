# Public URL (for your students): https://codecheck.io/files/2212150557argma1syqznqkm894fbdewd0g
# Edit URL (for you only): https://codecheck.io/private/problem/2212150557argma1syqznqkm894fbdewd0g/BUTVNG88NS45B9Q8R2C2ERIW8
class Match:
    __ID = 0
    __matchDetails = {}
    __teamListSet = set() 

    def __init__(self, team1_name, team2_name, team1_goals=0, team2_goals=0):
        self.__team1_name = team1_name
        self.__team2_name = team2_name
        self.__team1_goals = team1_goals
        self.__team2_goals = team2_goals

        type(self).__ID += 1
        self.__id = type(self).__ID 

        type(self).__teamListSet.update([team1_name, team2_name])
        
        # crate a dictionary with key as ID and value as a string with team1_name, team2_name, team1_goals, team2_goals
        type(self).__matchDetails[type(self).__ID] = f"{self.__team1_name} ({self.__team1_goals}) :  {self.__team2_name} ({self.__team2_goals})"

    @classmethod
    def printDetailsfromID(cls, match_id):
        if match_id in cls.__matchDetails.keys():
            print(cls.__matchDetails[match_id])

    @classmethod
    def printTeamList(cls):
        teamList= sorted(list(cls.__teamListSet))
        print(*teamList, sep=", ") # using * to unpack the list

    def __gt__(self, other):
        return (self.__team1_goals + self.__team2_goals) > (other.__team1_goals + other.__team2_goals)

    def __lt__(self, other):
        return (self.__team1_goals + self.__team2_goals) < (other.__team1_goals + other.__team2_goals)

    def __eq__(self, other):
        return (self.__team1_goals + self.__team2_goals) == (other.__team1_goals + other.__team2_goals)

    def getID(self):
        return self.__id

    def getGoals(self):
        return (self.__team1_goals, self.__team2_goals)

    # WRITE A CLASS METHOD CALLED isTie() that can handle below call
    # Match.isTie(*m3.getGoals())
    @classmethod
    def isTie(cls, team1_goals, team2_goals):
        return team1_goals == team2_goals



m1 = Match("USA", "Wales", 1 ,1)
m2 = Match("Wales", "Iran", 0, 2)
Match.printTeamList() # prints sorted list of team names
print("=====================================")
m3 = Match("England", "USA")
m4 = Match("USA", "Iran", 1)
print(m1 > m2)
print(m2 == m1)
print(m1.getID())
Match.printDetailsfromID(3)
print("=====================================")
print(m3 < m4)
print(m4 == m3)
print(m2.getGoals())
print("=====================================")
print(Match.isTie(*m3.getGoals()))
print(Match.isTie(*m4.getGoals()))
Match.printTeamList() # prints sorted list of team names
print("=====================================")