-- CptS 355 - Spring 2024 Assignment 1
-- Please include your name: Akalya Sridharan


module HW1
    where

import Data.Char (toUpper)

import System.Environment


--module Main where


--main = putStrLn "Hello World!"

-- 1. exists

-- exists function declaration
-- Takes an element x and a list [t], returns True if x exists in the list, otherwise False.
-- Constraints: t must be an instance of Eq.

exists :: (Eq t) => t -> [t] -> Bool

-- Base case: If the list is empty, the element does not exist, return False.
exists x [] = False

-- Recursive case: Check if the current element y is equal to x.
-- If it is, return True.
-- Otherwise, recursively check in the rest of the list (ys).
exists x (y:ys)
    | x == y = True
    | otherwise = exists x ys


{-  why the type is exists :: Eq t => t -> [t] -> Bool but not exists :: t -> [t] -> Bool ?

This type signature uses the Eq type class constraint, this means that the type t has to be of the Eq type class. 
Which is necessary for comparing whether a value is equal to an element in the list.

If we had the type exists :: t -> [t] -> Bool, it means that it can be any type t, regardless of whether t supports == comparison. 
This leads to a problem because the == operator used inside the function wouldn't work for types that are not instances of Eq.          -}

-- 2. listUnion
--takes two lists and returns a new list containing the elements of both lists, with duplicates removed. The function uses two helper functions:
--removeDuplicates and remove. removeDuplicates removes duplicates from a list, while remove removes a specific element from a list.
-- Define a function listUnion that takes two lists of elements of type 'a' where 'a' is an instance of the Eq typeclass.
listUnion :: Eq a => [a] -> [a] -> [a]

-- Define listUnion function: It takes two lists x and y, removes duplicates, and returns a new list containing unique elements from both lists.
listUnion x y = removeDuplicates (x ++ y)

    -- Define a local function removeDuplicates that removes duplicates from a list.
    where
        -- removeDuplicates function takes a list and returns a new list without duplicates.
        removeDuplicates :: Eq a => [a] -> [a]
        removeDuplicates [] = [] -- Base case: Empty list, return an empty list.
        removeDuplicates (x:xs) = x : removeDuplicates (remove x xs) -- If the current element is not a duplicate, keep it and recurse with the rest of the list.

        -- Define a local function remove that removes a specific element from a list.
        remove :: Eq a => a -> [a] -> [a]
        remove x [] = [] -- Base case: Empty list, return an empty list.
        -- If the current element matches the one to remove, skip it; otherwise, keep it and recurse.
        remove i (x:xs) | i == x = remove i xs
                        | otherwise = x : remove i xs


-- 3. replace
replace :: (Eq t1, Num t1) => t1 -> t2 -> [t2] -> [t2]

replace n v list | null list = list
                 | otherwise = replaceHelper n v list
            where
                replaceHelper :: (Eq t1, Num t1) => t1 -> t2 -> [t2] -> [t2]
                replaceHelper n v [] = []
                replaceHelper 0 v (x:xs) = v : xs
                replaceHelper n v (x:xs) = x : replaceHelper (n-1) v xs




-- 4. prereqFor
prereqFor :: Eq t => [(a, [t])] -> t -> [a]

prereqFor prereqsList course = getCourses prereqsList course
    where
        getCourses :: Eq t => [(a, [t])] -> t -> [a]
        getCourses [] x = []
        getCourses ((x,prereqs):xs) course | elem course prereqs = x : getCourses xs course
                                           | otherwise = getCourses xs course




-- 5. isPalindrome  
isPalindrome :: [Char] -> Bool

isPalindrome a | length a < 2 = True
               | cleanedStr == reverse cleanedStr = True
               | otherwise = False
            where 
                upperStr = toUpperStr a  
                cleanedStr = removeSpace upperStr

                -- helper function to remove spaces 
                removeSpace :: [Char] -> [Char]
                removeSpace [] = []
                removeSpace (x:xs) | x == ' ' = removeSpace xs       
                                   | otherwise = x : removeSpace xs

                -- helper function to set the capitlization the same in the string
                toUpperStr :: [Char] -> [Char]
                toUpperStr [] = []
                toUpperStr (x:xs) = toUpper x : toUpperStr xs
            

  
-- used this website : https://subscription.packtpub.com/book/data/9781783286331/2/ch02lvl1sec23/trimming-excess-whitespace to learn how to remove spaces from a string
-- nvm asked prof and he said not to use those and to create our own



-- 6. groupSumtoN
groupSumtoN :: (Ord a, Num a) => a -> [a] -> [[a]]

groupSumtoN x [] = [[]]
groupSumtoN x xs = list x xs []
    where
        list x [] acc = [acc]
        list x (y:ys) acc | x >= sum (acc ++ [y]) = list x ys (acc ++ [y])
                          | otherwise = acc : list x ys [y]
        



