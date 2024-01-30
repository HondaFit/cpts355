
--
-- ##### TYPE CLASSES #####
--

-- parameterized types
exampleFunc :: (Eq a, Ord a) => a -> a -> a
exampleFunc arg1 arg2 = arg1


-- simpler example
exampleFunc1 :: Integral a => a -> a
exampleFunc1 arg1 = arg1


{-
Some useful type classes:
    Show (the variable can be converted to a string)
    Eq (equality can be checked)
    Ord (two variables can be ordered)
    Num (basic arithmetic operations)
    Integral (can be modded, divided)
    Fractional (stores values with decimal points)
-}


exampleFunc2 :: Show a => a -> a
exampleFunc2 x = x



--
-- ##### TUPLES #####
--

-- basic tuple
myTuple :: (Bool, Integer, String)
myTuple = (True, 1, "one")


-- nested
nestedTuple :: (Bool, (Integer, String), Double)
nestedTuple = (True, (2, "two"), 2.0)


-- grabbing first and second for 2-sized tuples
coords = (3.2, -10.4)

xCoord = fst coords
yCoord = snd coords
-- NOTE: fst and snd only work for 2-sized tuples



--
-- ##### LISTS #####
--

-- basic list
someNums :: [Integer]
someNums = [3, 2, 56, 10, 3, 20, 34, 26, 43]

someTuples :: [(Integer, Integer)]
someTuples = [(1, 2), (3,2), (50, 25)]


-- ranges

{-
    [first..]
    [first, second..]
    [first..last]
    [first,second..last]
-}

-- range examples
rangeOne = [2..15] --both ends included
rangeTwo = [1,4..30] --count by 3's from 1 to 30


-- using range in function
evenNumbers :: Integer -> [Integer]
evenNumbers cap = [2,4..cap]
-- NOTE: use ghci to show calling 0, 1, 2, 3, 4, 5, 6


-- cons
firstList = evenNumbers 10
secondList = 13 : firstList --pushed to front


-- append two lists
thirdList = evenNumbers 8
fourthList = thirdList ++ secondList


-- push to end
lis = secondList ++ [15]


-- splitting
alpha = head lis
beta = tail lis


-- better splitting via pattern matching
(alphaOne:betaOne) = lis


-- ignoring with pattern matching
(_:betaTwo) = lis


-- indexing
omega = lis !! 3 --haskell is 0-indexed
-- NOTE: indexing like this is not recommended usually


-- length, elem
-- sum, product


-- maximum:
var1 = maximum [1, 24, 3, 41] --41

-- minimum:
var2 = minimum [1, 24, 3, 41] --1

-- elem:
var3 = elem 24 [1, 24, 3, 41] --True
-- can also infix as
--      24 `elem` [1, 24, 3, 41]
var4 = elem 25 [1, 24, 3, 41] --False

-- max: similar to maximum but only operates on two values
var5 = max 2 5 --5
var6 = max 10 2 --10



--
-- ##### PATTERNS AND CONDITIONALS #####
--

-- if statements
maxNum :: Ord a => a -> a -> a
maxNum x y = if x >= y
             then x
             else y

oneLine x y = if x >= y then x else y


-- guards (better)
maxNum1 :: (Ord a, Num a) => a -> a -> a
maxNum1 x y
    | x >= y = x
    | x > (y - 5) = 0
    | x < y = y


-- some fun with guards and "do"
funFunc :: Integer -> Integer
funFunc n
    | n >= 10 = do
        let square = n * n
        let diff = square - n
        diff
    | otherwise = n


funFunc1 :: Integer -> Integer
funFunc1 n
    | n >= 10 =
        let
            square = n * n
            diff = square - n
        in
            diff
    | otherwise = n


-- basic pattern matching
retFirst :: Show a => [a] -> [a]
retFirst [] = []
retFirst (x:xs) = [x]


-- NOTE: always put most restrictive patterns at the top
retSecond :: Show a => [a] -> [a]
retSecond (x:y:xs) = [y] --this case will never happen because of previous pattern
--retSecond (x:xs) = []
--retSecond [] = []
retSecond _ = []


-- "let in"
addOneCoords :: (Integer, Integer) -> (Integer, Integer)
addOneCoords (x, y) =
    let
        addOne :: Integer -> Integer --helper function
        addOne x = x + 1
    in
        (addOne x, addOne y)


-- "where"
addTwoCoords :: (Integer, Integer) -> (Integer, Integer)
addTwoCoords (x, y) = (addTwo x, addTwo y + anotherVariable)
    where
        --helper function
        addTwo :: Integer -> Integer
        addTwo x = x + 2
        anotherVariable = 10


-- functions declared in "where" or "let..in" clauses are not accessible here
--example = addTwo 3


-- if list has a 2 in the second index then add the num
coolFunc :: (Integer, [Integer]) -> [Integer]
coolFunc (n, (x:2:xs)) = x : (2 + n) : xs
coolFunc (_, xs) = xs
-- coolFunc (3, [1, 2, 3, 4])



--
-- ##### RECURSION #####
--

nthElement :: Show a => [a] -> Integer -> a
nthElement [] _ = error "Bad index"
nthElement (x:xs) 0 = x
nthElement (x:xs) n = nthElement xs (n - 1)


-- sneak peak at algebraic types
nthMaybe :: Show a => [a] -> Integer -> Maybe a
nthMaybe [] _ = Nothing
nthMaybe (x:xs) n
    | n > 0 = nthMaybe xs (n - 1)
    | n == 0 = Just x
    | n < 0 = Nothing

{-
enum Maybe {
    Nothing
    Just Integer
}
-}



-- NOTE: remember to put negatives in parentheses in parameters


-- another recursive example
addAll :: [Integer] -> Integer
addAll [] = 0
addAll (x:xs) = x + addAll xs


{-
addAll [3, 4, 2, 43, 5]
    3 + addAll [4, 2, 43, 5]
    3 + 4 + addAll [2, 43, 5]
    3 + 4 + 2 + addAll [43, 5]
    3 + 4 + 2 + 43 + addAll [5]
    3 + 4 + 2 + 43 + 5 + addAll []
    3 + 4 + 2 + 43 + 5 + 0
-}


factorial' :: Integer -> Integer
factorial' 1 = 1
factorial' n = n * factorial' (n - 1)


data CustomType = First Integer | Second Integer Integer | Third

coolFunc2 :: CustomType -> Integer
coolFunc2 (First n) = n
coolFunc2 (Second x y) = x + y
coolFunc2 Third = -1


data TreeNode = InternalNode TreeNode | Leaf Integer

{-
enum CustomType {
    First Integer,
    Second Integer Integer,
    Third,
}
-}




