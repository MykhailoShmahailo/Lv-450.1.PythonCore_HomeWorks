def enough(cap,on,wait):
    if (cap-on) > wait:
        print(cap-on - wait)
    elif (cap-on) == wait:
        print("0")
    else:
        print(cap-on) 
 
 
 
 print(enough(100, 60, 50))