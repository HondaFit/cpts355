-- | Merge two sorted lists l1 and l2 into a single sorted list.
-- | The resulting list includes elements from both lists and may contain duplicates.
-- | The function uses recursion to compare elements from both lists and merge them accordingly.
merge2 :: Ord a => [a] -> [a] -> [a]
merge2 [] l2 = l2
merge2 l1 [] = l1 
merge2 (x:xs) (y:ys) 
  | x <= y = x : merge2 xs (y:ys)  -- Add x to the merged list and proceed with the rest of l1 and l2
  | otherwise = y : merge2 (x:xs) ys -- Add y to the merged list and proceed with the rest of l1 and l2

-- | Tail-recursive version of the merge2 function.
-- | Uses an accumulator to build the result list in reverse, then appends the accumulator to the remaining list.
merge2Tail :: Ord a => [a] -> [a] -> [a]
merge2Tail l1 l2 = revAppend l1 l2 []  -- Start with an empty accumulator
  where
    revAppend [] l acc = acc ++ l     -- If the first list is empty, append the accumulator to the second list
    revAppend l [] acc = acc ++ l     -- If the second list is empty, append the accumulator to the first list
    revAppend (x:xs) (y:ys) acc       -- If both lists have elements:
      | x <= y = revAppend xs (y:ys) (x:acc)  -- Add x to the accumulator and proceed with the rest of l1 and l2
      | otherwise = revAppend (x:xs) ys (y:acc) -- Add y to the accumulator and proceed with the rest of l1 and l2

-- | Merge a list of sorted lists into a single sorted list using the merge2 function.
-- | Uses foldl to apply the merge operation to each pair of lists in the input list.
mergeN :: (Foldable t, Ord a) => t [a] -> [a]
mergeN = foldl1 merge2


---------------------------------------------------------------------------------------------------------------------------

-- | 'getInRange' filters elements in a list that are greater than 'low' and less than 'high' (exclusive).
-- It takes two values 'low' and 'high' and a list of elements 'nums'.
getInRange :: Ord a => a      -- ^ The lower bound value
                     -> a      -- ^ The upper bound value
                     -> [a]    -- ^ List of elements
                     -> [a]    -- ^ Filtered list of elements within the range
getInRange low high nums = filter inRange nums
    where
        -- | 'inRange' checks if an element falls within the specified range.
        inRange x = x > low && x < high

-- | 'countInRange' counts the total number of elements in nested lists that fall within the range specified by 'low' and 'high'.
-- It takes two values 'low' and 'high' and a list of lists 'lists'.
countInRange :: Ord a => a        -- ^ The lower bound value
                          -> a        -- ^ The upper bound value
                          -> [[a]]    -- ^ List of lists of elements
                          -> Int      -- ^ Total count of elements within the range
countInRange low high lists = sum $ map numInRange lists
    where
        -- | 'numInRange' calculates the number of elements within the range for a given list.
        numInRange xs = length $ getInRange low high xs

---------------------------------------------------------------------------------------------------------------------------
-- Define LengthUnit data type
data LengthUnit = INCH Int | FOOT Int | YARD Int
    deriving (Show, Read, Eq)

-- Add lengths function  
-- This function takes two LengthUnit values and calculates their sum in inches.
addLengths :: LengthUnit -> LengthUnit -> LengthUnit
addLengths (INCH a) (INCH b) = INCH (a + b)
addLengths (FOOT a) (INCH b) = INCH (a * 12 + b)  
addLengths (INCH a) (FOOT b) = INCH (a + b * 12)
addLengths (YARD a) (INCH b) = INCH (a * 36 + b)
addLengths (INCH a) (YARD b) = INCH (a + b * 36)  
addLengths (FOOT a) (FOOT b) = INCH (a * 12 + b * 12)
addLengths (YARD a) (FOOT b) = INCH (a * 36 + b * 12)
addLengths (FOOT a) (YARD b) = INCH (a * 12 + b * 36)
addLengths (YARD a) (YARD b) = INCH (a * 36 + b * 36)

-- Helper function to convert LengthUnit to inches
-- This function converts a LengthUnit value to inches.
toInches :: LengthUnit -> Int
toInches (INCH a) = a
toInches (FOOT a) = a * 12
toInches (YARD a) = a * 36

-- Add all lengths
-- This function takes a nested list of LengthUnit values and calculates the sum of those in inches.
addAllLengths :: [[LengthUnit]] -> LengthUnit
addAllLengths lengths = INCH (sum $ map (toInches . foldl1 addLengths) lengths)

