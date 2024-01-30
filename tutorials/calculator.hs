import Distribution.Simple.GHC (getLibDir)
import Control.Arrow (Arrow(second))
import GHC.Base (VecElem(Int16ElemRep))
main = do 
    putStrLn "Enter your first number"
    firstString <- getLine
    putStrLn "Enter your second number"
    secondString <- getLine

    let firstNum = read firstString::Int
    let secondNum = read secondString::Int

    let total = firstNum + secondNum

    putStrLn ("Your total is "++show total)
    

