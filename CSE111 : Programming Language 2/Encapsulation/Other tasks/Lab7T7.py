"""Given the following classes, write the code for the Player and the Manager class so that the following output is printed. To calculate the match earning use the following formula:
Player: (total_goal * 1000) + (total_match * 10)
Manager: match_win * 1000
"""

class Football:

  def __init__(self, team_name, name, role):
    self.__team = team_name
    self.__name = name
    self.role = role
    self.earning_per_match = 0

  def get_name_team(self):
    return 'Name: '+self.__name+', Team Name: ' +self.__team

class Player(Football):
  def __init__(self, team_name, name, role, total_goal, total_match):
    super().__init__(team_name, name, role)
    self.total_goal = total_goal
    self.total_match = total_match
    self.earning_per_match = (self.total_goal * 1000) + (self.total_match * 10)
    self.role = role

  def calculate_ratio(self):
    return self.total_goal / self.total_match

  def print_details(self):
    print(self.get_name_team())
    print(f'Team Role: {self.role}')
    print(f'Total Goal: {self.total_goal}, Total Played: {self.total_match}')
    print(f'Ratio: {(self.calculate_ratio())}')
    print(f'Match Earning: {self.earning_per_match}K')

class Manager(Football):
    def __init__(self, team_name, name, role, match_win):
        super().__init__(team_name, name, role)
        self.match_win = match_win
        self.earning_per_match = match_win * 1000
        self.role = role
    
    def print_details(self):
        print(self.get_name_team())
        print(f'Team Role: {self.role}')
        print(f'Match Win: {self.match_win}')
        print(f'Match Earning: {self.earning_per_match}K')

#write your code here

player_one = Player('Juventus', 'Ronaldo', 'Striker', 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print('------------------------------------------')
manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
manager_one.print_details()
    