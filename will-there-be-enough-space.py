def enough(cap, on, wait):
    esp = on + wait - cap
    if esp < 0:
        esp = 0        
    return esp

print(enough(100,50,181))    