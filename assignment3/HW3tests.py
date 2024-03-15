import unittest
from HW3 import *

class HW3tests(unittest.TestCase):

    def setUp(self):
        
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        # sprintLog inputs
        self.log1 = {'John': {'task1': 5}, 'Rae': {'task1': 10, 'task2': 4}, 'Kelly': {'task1': 8, 'task3': 5}, 'Alex': {'task1': 11, 'task2': 2, 'task3': 1}, 'Aaron': {'task2': 15}, 'Ethan':{'task3': 12}, 'Helen': {'task3': 10}}
        self.log2 = {'Mark': {'task1': 5, 'task2': 2}, 'Kelly': {'task1': 10}, 'Alex': {'task1': 15, 'task2': 2}, 'Rae': {'task2': 10}, 'Aaron': {'task2': 10}, 'Helen': {'task4': 16}}
        self.log3 = {'Aaron': {'task5': 15, 'task6': 8}, 'Rae': {'task5': 20}, 'Helen': {'task6': 16}}
        self.log4 = {'Alex': {'task6': 15}, 'Kelly': {'task5': 20}, 'Helen': {'task6': 10}}
        # addSprints inputs/outputs
        self.sprint1 = {'task1': {'John': 5, 'Rae': 10, 'Kelly': 8, 'Alex': 11}, 'task2': {'Rae': 4, 'Alex': 2, 'Aaron': 15}, 'task3': {'Kelly': 5, 'Alex': 1, 'Ethan': 12, 'Helen': 10}}
        self.sprint2 = {'task1': {'Mark': 5, 'Kelly': 10, 'Alex': 15}, 'task2': {'Mark': 2, 'Alex': 2, 'Rae': 10, 'Aaron': 10}, 'task4': {'Helen': 16}}
        self.addedSprints = {'task1': {'John': 5, 'Rae': 10, 'Kelly': 18, 'Alex': 26, 'Mark': 5}, 'task2': {'Rae': 14, 'Alex': 4, 'Aaron': 25, 'Mark': 2}, 'task3': {'Kelly': 5, 'Alex': 1, 'Ethan': 12, 'Helen': 10}, 'task4': {'Helen': 16}}
        # addNLogs input/output
        self.logList = [self.log1,self.log2,self.log3,self.log4]
        self.sprintSummary = {'task1': {'John': 5, 'Rae': 10, 'Kelly': 18, 'Alex': 26, 'Mark': 5}, 'task2': {'Rae': 14, 'Alex': 4, 'Aaron': 25, 'Mark': 2}, 'task3': {'Kelly': 5, 'Alex': 1, 'Ethan': 12, 'Helen': 10}, 'task4': {'Helen': 16}, 'task5': {'Aaron': 15, 'Rae': 20, 'Kelly': 20}, 'task6': {'Aaron': 8, 'Helen': 26, 'Alex': 15}}
        #lookupVal inputs
        self.lookupList = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]
        self.lookup2List = [(0,{"x":0,"y":True,"z":"zero"}), (0,{"x":1}), (1,{"y":False}), (1,{"x":3, "z":"three"}), (2,{})]
        # iterFile output
        self.filetokens = ["CptS","355","Assignment","3","-","Python","Warmup","This","is","a","text","test","file","for","CptS","355","-","Assignment","3","-","Python","Warmup","With","some","repeated","text","for","CptS","355","-","Assignment","3","-","Python","Warmup","."]
        self.histogram = [('-', 5), ('3', 3), ('355', 3), ('Assignment', 3), ('CptS', 3), ('Python', 3), ('Warmup', 3), ('for', 2), ('text', 2), ('.', 1), ('This', 1), ('With', 1), ('a', 1), ('file', 1), ('is', 1), ('repeated', 1), ('some', 1), ('test', 1)]

        #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        # sprintLog inputs
        self.log5 = {'Bobby': {'task1': 5}, 'Randy': {'task1': 10, 'task2': 4}, 'Kevin': {'task1': 8, 'task3': 5}, 'Adam': {'task1': 11, 'task2': 2, 'task3': 1}, 'Eric': {'task2': 15}, 'Frank':{'task3': 12}, 'Sally': {'task3': 10}}
        self.log6 = {'Mark': {'task1': 5, 'task2': 2}, 'Kevin': {'task1': 10}, 'Adam': {'task1': 15, 'task2': 2}, 'Randy': {'task2': 10}, 'Eric': {'task2': 10}, 'Sally': {'task4': 16}}
        self.log7 = {'Eric': {'task5': 15, 'task6': 8}, 'Randy': {'task5': 20}, 'Sally': {'task6': 16}}
        self.log8 = {'Adam': {'task6': 15}, 'Kevin': {'task5': 20}, 'Sally': {'task6': 10}}
        # addSprints inputs/outputs
        self.sprint3 = {'task1': {'Bobby': 5, 'Randy': 10, 'Kevin': 8, 'Adam': 11}, 'task2': {'Randy': 4, 'Adam': 2, 'Eric': 15}, 'task3': {'Kevin': 5, 'Adam': 1, 'Frank': 12, 'Sally': 10}}
        self.sprint4 = {'task1': {'Mark': 5, 'Kevin': 10, 'Adam': 15}, 'task2': {'Mark': 2, 'Adam': 2, 'Randy': 10, 'Eric': 10}, 'task4': {'Sally': 16}}
        self.addedSprints2 = {'task1': {'Bobby': 5, 'Randy': 10, 'Kevin': 18, 'Adam': 26, 'Mark': 5}, 'task2': {'Randy': 14, 'Adam': 4, 'Eric': 25, 'Mark': 2}, 'task3': {'Kevin': 5, 'Adam': 1, 'Frank': 12, 'Sally': 10}, 'task4': {'Sally': 16}}
        # addNLogs input/output
        self.logList2 = [self.log5,self.log6,self.log7,self.log8]
        self.sprintSummary2 = {'task1': {'Bobby': 5, 'Randy': 10, 'Kevin': 18, 'Adam': 26, 'Mark': 5}, 'task2': {'Randy': 14, 'Adam': 4, 'Eric': 25, 'Mark': 2}, 'task3': {'Kevin': 5, 'Adam': 1, 'Frank': 12, 'Sally': 10}, 'task4': {'Sally': 16}, 'task5': {'Eric': 15, 'Randy': 20, 'Kevin': 20}, 'task6': {'Eric': 8, 'Sally': 26, 'Adam': 15}}
        # lookupVal inputs
        self.lookupList2 = [{"a": 1, "b": True}, {"b": False, "c": "found"}, {"d": 5}, {"a": "apple", "b": "banana"}]
        self.lookup2List = [(0,{"x":0,"y":True,"z":"zero"}), (0,{"x":1}), (1,{"y":False}), (1,{"x":3, "z":"three"}), (2,{})]
        # iterFile output
        self.filetokens2 = ["Joey","Mama","Loves","10","dogs"]
        self.histogram = [('-', 5), ('3', 3), ('355', 3), ('Assignment', 3), ('CptS', 3), ('Python', 3), ('Warmup', 3), ('for', 2), ('text', 2), ('.', 1), ('This', 1), ('With', 1), ('a', 1), ('file', 1), ('is', 1), ('repeated', 1), ('some', 1), ('test', 1)]
        
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        # sprintLog inputs
        self.log9 = {'Alice': {'task1': 5}, 'Bob': {'task1': 10, 'task2': 4}, 'Charlie': {'task1': 8, 'task3': 5}, 'David': {'task1': 11, 'task2': 2, 'task3': 1}, 'Eve': {'task2': 15}, 'Fiona': {'task3': 12}, 'Grace': {'task3': 10}}
        self.log10 = {'Mark': {'task1': 5, 'task2': 2}, 'Charlie': {'task1': 10}, 'David': {'task1': 15, 'task2': 2}, 'Bob': {'task2': 10}, 'Eve': {'task2': 10}, 'Grace': {'task4': 16}}
        self.log11 = {'Eve': {'task5': 15, 'task6': 8}, 'Bob': {'task5': 20}, 'Grace': {'task6': 16}}
        self.log12 = {'David': {'task6': 15}, 'Charlie': {'task5': 20}, 'Grace': {'task6': 10}}
        # addSprints inputs/outputs
        self.sprint5 = {'task1': {'Alice': 5, 'Bob': 10, 'Charlie': 8, 'David': 11}, 'task2': {'Bob': 4, 'David': 2, 'Eve': 15}, 'task3': {'Charlie': 5, 'David': 1, 'Fiona': 12, 'Grace': 10}}
        self.sprint6 = {'task1': {'Mark': 5, 'Charlie': 10, 'David': 15}, 'task2': {'Mark': 2, 'David': 2, 'Bob': 10, 'Eve': 10}, 'task4': {'Grace': 16}}
        self.addedSprints3 = {'task1': {'Alice': 5, 'Bob': 10, 'Charlie': 18, 'David': 26, 'Mark': 5}, 'task2': {'Bob': 14, 'David': 4, 'Eve': 25, 'Mark': 2}, 'task3': {'Charlie': 5, 'David': 1, 'Fiona': 12, 'Grace': 10}, 'task4': {'Grace': 16}}
        # addNLogs input/output
        self.logList3 = [self.log9, self.log10, self.log11, self.log12]
        self.sprintSummary3 = {'task1': {'Alice': 5, 'Bob': 10, 'Charlie': 18, 'David': 26, 'Mark': 5}, 'task2': {'Bob': 14, 'David': 4, 'Eve': 25, 'Mark': 2}, 'task3': {'Charlie': 5, 'David': 1, 'Fiona': 12, 'Grace': 10}, 'task4': {'Grace': 16}, 'task5': {'Eve': 15, 'Bob': 20, 'Charlie': 20}, 'task6': {'Eve': 8, 'Grace': 26, 'David': 15}}
        # lookupVal inputs
        self.lookupList3 = [{"x": 5, "y": True, "z": "new_value"}, {"x": 8}, {"y": False, "z": "updated"}]
        self.lookup2List = [(0,{"x":0,"y":True,"z":"zero"}), (0,{"x":1}), (1,{"y":False}), (1,{"x":3, "z":"three"}), (2,{})]
        # iterFile output
        self.filetokens3 = ["Be","sure","to","spend","time","with","your","parents","while","they're","still","here."]
        self.histogram = [('-', 5), ('3', 3), ('355', 3), ('Assignment', 3), ('CptS', 3), ('Python', 3), ('Warmup', 3), ('for', 2), ('text', 2), ('.', 1), ('This', 1), ('With', 1), ('a', 1), ('file', 1), ('is', 1), ('repeated', 1), ('some', 1), ('test', 1)]

        #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#sprintLog testCases   
    def test_sprintLog(self):
        self.assertDictEqual(sprintLog(self.log1),self.sprint1)
        self.assertDictEqual(sprintLog(self.log2),self.sprint2)  
    
        
    def test2_sprintLog(self):
        #testCase Batch 2
        self.assertDictEqual(sprintLog(self.log5),self.sprint3) 
        self.assertDictEqual(sprintLog(self.log6),self.sprint4)
        
    def test3_sprintLog(self):
        #testCase Batch 3
        self.assertDictEqual(sprintLog(self.log9),self.sprint5)
        self.assertDictEqual(sprintLog(self.log10),self.sprint6)
        
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#addSprints testCases
    def test_addSprints(self):
        self.assertDictEqual(addSprints(self.sprint1,self.sprint2),self.addedSprints)
    
    def test2_addSprints(self):    
        #testCase Batch 2
        self.assertDictEqual(addSprints(self.sprint3,self.sprint4),self.addedSprints2)
        
    def test3_addSprints(self):
        #testCase Batch 3
        self.assertDictEqual(addSprints(self.sprint5,self.sprint6),self.addedSprints3)
        
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#addLogs testCases
    def test_addNLogs(self):
        self.assertDictEqual(addNLogs(self.logList),self.sprintSummary)
        
    def test2_addNLogs(self):    
        #testCase Batch 2
        self.assertDictEqual(addNLogs(self.logList2),self.sprintSummary2)

    def test3_addNLogs(self): 
        #testCase Batch 3
        self.assertDictEqual(addNLogs(self.logList3),self.sprintSummary3)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# lookupVal testCases
    def test_lookupVal(self):
        self.assertEqual(lookupVal(self.lookupList,"x"),2)
        self.assertEqual(lookupVal(self.lookupList,"y"),False)
        self.assertEqual(lookupVal(self.lookupList,"z"),"found")
        self.assertEqual(lookupVal(self.lookupList,"t"),None)
        
    def test_lookupVal2(self):
        self.assertEqual(lookupVal(self.lookupList2, "a"), "apple")
        self.assertEqual(lookupVal(self.lookupList2, "b"), "banana")
        self.assertEqual(lookupVal(self.lookupList2, "c"), "found")
        self.assertEqual(lookupVal(self.lookupList2, "d"), 5)
        self.assertEqual(lookupVal(self.lookupList2, "e"), None)
        
    
    def test_lookupVal3(self):
        self.assertEqual(lookupVal(self.lookupList3, "x"), 8)
        self.assertEqual(lookupVal(self.lookupList3, "y"), False)
        self.assertEqual(lookupVal(self.lookupList3, "z"), "updated")
        self.assertEqual(lookupVal(self.lookupList3, "t"), None)
           
    
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# custom made since none was provided in sample
    
    def test_unzip(self):
        pass
    
    def test_unzip2(self):
        unzipList1 = [({"hello": 1}, "a", 10), ({"world": 2}, "b", 100), ({"!": 3}, "c", 1000)]
        unzipResult1 = ([{"hello": 1}, {"world": 2}, {"!": 3}], ['a', 'b', 'c'], [10, 100, 1000])
        self.assertEqual(unzip(unzipList1), unzipResult1)
        
    def test_unzip3(self):
        unzipList2 = [(5, "w", {1: "a"}), (10, "x", {2: "b"}), (15, "y", {3: "c"}), (20, "z", {4: "d"})]
        unzipResult2 = ([5, 10, 15, 20], ['w', 'x', 'y', 'z'], [{1: 'a'}, {2: 'b'}, {3: 'c'}, {4: 'd'}])
        self.assertEqual(unzip(unzipList2), unzipResult2)



    def test_numPaths(self):
        pass
    
    def test_numPaths1(self):
        self.assertEqual(numPaths(3, 3, [(2, 2)]), 2)
        
    def test_numPaths2(self):
        self.assertEqual(numPaths(10, 3, [(2, 2), (7, 1)]), 27)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#iterFile testCases

    def test_iterFile(self):
        mywords = iterFile(r"C:\Users\Harish Sridharan\Documents\Computer Programming\cpts355\assignment3\HW3testfile.txt")
        self.assertEqual(mywords.__next__(),"CptS")
        self.assertEqual(mywords.__next__(),"355")
        self.assertEqual(mywords.__next__(),"Assignment")
        restofFile = []
        for word in mywords:
            restofFile.append(word)
        self.assertEqual(restofFile,self.filetokens[3:])
        
    def test_iterFile2(self):
        mywords2 = iterFile(r"C:\Users\Harish Sridharan\Documents\Computer Programming\cpts355\assignment3\testFile2.txt")
        self.assertEqual(mywords2.__next__(),"Joey")
        self.assertEqual(mywords2.__next__(),"Mama")
        self.assertEqual(mywords2.__next__(),"Loves")
        restofFile2 = []
        for word2 in mywords2:
            restofFile2.append(word2)
        self.assertEqual(restofFile2,self.filetokens2[3:])
        
    def test_iterFile2(self):
        mywords3 = iterFile(r"C:\Users\Harish Sridharan\Documents\Computer Programming\cpts355\assignment3\testFile3.txt")
        self.assertEqual(mywords3.__next__(),"Be")
        self.assertEqual(mywords3.__next__(),"sure")
        self.assertEqual(mywords3.__next__(),"to")
        restofFile3 = []
        for word3 in mywords3:
            restofFile3.append(word3)
        self.assertEqual(restofFile3,self.filetokens3[3:])

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# custom histogramTest Cases

    def test_wordHistogram(self):
        pass
        

if __name__ == '__main__':
    unittest.main()