---------------------------------------------------------------------------------------------------------------------------
-- Define a polymorphic binary tree data structure where each node can be either a leaf containing a value of type 'a'
-- or an interior node containing a value of type 'a' along with left and right subtrees.
data Tree a = LEAF a | NODE a (Tree a) (Tree a)  
    deriving (Show, Read, Eq)

-- | sumTreeLeaves function calculates the sum of the values stored in the leaves of the tree.
sumTreeLeaves :: (Num a) => Tree a -> a
sumTreeLeaves (LEAF x) = x                             -- If the node is a leaf, return its value.
sumTreeLeaves (NODE _ left right) =                     -- If the node is an interior node,
    sumTreeLeaves left + sumTreeLeaves right            -- recursively calculate the sum of values in the left and right subtrees.

-- | createSumNode function takes a sum and a tree, and creates a new tree where the interior nodes store the sum 
-- of the values of the leaves underneath them.
createSumNode :: (Num a) => a -> Tree a -> Tree a 
createSumNode sum (LEAF x) = LEAF x                                             -- If the node is a leaf, return it.
createSumNode sum (NODE _ left right) =                                          -- If the node is an interior node,
    NODE sum (createSumNode (sumTreeLeaves left) left)                            -- create a new node with the sum as its value
              (createSumNode (sumTreeLeaves right) right)                         -- and recursively apply to the left and right subtrees.

-- | createSumTree function takes a tree and returns a new tree where the interior nodes store the sum of the leaf values underneath them.
createSumTree :: (Num a) => Tree a -> Tree a
createSumTree t = createSumNode (sumTreeLeaves t) t                               -- Start the creation with the sum of the entire tree and the tree itself.

---------------------------------------------------------------------------------------------------------------------------
-- Define a polymorphic tree data structure where each node can be either a leaf containing a list of elements of type 'a',
-- or an interior node containing a list of child trees.
data ListTree a = ListLEAF [a] | ListNODE [(ListTree a)]
    deriving (Show, Read, Eq)

-- Define a function 'foldListTree' that folds over a ListTree structure by combining elements using a binary function 'f',
-- starting with an initial accumulator 'acc'.
foldListTree :: (a -> a -> a) -> a -> ListTree a -> a
foldListTree _ acc (ListLEAF lis) = foldl f acc lis -- If the tree node is a leaf, fold over the list using the binary function 'f'.
    where 
        f a b = a `f` b -- Apply the binary function 'f' to combine two elements.

-- If the tree node is an interior node, fold over each child tree recursively using 'foldListTree'.
foldListTree f acc (ListNODE trees) = 
    foldl (\acc tree -> foldListTree f acc tree) acc trees

-- Example tree structure for testing.
helper :: ListTree Int  
helper = ListNODE [
                    ListLEAF [1,2],
                    ListLEAF [3,4],  
                    ListNODE [
                        ListLEAF [5,6],
                        ListLEAF [7,8]
                    ]
                   ]

-- Test the foldListTree function by folding over the tree structure 'helper' with addition as the combining function.
test = foldListTree (+) 0 helper -- Returns 36

---------------------------------------------------------------------------------------------------------------------------

-- Define a binary tree data structure
data Tree a = LEAF a | NODE a (Tree a) (Tree a)

-- Define a tree-like data structure using lists
data ListTree a = ListLEAF [a] | ListNODE [ListTree a]

-- Sample trees
t3 :: Tree Integer  
t3 = NODE 10 
        (NODE 3 (LEAF 2) (LEAF 5))
        (NODE 4 (LEAF 1) (LEAF 3))

-- Sample list trees
l1 :: ListTree Int
l1 = ListLEAF [1,2,3]  
l2 = ListLEAF [4,5]
l3 = ListLEAF [6]  
l4 = ListLEAF []
t4 :: ListTree Int
t4 = ListNODE 
        [ListNODE [l1, l2, ListNODE [l3, l4]],
         ListNODE []]

-- Function to calculate the sum of values in a binary tree
sumTree :: Num p => Tree p -> p  
sumTree (LEAF x) = x
sumTree (NODE n left right) = n + sumTree left + sumTree right

-- Function to create a new binary tree where each node contains the sum of its children
createSumTree :: Num a => Tree a -> Tree a
createSumTree (LEAF x) = LEAF x
createSumTree (NODE _ left right) = 
    let leftSum = sumTree left
        rightSum = sumTree right
    in NODE (leftSum + rightSum) (createSumTree left) (createSumTree right)

-- Function to fold a ListTree structure into a single value using a binary function
foldListTree :: (a -> a -> a) -> a -> ListTree a -> a
foldListTree _ acc (ListLEAF xs) = foldl f acc xs
    where f a x = a `f` x 
foldListTree f acc (ListNODE trees) = 
    foldl (\acc' tree -> foldListTree f acc' tree) acc trees


