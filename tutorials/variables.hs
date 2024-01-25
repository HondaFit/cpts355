import Text.Parsec (putState)
main = do
    let name = "Dudley"
    putStrLn (name ++" was a bad child")
    putStrLn (name ++" was a good child")
    putStrLn (name ++" ate a lot of food")
    putStrLn (name ++" got in trouble today. " ++ name ++ "is going to get scollded by his parents")
-- to comment use "--"
-- to have a coment block open with "{-" and end with "-}"

    --YOU CANNOT PRINT INTEGERS YOU NEED TO CONVERT THEM INTO STRINGS
    print 36 --you cannot use putStrLn to print an integer use "print" instead
    putStrLn (show 36) -- shows an integer as a string

    let numOfGifts = 30

    putStrLn ("Today was "++name++" birthday he recieved "++show numOfGifts++ " gifts") -- in order to print integers to the console you need to use "show"

    let name2 = "fred"

    putStrLn (name2++ "and " ++name++ "got into a fight resulting in " ++show numOfGifts++ " deaths")

    


    

