import Text.Parsec (putState)



main = do 
    putStrLn "Please enter your name: "
    name <- getLine -- "<-" take the value of the right side and store it into name. "getline" gets input from user
    putStrLn ("Your name is: "++name++".")

    putStrLn "Enter your age"
    age <- getLine
    putStrLn("Name: "++name++" || Age: "++age)

    let ageNum = read age::Int -- read is like a type cast. let newVariable = read (variable you want to convert)::(the type you want to convert it int, char, etc)

    let newAge = ageNum + 10
    putStrLn ("In 10 years you will be "++ show newAge)




    

