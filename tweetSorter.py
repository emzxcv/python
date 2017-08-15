import json
from collections import OrderedDict,defaultdict
import operator

totalGrids = 16

json_data=open('melbGrid.json').read()
data = json.loads(json_data)
#Initialise data structures
gridDict = []
for i in range (totalGrids):
    gridDict.append(data["features"][i]["properties"])

grid ={}
for i in range(totalGrids):
    grid[gridDict[i]['id']] = 0

def sortTweet(point):
    for i in range (totalGrids):
        if (point[0]>= gridDict[i]['xmin'] and point[0] <= gridDict[i]['xmax']
        and point[1]>= gridDict[i]['ymin'] and point[1] <= gridDict[i]['ymax']):
           grid[gridDict[i]['id']] += 1

def sortDesc(someGrid):
    return OrderedDict(sorted(list(someGrid.items()),key = lambda t: t[1], reverse = True))

tweets = open('./bigTwitter.json', 'r')
tweets.readline()

#pre-process line
for line in tweets:
    line = line.strip('\n')

    if line[-1:] == ',':
         line = line[0:-1]
    try:
        position = json.loads(line)
        coordinates = (position['json']['coordinates']['coordinates'])
        #sort tweet into grid dictionary
        sortTweet(coordinates)
    except Exception as e:
        continue

#sort the Order (rank) the Grid boxes based on the total number of tweets made in each box
sortedTwitterGrid = sortDesc(grid)

rows= defaultdict(int)
columns = defaultdict(int)

def tallyRowCol():
    rows[key[0]] += val
    columns[key[1]] += val

print("Order (rank) the Grid boxes based on the total number of tweets made in each box ")
for key, val in list(sortedTwitterGrid.items()):
    print("{}: {} tweets,".format(key,val))
    tallyRowCol()

#sort in descending order for the rows and columns of the grid
r = sortDesc(rows)
c = sortDesc(columns)

print("\nOrder (rank) the rows based on the total number of tweets in each row")
for key, val in list(r.items()):
    print("{}-Row: {} tweets,".format(key,val))


print("\nOrder (rank) the columns based on the total number of tweets in each column")
for key, val in list(c.items()):
    print("{}-Column: {} tweets,".format(key,val))
