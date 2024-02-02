exists :: Eq t => t -> [t] -> Bool  
exists val list = elem val list


main::IO()
main = do 
    print (exists 10 [5,5,2,7,9,4,1])

