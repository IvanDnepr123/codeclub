import random

commands = ["Shahtar", "Dynamo Kyev", "Dnipro-1", "Zorya", "Aleksandria", "Kryvbass", "Kolos K", "Vorskla", "Ingulets",
            "Mettalist 1925", "Chernomorets", "Veres", "Minay", "Ruch", "Metallits Kharkiv", "Lvov"]

favorite_team = input("Введіть назву своєї улюбленої команди: ")

results = {}

for team1 in commands:
    for team2 in commands:
        if team1 != team2:
            if (team2, team1) in results:
                score = results[(team2, team1)]
            else:
                score = random.randint(0, 5), random.randint(0, 5)
                results[(team1, team2)] = score

points = [0] * len(commands)

print("Результати матчів:")
for (team1, team2), (score1, score2) in results.items():
    print(f"{team1} {score1} : {score2} {team2}")
    if score1 > score2:
        points[commands.index(team1)] += 3
        if team1 == favorite_team:
            print("Ти виграв!")
        elif team2 == favorite_team:
            print("Ти програв(")
    elif score2 > score1:
        points[commands.index(team2)] += 3
        if team2 == favorite_team:
            print("Ти виграв!")
        elif team1 == favorite_team:
            print("Ти програв(")
    else:
        points[commands.index(team1)] += 1
        points[commands.index(team2)] += 1

table = sorted(list(zip(commands, points)), key=lambda x: x[1], reverse=True)

print("Турнірна таблиця:")
for i, (team, point) in enumerate(table):
    print(f"{i+1}. {team} - {point} очок")

