calculate:: Double -> String -> Double -> IO()
calculate firstNum operator secondNum = do
    if operator == "+"
        then print (firstNum + secondNum)
    else if operator == "-"
        then print (firstNum - secondNum)
    else if operator == "/"
        then print (firstNum/secondNum)
    else if operator == "*"
        then print (firstNum*secondNum)
    else putStrLn "invalid operator or numbers"


main :: IO ()
main = do
    putStrLn "Enter first number: "
    firstStr <- getLine
    putStrLn "Enter an operator: "
    operator <- getLine
    putStrLn "Enter second Number: "
    secondStr <- getLine
    let firstNum = read firstStr::Double
    let secondNum = read secondStr::Double

    calculate firstNum operator secondNum


