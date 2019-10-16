from math import radians,degrees,cos,sin,acos

def distance_finder(latitude_1,longitude_1,latitude_2,longitude_2):
    latitude_1 = radians(latitude_1)
    latitude_2 = radians(latitude_2)
    longitude_difference = radians(longitude_1 - longitude_2)

    distance = (sin(latitude_1)*sin(latitude_2)+cos(latitude_1)*cos(latitude_2)*cos(longitude_difference))

    resToMile = degrees(acos(distance)) * 69.09
    resToMt = resToMile / 0.00062137119223733
    restokm = resToMt / 1000
    return restokm


print(distance_finder(70,5,5,5))
