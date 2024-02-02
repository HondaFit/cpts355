-- CptS 355 - Spring 2024 Assignment 1
-- Please include your name and the names of the students with whom you discussed any of the problems in this homework

module HW1
     where

import Data.Char (toUpper)
import Distribution.Simple.Utils (listUnion)

-- 1. exists

exists :: Eq t => t -> [t] -> Bool  
exists val list = elem val list

--Part B: 


-- 2. listUnion

removeDuplicates:: Eq a=> [a] -> [a] -- seperate fucntion removes duplicates from list
removeDuplicates (x:xs)
  | x `elem` xs = removeDuplicates xs
  | otherwise   = x : removeDuplicates xs

listUnion :: Eq a => [a] -> [a] -> [a]
listUnion val1 val2 = removeDuplicates(val1 ++ val2) --function cateneates list and is used as a parameter for removeDuplicates

-- 3. replace



-- 4. prereqFor
prereqsList =
  [ ("CptS122" , ["CptS121"]),
  ("CptS132" , ["CptS131"]),
  ("CptS223" , ["CptS122", "MATH216"]),
  ("CptS233" , ["CptS132", "MATH216"]),
  ("CptS260" , ["CptS223", "CptS233"]),
  ("CptS315" , ["CptS223", "CptS233"]),
  ("CptS317" , ["CptS122", "CptS132", "MATH216"]),
  ("CptS321" , ["CptS223", "CptS233"]),
  ("CptS322" , ["CptS223","CptS233"]),
  ("CptS350" , ["CptS223","CptS233", "CptS317"]),
  ("CptS355" , ["CptS223"]),
  ("CptS360" , ["CptS223","CptS260"]),
  ("CptS370" , ["CptS233","CptS260"]),
  ("CptS427" , ["CptS223","CptS360", "CptS370", "MATH216", "EE234"])
  ]


prereqFor :: Eq t => [(a, [t])] -> t -> [a] 
prereqFor [] _ = []
prereqFor ((course, prereqs):courses) pre
  | pre `elem` prereqs = course : prereqFor courses pre
  | otherwise = prereqFor courses pre

  
-- 5. isPalindrome




-- 6. groupSumtoN