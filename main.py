import urllib.request
import json

with urllib.request.urlopen("https://dowsy.github.io/FPLMiniLeague/data_file.json") as u:
    data = u.read()
    data = json.loads(data)

gameWeeks = []
for i in range (1,39):
    gameWeeks.append(str(i))
playerList = ['91225', '91449', '92236', '92611', '105045', '1164477', '1505241']
visual = []

playerTotalpts = ['Overall Points']
for j in playerList:
    totalpts = []
    for i in gameWeeks:
        totalpts.append(data[i][j]['game week points'])
    summation = sum(totalpts)
    playerTotalpts.append(summation)

playerBenchpts = ["Points left on bench"]
for j in playerList:
    totalpts = []
    for i in gameWeeks:
        totalpts.append(data[i][j]['points left on bench'])
    summation = sum(totalpts)
    playerBenchpts.append(summation)

playerDFpts = ["Points scored by defense"]
for j in playerList:
    totalpts = []
    for i in gameWeeks:
        totalpts.append(data[i][j]['points by defense'])
    summation = sum(totalpts)
    playerDFpts.append(summation)

playerMFpts = ["Points scored by midfielders"]
for j in playerList:
    totalpts = []
    for i in gameWeeks:
        totalpts.append(data[i][j]['points by midfield'])
    summation = sum(totalpts)
    playerMFpts.append(summation)

playerFWpts = ["Points scored by forwards"]
for j in playerList:
    totalpts = []
    for i in gameWeeks:
        totalpts.append(data[i][j]['points by forwards'])
    summation = sum(totalpts)
    playerFWpts.append(summation)

playerCappts = ["Points scored by captain (x1)"]
for j in playerList:
    totalpts = []
    for i in gameWeeks:
        totalpts.append(data[i][j]['points by captain'])
    summation = sum(totalpts)
    playerCappts.append(summation)

title = ["FPL",'TT Chan', 'shing chow', 'Jeffrey Wong', 'CHAN JOHN', 'Adrian Lam', 'James Chan', 'Jeffrey Kong']
visual.append(title)
visual.append(playerTotalpts)
visual.append(playerBenchpts)
visual.append(playerDFpts)
visual.append(playerMFpts)
visual.append(playerFWpts)
visual.append(playerCappts)
matr = [title, playerTotalpts, playerBenchpts, playerDFpts, playerMFpts, playerFWpts, playerCappts]

visualb = []

for i in range(0,len(title)):
    lista = []
    for j in range (0,len(matr)):
        lista.append(visual[j][i])
    visualb.append(lista)

finalvisual = [visualb]
print(finalvisual)

with open("data_file.json", "w") as write_file:
    json.dump(finalvisual, write_file)

