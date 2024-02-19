
-- for importing with ghci, use :l [filename]

{-
Multiline Comment
woo
-}

-- single line comment


-- type inference
x = 3
-- :t x

-- explicit typing
y = 4 :: Int
-- :t y


-- FUNCTIONS AND PARAMETERS

-- for type info in ghci, do :t [variable_name]

{-
    Anatomy of a function declaration:
    [my_func_name] :: [type]
    [my_func_name] [arg1] [arg2] [arg3] ... = [function body / return value]
-}

addTogether :: Int -> Int -> Int
addTogether num1 num2 = num1 + num2

-- negatives should be in parentheses for function calls
a = addTogether 10 (-4)
b = -3 --this is fine though

-- omitting type information can make a function generic
addTogetherGeneric num1 num2 = num1 + num2
--z = addTogether 10.3 (-4)
z = addTogetherGeneric 10.3 (-4)


-- use type declarations when possible, helps especially when things get more complex
-- haskell may guess your type wrong, leading to bugs, so being explicit can be helpful


-- CURRYING
addTwoNums :: (Num a) => a -> a -> a
addTwoNums first second = first + second

norm = addTwoNums 3 4

addToThree = addTwoNums 3.0
curried = addToThree 8
curried1 = addToThree 13


variable1 = 2


-- RECURSION
longMultiplication :: (Eq a, Num a) => a -> a -> a
longMultiplication x y = if x == 1
                         then y
                         else y + longMultiplication (x-1) y
c = longMultiplication 3 4
d = longMultiplication 5 1


-- DO KEYWORD
perimeterRectangle :: Num a => a -> a -> a
perimeterRectangle length width = do
    let sides = length * 2
    let vertical = width * 2
    sides + vertical

e = perimeterRectangle 3 4
f = perimeterRectangle 10 2


-- INFIX vs PREFIX
g = 3 + 4
h = (+) 3 4
i = elem 25 [1, 24, 3, 40]
j = 25 `elem` [1, 24, 3, 40]

k = 10 `perimeterRectangle` 2






appendStrInt :: [Char] -> Int -> Int -> [Char]
appendStrInt string integer integer1 = string ++ show integer ++ show integer1


--printResults :: (Show a, Show b) => a -> b -> [Char]
printResults :: (Show a) => a -> a -> [Char]
printResults var0 var1 = show var0 ++ show var1



variableOne :: Float
variableOne = 3 + 2
variableTwo = show variableOne
variableThree = (3 :: Float) + 2
variableFour = (3 + 2) :: Float



-- Tail Recursion


