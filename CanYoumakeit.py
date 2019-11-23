# https://www.codewars.com/kata/will-you-make-it/train/python

# Variant 1

fuel = int(input("Enter how many fuel you have "))
distance = int(input("Enter how long distance you have to go "))
fuelconsuming = int(input("Enter fuel consuming "))

def rangefuel():
    if (distance / fuelconsuming) == fuel:
        return True
    elif (distance / fuelconsuming) < fuel: 
        return True   
    else:  
        return False

print(rangefuel())

# Variant 2

def rangefuel(fuel,distance,fuelconsuming):
    if (distance / fuelconsuming) == fuel:
        return True
    elif (distance / fuelconsuming) < fuel: 
        return True   
    else:  
        return False
    
print(rangefuel(3,50,25))


