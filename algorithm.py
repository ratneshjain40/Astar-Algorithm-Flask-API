from math import sqrt
class Astar:

    class Node:
        def __init__(self,i,j):
            self.previous = None
            self.i = i
            self.j = j
            self.f = 0
            self.g = 0
            self.h = 0
            self.closed = False
            self.isWall = False

    class PathFinding:

        def __init__(self,gird_size,startPos,endPos,wall_list):

            self.gird_size = gird_size
            self.startPos = startPos
            self.endPos = endPos
            self.wall_list = wall_list

            self.openSet = []
            self.path = []
            self.visited = []
            self.grid = []
            self.useDiagnols = True
            self.hValueWeight = 2

            for i in range(self.gird_size[0]):
                self.grid.append([])
                for j in range(self.gird_size[1]):
                    self.grid[i].append(0)
                    self.grid[i][j] = Astar.Node(i,j)
                    if [i,j] in self.wall_list:
                        self.grid[i][j].isWall = True

            self.openSet.append(self.grid[self.startPos[0]][self.startPos[1]])
            

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
            if self.useDiagnols:
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
            if not(0 <= j < self.gird_size[1] and 0 <= i < self.gird_size[0]):
                return False
            if self.grid[i][j].closed:
                return False
            if self.grid[i][j].isWall:
                return False
            return True

        def add_to_openset(self,node):
            for i in range(len(self.openSet)):
                if node.f <= self.openSet[i].f :
                    self.openSet.insert(i,node)
                    break
            else:
                self.openSet.append(node)

        def nextNode(self):
            minNode = self.openSet[0]
            minNode.closed = True
            self.openSet.remove(minNode)
            return minNode

        def setHeuristic(self,node):
            i = node.i
            j = node.j
            x,y = self.endPos 
            node.h = (abs(x - i)+abs(y - j))*self.hValueWeight
        
        def run(self):
            while bool(self.openSet):
                currentNode = self.nextNode()
                if [currentNode.i,currentNode.j] == self.endPos:
                    while currentNode.previous:
                        currentNode = currentNode.previous
                        self.path.append((currentNode.i,currentNode.j))
                    break
                
                neighborPosAndTypeList = self.findneighborNodes(currentNode)
                temp_visited = []
                for neighbour in neighborPosAndTypeList:
                    neighbourPos,neighbourType = neighbour
                    i,j = neighbourPos
                    neighbour = self.grid[i][j]
                    if neighbourType == 'A':
                        tempValue = currentNode.g + 1
                    if neighbourType == 'D':
                        tempValue = currentNode.g + 1.4
                    if neighbour in self.openSet:
                        if tempValue < neighbour.g:
                            neighbour.g = tempValue
                            neighbour.f = neighbour.g + neighbour.h
                            neighbour.previous = currentNode
                    else:
                        neighbour.previous = currentNode
                        neighbour.g = tempValue
                        self.setHeuristic(neighbour)
                        neighbour.f = neighbour.g + neighbour.h
                        temp_visited.append([neighbour.i,neighbour.j])
                        self.add_to_openset(neighbour)

                if(len(temp_visited) != 0): self.visited.append(temp_visited)
                
            return self.path,self.visited