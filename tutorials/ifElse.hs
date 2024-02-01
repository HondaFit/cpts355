import Distribution.Simple.Setup (trueArg)

travelToWork :: String -> IO()
travelToWork weather = do 
    if weather == "sunny"
        then putStrLn "walking to work"
    else if weather == "cloudy" 
        then putStrLn "bike to work"
        else putStrLn "drive to work"


travelToWork2 ::String -> Bool -> IO()
travelToWork2 weather isRaining = do
    if weather == "cloudy" && isRaining --and logic. Both must be true
        then putStrLn "drvie to work"
        else putStrLn "walk to work"


travelToWork3 ::String -> Bool -> IO()
travelToWork3 weather isRaining = do --one or the other must be true
    if weather == "cloudy" || isRaining
        then putStrLn "drvie to work"
        else putStrLn "walk to work"

main::IO()
main = do 
    travelToWork "sunny"
    travelToWork "rainy"
    travelToWork "cloudy"

    putStrLn ""

    let isRaining = False
    travelToWork2 "cloudy" isRaining

    putStrLn ""

    travelToWork3 "cloudy" isRaining


