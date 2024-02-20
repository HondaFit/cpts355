-- CptS 355 - Spring 2024 Assignment 2
-- Harish Sridharan
-- the test.hs was used for debugging and testing my code with the examples in the assignment. I later just copied and pasted into HW2.hs

module HW2
     where


{- 1-  merge2 & merge2Tail & mergeN - 22% -}
--merge2
--Part A: Nomrol recursive murge function for two sorted list. Compare elements from two lists and arranges them 
--least to greatest
merge2 :: Ord a => [a] -> [a] -> [a]
merge2 [] ys = ys
merge2 xs [] = xs 
merge2 (x:xs) (y:ys)
    | x <= y    = x : merge2 xs (y:ys)
    | otherwise = y : merge2 (x:xs) ys


--merge2Tail
--Part B: Tail recursive merge function
merge2Tail :: Ord a => [a] -> [a] -> [a]
merge2Tail [] ys = reverse ys
merge2Tail xs [] = reverse xs
merge2Tail (x:xs) (y:ys) 
    | x <= y = x : merge2Tail xs (y:ys)
    | otherwise = y : merge2Tail (x:xs) ys

revAppend :: [a] -> [a] -> [a]
revAppend [] ys = ys
revAppend (x:xs) ys = revAppend xs (x:ys)

--mergeN
--Part C: merge multiple sorted ist using foldl
mergeN :: Ord a => [[a]] -> [a]
mergeN xs = foldl1 merge2 xs



{- 2 - getInRange & countInRange - 18% -}

--getInRange
--Part A. returns a list of elements from the input list that fall within the range 
getInRange :: Ord a => a -> a -> [a] -> [a]
getInRange v1 v2 nums = 
  let
    inRange x = x > v1 && x < v2 
    filtered = filter inRange nums
  in
    filter inRange filtered

--countInRange
--Part B: conts the total number of elemtns in multiple lists that fall within the range
countInRange :: Ord a => a -> a -> [[a]] -> Int
countInRange v1 v2 iLL = sum $ map (length . filterInRange v1 v2) iLL 
  where
    filterInRange :: Ord a => a -> a -> [a] -> [a]
    filterInRange v1 v2 l = filter (\x -> x > v1 && x < v2) l


{- 3 -  addLengths & addAllLengths - 18% -}

data LengthUnit =  INCH  Int | FOOT  Int | YARD  Int
                   deriving (Show, Read, Eq)
-- addLengths
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

-- addAllLengths
--Part B: adds multiple lenths and returns in inches.
addAllLengths :: Foldable t => t [LengthUnit] -> LengthUnit
addAllLengths lengths = foldl addLengths (INCH 0) (concat lengths)

{-4 - sumTree and createSumTree - 22%-}

data Tree a = LEAF a | NODE a  (Tree a)  (Tree a)
              deriving (Show, Read, Eq)

--sumTree
--Part A: calculates the sum of all values in tree
sumTree :: Num p => Tree p -> p
sumTree (LEAF x) = x
sumTree (NODE _ l r) = sumTree l + sumTree r

--createSumTree
--Part B: takes tree as parameter and returns new tree where each node is the sum of all vaues in subtree
createSumTree :: Num a => Tree a -> Tree a
createSumTree tree = 
  let sumLeaves (LEAF x) = x
      sumLeaves (NODE _ l r) = sumLeaves l + sumLeaves r
  in case tree of
    LEAF x -> LEAF x
    NODE _ l r -> NODE (sumLeaves tree) (createSumTree l) (createSumTree r)


{-5 - foldListTree - 20%-}
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



{- 6- Create two tree values :  Tree Integer  and  listTree a ;  Both trees should have at least 3 levels. -}

--Can be found in HW2SampleTest.hs