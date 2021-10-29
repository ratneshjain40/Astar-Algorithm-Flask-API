## To IMPROVE:
## Can use priority queue for openSet
## Use this algorithm in backend and make a web based version of UI
from math import sqrt

class Maze:
    @staticmethod
    def makeMaze():
        maze = []
        maze.append(["O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "])
        maze.append([" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "])
        maze.append([" "," ",""," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "])
        maze.append([" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "])
        maze.append([" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "])
        maze.append([" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","X"," "])
        maze.append([" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "])
        maze.append([" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "])
        maze.append([" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "])
        maze.append([" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "])
        maze.append([" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "])
        maze.append([" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "])
        maze.append([" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "])
        maze.append([" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "])
        maze.append([" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "])
        maze.append([" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "])
        maze.append([" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "])
        maze.append([" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "])
        maze.append([" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "])
        maze.append([" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "])
        maze.append([" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",""," "," "," "," "])
        return maze
    @staticmethod
    def findPos(maze):
        for i,row in enumerate(maze):
            for j,col in enumerate(row):
                if maze[i][j] == 'O':
                    startPos = (i,j)
                if maze[i][j] == 'X':
                    endPos = (i,j)
                    break
        return startPos,endPos

    @staticmethod
    def printMaze(maze,path):
        path.remove(startPos)
        for i,row in enumerate(maze):
            for j,col in enumerate(row):
                if (i,j) in path:
                    print("+"," ",end="")
                else:
                    print(col," ",end="")
            print()

class Node:
    def __init__(self,i,j):
        self.previous = None
        self.i = i
        self.j = j
        self.f = 0
        self.g = 0
        self.h = 0
        self.closed = False

class PathFinding:
    def __init__(self):
        i,j = startPos
        openSet.append(grid[i][j])

    def findneighborNodes(self,node):
        i,j = node.i,node.j

        U = (i-1,j)
        R = (i,j+1)
        D = (i+1,j)
        L = (i,j-1)
        neighbourList = []
        if self.isValid(U):
            neighbourList.append((U,"A"))
        if self.isValid(R):
            neighbourList.append((R,"A"))
        if self.isValid(D):
            neighbourList.append((D,"A"))
        if self.isValid(L):
            neighbourList.append((L,"A"))
        if useDiagnols:
            LU = (i-1,j-1)
            LD = (i+1,j-1)
            RU = (i-1,j+1)
            RD = (i+1,j+1)
            if self.isValid(LU):
                neighbourList.append((LU,"D"))
            if self.isValid(RU):
                neighbourList.append((RU,"D"))
            if self.isValid(LD):
                neighbourList.append((LD,"D"))
            if self.isValid(RD):
                neighbourList.append((RD,"D"))

        return neighbourList
    
    def isValid(self,point):
        i,j = point
        if not(0 <= j < len(maze[0]) and 0 <= i < len(maze)):
            return False
        if grid[i][j].closed:
            return False
        if maze[i][j]=="#":
            return False
        return True

    def nextNode(self):
        minNode = openSet[0]
        for node in openSet:
            if node.f < minNode.f:
                minNode = node

        minNode.closed = True
        openSet.remove(minNode)
        return minNode

    def setHeuristic(self,node):
        i = node.i
        j = node.j
        x,y = endPos 
        ## two formuals can be used:
        ##1.(sqrt((x - i)**2 + (y - j)**2))
        ##2. 
        node.h = (abs(x - i)+abs(y - j))*hValueWeight

## <---------------------------------------   Grid   ------------------------------------>
## Making A Maze, and making each element in that maze, an object of Node, Node objects have diffrent properties
## make seperate matrix corresponding to maze, to store objects of Node, HERE it is called grid
maze = Maze.makeMaze()
startPos,endPos = Maze.findPos(maze)
grid = []
for i,row in enumerate(maze):
    grid.append([])
    for j,col in enumerate(row):
        grid[i].append(0)
        grid[i][j] = Node(i,j)
## <---------------------------------------   Initializing lists   ------------------------------------>
## OpenSet Stores all the computed neighbors Nodes (From grid)
## A Node of least value will be picked from openSet and put in the loop to find neighbors or the endPoint
openSet = []
path = []
Astar = PathFinding()
## <---------------------------------------   Change Variables   ------------------------------------>
Heuristic = True
useDiagnols = True
hValueWeight = 1
## <---------------------------------------   Main Loop   ------------------------------------>
while bool(openSet):
    currentNode = Astar.nextNode()
    #if End Pos is Reached and Trace Path.
    if (currentNode.i,currentNode.j) == endPos:
        while currentNode.previous:
            currentNode = currentNode.previous
            path.append((currentNode.i,currentNode.j))
        break
    
    neighborPosAndTypeList = Astar.findneighborNodes(currentNode)
    for neighbour in neighborPosAndTypeList:
        # Unpack The neighbour and get position and type
        # convert neighbour varibale into a Node.
        neighbourPos,neighbourType = neighbour
        i,j = neighbourPos
        neighbour = grid[i][j]
        # "A" - Adjacent
        # "D" - Diagonal
        if neighbourType == 'A':
            tempValue = currentNode.g + 1
        if neighbourType == 'D':
            tempValue = currentNode.g + 1.4
        # if neighbour node already exists in openSet update its values
        if neighbour in openSet:
            if tempValue < neighbour.g:
                neighbour.g = tempValue
                neighbour.f = neighbour.g + neighbour.h
                neighbour.previous = currentNode
        else:
            # set parent node of neighbour to previous node
            # set f = g + h scores
            # if Heuristic is TRUE the it is A* algorithm, otherwise its just dijsktras algorithm
            neighbour.previous = currentNode
            neighbour.g = tempValue
            if Heuristic:
                Astar.setHeuristic(neighbour)
            neighbour.f = neighbour.g + neighbour.h
            openSet.append(neighbour)

Maze.printMaze(maze,path)
print(startPos,endPos)
print(path)