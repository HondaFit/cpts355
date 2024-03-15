#This is just a sandbox/debugging to test out all my functions without messing with HW3.py and HW3tests.py 
#This does not reflect the final product but merely shows my thought process of how I was able to get the fucntion to work
#comments and other minor changes might not be shown refelcted here
"""
Note for this sandbox to work you need to link your HW3testfile.txt to it. So you need to set a pathway to it. Go to line #176 & #187 to change path
"""

from functools import reduce

#-----------------------------------------------------------------# Problem 1
def sprintLog(sprnt):
    result = {}
    for developer, tasks in sprnt.items():
        for task, hours in tasks.items():
            if task not in result:
                result[task] = {}
            result[task][developer] = hours
    return result

def addSprints(sprint1, sprint2):
    result = {}
    for task, developers in sprint1.items():
        result[task] = developers.copy()
    for task, developers in sprint2.items():
        if task not in result:
            result[task] = developers.copy()
        else:
            for developer, hours in developers.items():
                if developer not in result[task]:
                    result[task][developer] = hours
                else:
                    result[task][developer] += hours
    return result

def addNLogs(logList):
    return reduce(addSprints, map(sprintLog, logList))
#-----------------------------------------------------------------# Problem 2
# 2a) lookupVal(L,k)
def lookupVal(L, k):
    for d in reversed(L):
        if k in d:
            return d[k]
    return None

# 2b) lookupVal2(tL,k)
def lookupVal2(tL, k):
    def search_key(idx):
        if idx < 0:
            return None
        
        index, dictionary = tL[idx]
        
        if k in dictionary:
            return dictionary[k]
        elif index == idx:
            return None
        else:
            return search_key(index)
    
    return search_key(len(tL) - 1)

#-----------------------------------------------------------------# Problem 3
def unzip(L):
    return tuple(map(lambda i: list(map(lambda x: x[i], L)), range(len(L[0]))))
#-----------------------------------------------------------------# Problem 4
def numPaths(m, n, blocks):
    # Create a helper function to do the recursive calculation
    def countPaths(row, col):
        # Base case: if we reached the goal, return 1 for this path
        if row == m and col == n:
            return 1
        
        # Base case: if we are out of bounds or on a blocked cell, return 0
        if row > m or col > n or (row, col) in blocks:
            return 0

        # Recursive case: move right and down and sum the paths from there  
        return countPaths(row+1, col) + countPaths(row, col+1)

    # Start the recursive calculation from the origin (1, 1)
    return countPaths(1, 1)

#-----------------------------------------------------------------# Problem 5
class iterFile():
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.current_line = ""
        self.current_word_idx = 0
        self.current_words = []
        
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            if self.current_word_idx >= len(self.current_words):
                self.current_line = self.file.readline()
                if not self.current_line:
                    self.file.close()
                    raise StopIteration
                self.current_words = self.current_line.strip().split()
                self.current_word_idx = 0
            
            if self.current_word_idx < len(self.current_words):
                word = self.current_words[self.current_word_idx]
                self.current_word_idx += 1
                return word
            
            
def wordHistogram(words):
    histogram = {}
    for word in words:
        histogram[word] = histogram.get(word, 0) + 1
    return list(histogram.items())


#////////////////////////////////////////////////////////////////////# Pr1

#partB:
sprint1 = {'task1': {'John': 5, 'Rae': 10, 'Kelly': 8, 'Alex': 11}, 'task2':
{'Rae': 4, 'Alex': 2, 'Aaron': 15}, 'task3': {'Kelly': 5, 'Alex': 1,
'Ethan': 12, 'Helen': 10}}
sprint2 = {'task1': {'Mark': 5, 'Kelly': 10, 'Alex': 15}, 'task2': {'Mark': 2,
'Alex': 2, 'Rae': 10, 'Aaron': 10}, 'task4': {'Helen': 16}}
print(addSprints(sprint1,sprint2))
print()

#partC:
logList = [{'John': {'task1':5}, 'Rae': {'task1':10, 'task2':4}, 'Kelly':
{'task1':8, 'task3':5}, 'Alex': {'task1':11, 'task2':2, 'task3':1},
'Aaron': {'task2':15}, 'Ethan':{'task3':12}, 'Helen': {'task3':10}},
{'Mark': {'task1':5, 'task2':2}, 'Kelly': {'task1':10}, 'Alex': {'task1':15,
'task2':2}, 'Rae': {'task2':10}, 'Aaron': {'task2':10}, 'Helen':
{'task4':16}},
{'Alex': {'task3':10, 'task2':5, 'task4':6}, 'Rae': {'task3':5, 'task5':16},
'Mark': {'task4':20}, 'Kelly': {'task2':5, 'task3':10, 'task4':12}, 'Helen':
{'task5':10, 'task4':8}}]

print(addNLogs(logList))
print()

#////////////////////////////////////////////////////////////////////# Pr2

#partA:
L1 = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]
print(lookupVal(L1,"x"))
print(lookupVal(L1,"y"))
print(lookupVal(L1,"z"))
print(lookupVal(L1,"t"))
print()

#partB:
L2 = [(0,{"x":0,"y":True,"z":"zero"}),
 (0,{"x":1}),
 (1,{"y":False}),
 (1,{"x":3, "z":"three"}),
 (2,{})]
print(lookupVal2(L2,"x"))
print(lookupVal2(L2,"y"))
print(lookupVal2(L2,"z"))
print(lookupVal2(L2,"t"))
print()

#////////////////////////////////////////////////////////////////////# Pr3

print(unzip ([(1,"a",{1:"a"}),(2,"b",{2:"b"}),(3,"c",{3:"c"}),(4,"d",{4:"d"})]))
print()

#////////////////////////////////////////////////////////////////////# Pr4
print(numPaths(2,2,[(2,1)]))
print(numPaths(3,3,[(2,3)]))
print(numPaths(4,3,[(2,2)])) 
print(numPaths(10,3,[(2,2),(7,1)]))
print()
#////////////////////////////////////////////////////////////////////# Pr5

#partA
mywords = iterFile(r"C:\Users\Harish Sridharan\Documents\Computer Programming\cpts355\assignment3\HW3testfile.txt")
print(mywords.__next__())
print(mywords.__next__())
print(mywords.__next__())
print()

for word in mywords:
    print(word)
print()

#partB:
print(wordHistogram(iterFile(r"C:\Users\Harish Sridharan\Documents\Computer Programming\cpts355\assignment3\HW3testfile.txt")))
print()
