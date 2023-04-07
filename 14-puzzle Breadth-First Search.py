from copy import deepcopy


class Node: # node class
    graf=[]
    parent=None




def GrafSearch(): #the main function to search the nodes and check them
    mainInit=None
    while True:
        if frontier==[]:
            break
        
        mainInit=frontier[0]
        tempGraf=mainInit.graf
        del frontier[0]
        
        if tempGraf==goal:
            break
        
        explored.append(tempGraf)
        
        AddToFrontier(mainInit)
    

    moves=0
    while mainInit.parent!=None:
        for i in range(4):
            print(mainInit.graf[i][:])
        print("--------------------------------------------------------------")
        mainInit=mainInit.parent
        moves=moves+1
    print("first base:")
    for i in range(4):
            print(mainInit.graf[i][:])
            
    print("explored: " , len(explored))
    print("frontier: " , len(frontier))
    print("Moves: ", moves)


def AddToFrontier(node): #creates new matrises and put them in frontier
    tempGrid=node.graf
    location=FindSpace(tempGrid)
    k=0
    while k<len(location):
        i= -1
        while i<2:
            j=-1
            tempi=i+location[k][0]
            while j<2:
                tempj=j+location[k][1]
                if ((j!=0 or i!=0) and (tempi>=0 and tempi<len(tempGrid)) 
                    and (tempj>=0 and tempj<len(tempGrid)) 
                    and (tempGrid[tempi][tempj]!=0) and (i+j==-1 or i+j==1)):
                    newGrid=deepcopy(tempGrid)
                    newGrid[location[k][0]][location[k][1]], newGrid[tempi][tempj]= newGrid[tempi][tempj], newGrid[location[k][0]][location[k][1]]

                    checker= newGrid in explored
                    
                    if checker==False:
                        for search in frontier:
                            if(search.graf==newGrid):
                                checker=True
                                break   

                    if(checker==False):
                        newNode=Node()
                        newNode.parent=node
                        newNode.graf=newGrid
                        frontier.append(newNode)
                j=j+1
            i=i+1
        k=k+1






def FindSpace(graf): # finds the two empty spaces in matrix
    x=[]
    for i in range(4):
        for j in range(4):
            if(graf[i][j]==0):
                x.append([i, j])
                if(len(x)==2):
                    return x



goal=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 0]]

intitial =[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 12], [13, 11, 0, 14]]

#[[0,1,0,2],[3,4,5,6],[7,8,9,10],[11,12,13,14]]
#[[1, 2, 3, 4], [5, 0, 6, 7], [8, 9, 0, 10], [11, 12, 13, 14]]

frontier=[]
explored=[]

init=Node()
init.graf=intitial
frontier.append(init)
GrafSearch()
