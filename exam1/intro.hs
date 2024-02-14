main = putStrLn "Hello, world!"
{- Basic "Hello World" program using "main" function and "putStrLn" to print.
   "putStrLn" adds a trailing newline character to the printed string. 
-}

main = do {- do-notation allowing series of I/O actions (imperitive style) -}
  putStrLn "What is 4 * 5?" -- Print a prompt
  x <- readLn -- Read text input and bind it to x. readLn has return/bind action
  if x == 20  -- if-conditional will evaluate and branch based on condition
    then putStrLn "You're right!" -- Branch if condition is true
    else putStrLn "You're wrong!" -- Branch if false

x :: Integer -- {- Type declaration using :: -} 
x = (1 :: Integer) + (1 :: Integer) :: Integer {- Explicit integer literals 
   needed, default numeric type is fracional in Haskell-}

   
x = 2 {- Defines binding x to value 2 -}
y = 3

addOne arg = 1 + arg {- Function definition - takes one arg, returns arg+1 -}
four = addOne 3 -- {- Function application - binds result of addOne 3 to four -}

add arg1 arg2 = arg1 + arg2 -- {- Defines function add taking two arguments -}
five = add 2 3 {- Applies add function - binds result to name five -}




-- Function definition with type signature  
double :: Integer -> Integer
double x = 2*x

-- Tuple example
myTuple :: (Bool, Integer, String) 
myTuple = (True, 1, "one")

-- List examples
primes = [2, 3, 5, 7, 11] -- List of integers
chars = ['a', 'b', 'c'] -- List of chars is a string

-- List comprehension - generates list of cubes 
cubes = [x^3 | x <- [1..10]]  

-- Recursive factorial function
factorial n = if n > 1 
              then n * factorial (n-1)
              else 1


-- Binding examples
x = 2 
y = 3
z = x + y -- z binds to 5

-- Multi-line function definition
average :: Float -> Float -> Float 
average a b = (a + b) / 2.0

-- Safe division function  
safeDiv x y = 
  let q = div x y  
  in if y == 0 then 0 else q

-- Tuple functions
swap :: (Integer, String) -> (String, Integer)
swap (x,y) = (y,x) 

strPair :: Integer -> (Integer, String)  
strPair x = (x, show x)

-- List indexing
nums = [1, 2, 3]  
nums !! 0 -- Returns 1

-- List append
[1,2,3] ++ [4,5] -- Returns [1,2,3,4,5]  

-- List functions 
head [1,2,3] -- Returns 1
tail [1,2,3] -- Returns [2,3]
length [1,2,3] -- Returns 3

-- Recursive Fibonacci 
fib 0 = 0
fib 1 = 1  
fib n = fib (n-1) + fib (n-2)