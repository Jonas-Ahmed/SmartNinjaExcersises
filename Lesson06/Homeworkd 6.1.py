
class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

messi = FootballPlayer(first_name="Lionel", last_name="Messi", height_cm=170, weight_kg=67, goals=575, yellow_cards=67, red_cards=0)
kev_dur = BasketballPlayer(first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, points=27.2, rebounds=7.1, assists=4)
lebron = BasketballPlayer(first_name="Lebron", last_name="James", height_cm=203, weight_kg=113, points=27.2, rebounds=7.4, assists=7.2)
giannis = BasketballPlayer(first_name="Giannis", last_name="Antetokounmpo", height_cm=211, weight_kg=110, points=30.2, rebounds=12.8, assists=5.1)


#print(giannis.last_name)
#print(giannis.rebounds)
#print(giannis.weight_to_lbs())

print("Please type in player details")
name_first = input("Player's first name? ")
name_last = input("Player's last name? ")
height = input("Player's height? ")
weight = input("Player's weight in kg? ")

foot_or_basket = input("Would you like to create a new Basketballplayer or Footballplayer. Please type F or B ")
if foot_or_basket.upper == "F":
    goal = input("How many goals? ")
    yellow = input("How many yellow cards? ")
    red = input("How many red cards? ")
else:
    point = input("How many points? ")
    rebound = input("How many rebounds? ")
    assists = input("How many assists? ")

if foot_or_basket == "F":
    new_player = FootballPlayer(first_name=name_first, last_name=name_last, height_cm=height, weight_kg=weight, goals=goal, yellow_cards=yellow, red_cards=red)
else:
    new_player = BasketballPlayer(first_name=name_first, last_name=name_last, height_cm=height, weight_kg=weight, points=point, rebounds=rebound, assists=assists)

#print(new_player.first_name) var blot til test

with open("player.txt", "w") as player_file:
    player_file.write(str(new_player.__dict__))


print("Result from file")
with open("player.txt", "r") as player_file:
    result = player_file.read()
    print(result)



