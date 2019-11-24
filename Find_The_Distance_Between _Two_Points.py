import math

def distance(x1, y1, x2, y2):
    distPoint = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    roundedDist = round(distPoint,2)
    return roundedDist

print(distance(1,1,0,0))
# print(distance(3,7,2,8))
