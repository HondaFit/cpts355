
score1 = 79
score2 = 83
score3 = 100
--as you can see it takes a while to multiple values of the same categories 

scores:: [Int]
scores = [79,83,100,92,56,74] --instead we can use list to store multiple values 

main = do 
    {-print score1
    print score2
    print score3-}

    print (scores !! 0) -- use need "!! " followed by a the index to access the list
    print (scores !! 1)
    print (scores !! 2)
    putStrLn ("")
    print (head scores) --grabs the 0th index of list
    print (last scores) --grabs the last index of the list
    print (init scores) --grabs everything but the last index
    print (tail scores) --grabs everything but the 0th index




