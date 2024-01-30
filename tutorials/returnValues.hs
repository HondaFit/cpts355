cube :: Int -> Int
cube num = num * num * num

sayHi :: String -> String
sayHi name = "Hello "++name --remember your are not printing string to the console but rather you are returning "Hello name"

main :: IO ()
main = do
    let result = cube 3
    print result

    putStrLn (sayHi "Joey")

    let userName = sayHi "JoeyMama"
    putStrLn userName


    
