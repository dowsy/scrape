import urllib.request
import json

with urllib.request.urlopen("https://dowsy.github.io/FPLMiniLeague/data_file.json") as u:
    data = u.read()
    data = json.loads(data)

currGW = 38

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

title = ["Main Scores",'TT Chan', 'shing chow', 'Jeffrey Wong', 'CHAN JOHN', 'Adrian Lam', 'James Chan', 'Jeffrey Kong']
matr = [title, playerTotalpts, playerBenchpts, playerDFpts, playerMFpts, playerFWpts, playerCappts]
for i in matr:
    visual.append(i)

mainvisual = []

for i in range(0,len(title)):
    lista = []
    for j in range (0,len(matr)):
        lista.append(visual[j][i])
    mainvisual.append(lista)

print(mainvisual)

monthHeader = ['Manager of the Month']
months = ['August', 'September', 'October', 'November', 'December', 'January', 'February', 'March', 'April', 'May']
monthLimit = [0, 4, 7, 10, 14, 20, 24, 28, 31, 35, 38]
for i in range(0, len(months)):
    if (currGW > monthLimit[i]) and (currGW <= monthLimit[i+1]):
        currMonth = months[i]
        monthIndex = i
        for j in range(0,i+1):
            monthHeader.append(months[j])

monthVisual = [monthHeader]

for i in playerList:
    monthPoints = [i]
    for j in range(0,monthIndex):
        weeksOfMonth = []
        for k in range(monthLimit[j], monthLimit[j+1]):
            weeksOfMonth.append(data[gameWeeks[k]][i]['game week points'])
            ptsOfMonth = sum(weeksOfMonth)
        monthPoints.append(ptsOfMonth)
        weeksOfMonth = []
    for l in range(monthLimit[monthIndex],currGW):
        weeksOfMonth.append(data[gameWeeks[l]][i]['game week points'])
        ptsOfMonth = sum(weeksOfMonth)
    monthPoints.append(ptsOfMonth)
    monthVisual.append(monthPoints)

print(monthVisual)

cum18Header = ['2018/19']
for i in range(1,39):
    cum18Header.append(str(i))
cum1819 = [cum18Header]

for i in playerList:
    cumPoints = [i]
    for j in range(0+1,currGW+1):
        cumCal = []
        for k in range (0,j):
            cumCal.append(data[gameWeeks[k]][i]['game week points'])
        cumWeek = sum(cumCal)
        cumPoints.append(cumWeek)
    cum1819.append(cumPoints)

print(cum1819)

with open("cum_file.json", "w") as write_file:
    json.dump([cum1819], write_file)

rank1819 = cum1819[:]
rankDraft = []

for i in range(0, currGW+1):
    weekMat = []
    for j in range(1, 8):
        weekMat.append(rank1819[j][i])
    weekMat = sorted(weekMat,reverse=True)
    rankDraft.append(weekMat)

for i in range(1,8):
    for j in range(1, currGW+1):
        rank1819[i][j] = (rankDraft[j].index(rank1819[i][j]))+1

print(rank1819)

with open("data_file.json", "w") as write_file:
    json.dump([mainvisual,monthVisual], write_file)

with open("ranking_file.json", "w") as write_file:
    json.dump([rank1819], write_file)