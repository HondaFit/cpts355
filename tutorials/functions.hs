score :: Int
score = 30

sayHi :: IO ()
sayHi = putStrLn "Hello User"

sayHi2 :: IO ()
sayHi2 = do
  putStrLn "hello world"
  putStrLn "welcome to the united states"

sayHi3 :: String -> IO () --sayHi3 takes in a string as a parameter and returns something in the console
sayHi3 name = putStrLn ("Hello " ++name) -- functionName parameterTpyes = functionAction

sayHi4 :: String -> Int -> IO()
sayHi4 name age = putStrLn (name++ " Just turned "++show age)

main :: IO ()
main = do
  -- left side is the function name || --right side is what you want the function to do
  putStrLn "first"
  sayHi -- calling the sayHi function 
  sayHi2 -- you can also call the same function multiple times\
  sayHi3 "BobbyTheCoocker"
  sayHi4 "Alsex" 36 --multiple paramters are seperated by a space

  putStrLn "second"