main = do 
    putStrLn "Please enter your name: "
    name <- getLine -- "<-" take the value of the right side and store it into name. "getline" gets input from user
    putStrLn ("Your name is: "++name++".")
