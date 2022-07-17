import collections
from typing import List
from copy import deepcopy
import sys


startArr=[
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]
testArr=[
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
AnsArr=[
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]
errorArr=[
    [5,3,4,6,7,8,9,1,5],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]

def printArray(Array:list,debug):
    for line in Array:
        print(line)
    if debug !=0:
        print(debug)
        print('\n')

#Checking Array
def stripZeros(line: list) -> list:
    for i in range(0,line.count(0)):
        line.remove(0)

    return line

def checkDuplicates(line: list) -> int:
    Checkset=set()
    CountError=int()
    lineproxy=line.copy()
    lineproxy=stripZeros(lineproxy)
    for num in lineproxy:
        if num in Checkset:
            CountError+=1
        else:
            Checkset.add(num)
    return CountError
            
def ErrorCount(ArrayTest: List) -> int:
    countError=int()

    #horizontal test
    for line in ArrayTest:
        countError+=checkDuplicates(line)

    #vertical test
    i=0
    while i<9:
        column=[]
        for line in ArrayTest:
            column.append(line[i])
        
        countError+=checkDuplicates(column)
        i+=1
    
    #Box Test
    i=0
    j=0
    ii=0
    while ii<9:
        cell=[]

        #Build the cell
        #choose row x3
        for y in range(j,j+3):

            #choose column x3
            for x in range(i,i+3):

                #grab unit
                cell.append(ArrayTest[y][x])
            
        countError+=checkDuplicates(cell)

        #select next cell
        ii+=1
        i+=3
        if ii%3==0:
            j+=3
            i=0



    return countError

#Solving Algorithm (backtracking) (p=problem, c=Guess)

def reject(Guess: list,debug:list) -> bool:
    return (ErrorCount(Guess)!=0)

def accept(Guess: list,debug:list) -> bool:
    for line in Guess:
        if 0 in line: return False
    if ErrorCount(Guess)!=0: return False
    return True

def firstGuess(guess: list,debug:list):
    x=int()
    nextGuess=deepcopy(guess)
    for lineNum in range(0,9):
        try:
            x=guess[lineNum].index(0)
            break
        except:
            continue
    nextGuess[lineNum][x]+=1
    index=[x,lineNum]
    return nextGuess,index

def nextGuess(guess:list,currentPos:list,debug:list):
    nextGuess=deepcopy(guess)
    if nextGuess[currentPos[1]][currentPos[0]]<9:
        nextGuess[currentPos[1]][currentPos[0]]+=1
    else:
        return
    return nextGuess

def outPut(Problem: list, Guess: list,debug=0):
    printArray(Problem,debug)
    print('\n')
    printArray(Guess,debug)
    return True
    

def backTrack(guess:list,debug=0):
    #currentGuess=deepcopy(guess)
    if debug:
        debug+=1
    
    if reject(guess,debug): return
    if accept(guess,debug): return outPut(startArr,guess) #this prints out the global, not the base case we start with
    if debug>=46:
        printArray(guess,debug)
    s,index = firstGuess(guess,debug)
    while s is not None:
        exit=backTrack(s,debug)
        if exit: return True
        s = nextGuess(s,index,debug)
        
def main():
    debug=0
    backTrack(testArr,debug)
    
if __name__=="__main__":
    main()
