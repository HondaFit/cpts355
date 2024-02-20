--This is a just a file to test out my code without modifying other HW2 and HW2Sample



-------------------------------------------------------------------------------------------------------- Problem 1
--Part A: Nomrol recursive murge function for two sorted list. Compare elements from two lists and arranges them 
--least to greatest
merge2 :: Ord a => [a] -> [a] -> [a]
merge2 [] ys = ys
merge2 xs [] = xs 
merge2 (x:xs) (y:ys)
    | x <= y    = x : merge2 xs (y:ys)
    | otherwise = y : merge2 (x:xs) ys

--Part B: Tail recursive merge function.
merge2Tail :: Ord a => [a] -> [a] -> [a]
merge2Tail [] ys = reverse ys
merge2Tail xs [] = reverse xs
merge2Tail (x:xs) (y:ys) 
    | x <= y = x : merge2Tail xs (y:ys)
    | otherwise = y : merge2Tail (x:xs) ys

revAppend :: [a] -> [a] -> [a]
revAppend [] ys = ys
revAppend (x:xs) ys = revAppend xs (x:ys)

--Part C: merge multiple sorted ist using foldl
mergeN :: Ord a => [[a]] -> [a]
mergeN xs = foldl1 merge2 xs


    

--------------------------------------------------------------------------------------------------------Problem 2
--Part A. returns a list of elements from the input list that fall within the range 
getInRange :: Ord a => a -> a -> [a] -> [a]
getInRange v1 v2 nums = 
  let
    inRange x = x > v1 && x < v2 
    filtered = filter inRange nums
  in
    filter inRange filtered

--Part B: conts the total number of elemtns in multiple lists that fall within the range
countInRange :: Ord a => a -> a -> [[a]] -> Int
countInRange v1 v2 numLists = 
  let
    countInList xs = length (getInRange v1 v2 xs)
  in 
    foldl (+) 0 (map countInList numLists)


--------------------------------------------------------------------------------------------------------Problem 3
data LengthUnit = INCH Int | FOOT Int | YARD Int  
    deriving (Show, Read, Eq)

--Part A: adds two lengths values and returns in inches
addLengths :: LengthUnit -> LengthUnit -> LengthUnit
addLengths (INCH a) (INCH b) = INCH (a + b)
addLengths (FOOT a) (FOOT b) = INCH ((a * 12) + (b * 12))  
addLengths (YARD a) (YARD b) = INCH ((a * 36) + (b * 36))
addLengths (INCH a) (FOOT b) = INCH (a + (b * 12)) 
addLengths (INCH a) (YARD b) = INCH (a + (b * 36))
addLengths (FOOT a) (INCH b) = INCH ((a * 12) + b)  
addLengths (FOOT a) (YARD b) = INCH ((a * 12) + (b * 36))
addLengths (YARD a) (INCH b) = INCH ((a * 36) + b)
addLengths (YARD a) (FOOT b) = INCH ((a * 36) + (b * 12))

--Part B: adds multiple lenths and returns in inches.
addAllLengths :: Foldable t => t [LengthUnit] -> LengthUnit
addAllLengths lengths = foldl addLengths (INCH 0) (concat lengths)

--------------------------------------------------------------------------------------------------------Problem 4
data Tree a = LEAF a | NODE a  (Tree a)  (Tree a)
              deriving (Show, Read, Eq)

--Part A: calculates the sum of all values in tree
sumTree :: Num p => Tree p -> p
sumTree (LEAF x) = x
sumTree (NODE _ l r) = sumTree l + sumTree r


--Part B: takes tree as parameter and returns new tree where each node is the sum of all vaues in subtree
createSumTree :: Num a => Tree a -> Tree a
createSumTree tree = 
  let sumLeaves (LEAF x) = x
      sumLeaves (NODE _ l r) = sumLeaves l + sumLeaves r
  in case tree of
    LEAF x -> LEAF x
    NODE _ l r -> NODE (sumLeaves tree) (createSumTree l) (createSumTree r)

--------------------------------------------------------------------------------------------------------Problem 5

data ListTree a = ListLEAF [a] | ListNODE [(ListTree a)]
                  deriving (Show, Read, Eq)

--applies folding function to collapse listree stirng into a single function
foldListTree :: (a -> a -> a) -> a -> ListTree a -> a 
foldListTree f base (ListLEAF xs) = foldl f base xs
foldListTree f base (ListNODE trees) = 
  let
    foldNode [] acc = acc 
    foldNode (t:ts) acc = foldNode ts (foldListTree f acc t)
  in
    foldNode trees base
    where
    concatLists :: [[a]] -> [a]
    concatLists [] = []  
    concatLists (x:xs) = x ++ concatLists xs


-------------------------------------------------------------------------------------------------------- Problem 6


--------------------------------------------------------------------------------------------------------
main :: IO ()
main = do

    let list1 = [1, 3, 5, 7, 9]
        list2 = [2, 4, 6, 8, 10]
        list3 = [11, 13, 15, 17, 19]
        list4 = [12, 14, 16, 18, 20]
        listOfLists = [list1, list2, list3, list4]
    putStrLn "Merging two lists using merge2:"
    print (merge2 list1 list2)
    putStrLn "\nMerging two lists using merge2Tail:"
    print (merge2Tail list1 list2)
    putStrLn "\nMerging a list of lists using mergeN:"
    print (mergeN listOfLists)



    let nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    let numLists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    putStrLn "\nTesting getInRange function:"
    putStrLn ("Numbers in range: " ++ show (getInRange 3 7 nums))
    putStrLn "\nTesting countInRange function:"
    putStrLn ("Count of numbers in range: " ++ show (countInRange 3 7 numLists))

    putStrLn "\nTesting addLengths:"
    print (addLengths (FOOT 2)(INCH 5))
    print (addLengths (YARD 3)(INCH 3))
    print (addLengths (FOOT 3)(FOOT 5))

    putStrLn "\nTesting addAllLengths"
    print (addAllLengths [[YARD 2, FOOT 1], [YARD 1, FOOT 2, INCH 10],[YARD 3]])
    print (addAllLengths [[FOOT 2], [FOOT 2, INCH 2],[]])

    
    
    putStrLn "\nTesting sumTree"
    let tree = NODE 1
            (NODE 1 (NODE 3 (LEAF 4) (LEAF 5)) (LEAF 6))
            (NODE 7 (LEAF 8) (LEAF 9))
    --putStrLn "\nOriginal Tree:"
    --print tree
    print (sumTree tree)

    putStrLn "\n Testing createSumTree"
    let tree2 = NODE 0
            (NODE 0 (NODE 0 (LEAF 4) (LEAF 5)) (LEAF 6))
            (NODE 0 (LEAF 8)(LEAF 9))
    print (createSumTree tree2)


--unable to get the example from the assignment to work? Could be a bug. For problem 5 and 6. Hopefully it works in the HW2.hs

