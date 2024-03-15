from functools import reduce

#-----------------------------------------------------------------# Problem 1

#partA: converts a nested sprint log structure into a task-centric dictionary
def sprintLog(sprnt):
    result = {}
    for developer, tasks in sprnt.items():
        for task, hours in tasks.items():
            if task not in result:
                result[task] = {}
            result[task][developer] = hours
    return result

#partB: combines two sprint logs by summing
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

#partC:aggergates >1 sprin logs into a single log 
def addNLogs(logList):
    return reduce(addSprints, map(sprintLog, logList))
#-----------------------------------------------------------------# Problem 2

#partA: seaches dict in revers order and returns value 
def lookupVal(L, k):
    for d in reversed(L):
        if k in d:
            return d[k]
    return None

#partB: searches a list of tuples each containig index and dict, and returns value
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
#takes list of tuples and returns three list containt elemetn ofr 1st, 2nd, 3rd position
def unzip(L):
    return (
    list(map(lambda x: x[0], L)),
    list(map(lambda x: x[1], L)),
    list(map(lambda x: x[2], L))
    )
#-----------------------------------------------------------------# Problem 4
def numPaths(m, n, blocks):
    # Create a helper function to do the recursive calculation
    def countPaths(row, col):
        if row == m and col == n:
            return 1
        
        if row > m or col > n or (row, col) in blocks:
            return 0

        # Recursive case: move right and down and sum the paths from there  
        return countPaths(row+1, col) + countPaths(row, col+1)

    # Start the recursive calculation from the origin (1, 1)
    return countPaths(1, 1)

#-----------------------------------------------------------------# Problem 5

#partA: goes through file, returns one word at a time from each line
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
            
 
#partB: tells how many of that word appeard one time  
def wordHistogram(words):
    histogram = {}
    for word in words:
        histogram[word] = histogram.get(word, 0) + 1
    return list(histogram.items())
