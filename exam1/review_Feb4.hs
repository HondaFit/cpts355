
{-
Things you learned:


- how to recursion
    - base cases
    - recursive cases


- overview of reductions (combining elements in a list)
    - like finding the min or calculating the sum


- tail recursion
    - usually with recursion a large call stack forms
        - one stack frame per function call, each storing information
        - each frame popped from stack when function returns
    - tail recursion doesn't grow the call stack
        - each function call simply updates the same stack frame
-}


--
-- ##### TAIL RECURSION #####
--


-- basic example
addup :: Num p => [p] -> p
addup lis = addupHelper 0 lis
    where
        addupHelper :: Num p => p -> [p] -> p
        addupHelper sum [] = sum
        addupHelper sum (x:xs) = addupHelper (sum + x) xs

-- notice how each return value is simply a function call, no values stored


-- tail reverse
fastReverse :: [a] -> [a]
fastReverse xs = revAppend xs []
    where
        revAppend :: [a] -> [a] -> [a]
        revAppend [] acc = acc
        revAppend (x:xs) acc = revAppend xs (x:acc)



--
-- ##### HIGHER ORDER FUNCTIONS #####
--


-- one of the more important things to take away from this class

{-
map: [a] -> [b]
    a -> b
    a -> b
    a -> b
    a -> b
    a -> b
- transforms every element in the list to a new type


filter: [a] -> [a]
    a -> b
    a -> _
    a -> b
    a -> b
    - -> _
- keeps certain elements from the list and removes the rest


reduce / fold: [a] -> b
    a |
    a |
    a | -> b
    a |
    a |
- iterates through all elements and generates a new value
    - this new value could also be a list, or it could be anything else

-}


-- map
addOne :: Num a => [a] -> [a]
addOne lis = map (\x -> x + 1) lis


-- filter
onlyEven :: (Integral a) => [a] -> [a]
onlyEven lis = filter (\x -> (x `rem` 2) == 0) lis


-- fold
flattenList :: [[a]] -> [a]
flattenList lis = foldr (\x acc -> x ++ acc) [] lis


-- NOTE: foldl starts the accumulator on the left and moves right
    --   foldr starts the accumulator on the right and moves left


flattenListLeft :: [[a]] -> [a]
flattenListLeft lis = foldl (\acc x -> acc ++ x) [] lis



{-
Challenges:

find max in nested lists
remove every other item from list
convert a list of tuples to just the second element
    - same, but only if the first element is True

-}



