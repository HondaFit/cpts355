--Final version for testing functions for problems
--Note, this is not done yet. There are functinos for Problem 3,5,6 but there are bugs that need to be resolved. Once resolved, it will show here


exists :: Eq t => t -> [t] -> Bool  
exists val list = elem val list

listUnion :: Eq a => [a] -> [a] -> [a]
listUnion val1 val2 = removeDuplicates(val1 ++ val2) --function cateneates list and is used as a parameter for removeDuplicates
  where
  removeDuplicates:: Eq a=> [a] -> [a] -- seperate fucntion removes duplicates from list
  removeDuplicates (x:xs)
    | elem x xs = removeDuplicates xs
    | otherwise   = x : removeDuplicates xs

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
  | contains pre prereqs = course : prereqFor courses pre
  | otherwise = prereqFor courses pre
    where
      contains :: Eq t => t -> [t] -> Bool
      contains _ [] = False
      contains x (y:ys)
        | x == y = True
        | otherwise = contains x ys


main ::IO()
main = do 
  
    --Problem 1
    putStrLn (show (exists 4 [3,2,4,4,6,8]))
    putStrLn (show (exists 7 [3,2,4,4,6,8]))


    --Problem 2
    let dupeRemover = listUnion [1,3,5,6,7] [1,2,4,7,8,9]
    print dupeRemover
    let dupeRemover2 = listUnion "cpts355" "cpts377"
    print dupeRemover2


    --Problem 3
  



    --problem 4

    putStrLn (prereqFor [] "CptS355")
    print (prereqFor prereqsList "MATH216")
    print (prereqFor [("CourseA",["CptS355"]),("CourseB",[])] "CptS355")


    --problem 5


    --problem 6
    


    




    


