class AnyFootballTeam:
    teamGoal = 0
    playerOnTheField = 0

    def __init__(self, name):
        self.name = name
        self.playergoal = 0
        type(self).playerOnTheField += 1

    def goal(self):
        self.playergoal += 1
        type(self).teamGoal += 1

    def MatchDetails(self):
        print(f"Total player playing {type(self).playerOnTheField}")
        print(f"{self.name} gave {self.playergoal} goal")
        print(f"Total goal so far {type(self).teamGoal}")
    
p1 = AnyFootballTeam("XYZ")
p1.goal()
p1.MatchDetails()
print("=================")

p2 = AnyFootballTeam("Messi")
p2.goal()
p2.MatchDetails()
print("=================")
p3 = AnyFootballTeam("Neymar")
p3.goal()
p3.MatchDetails()
print("=================")

p1.goal()
p2.MatchDetails()
