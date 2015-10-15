import math

def project_to_distance(point_x,point_y,distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale

print project_to_distance(2, 7, 4)

print (1.0 / 4) * 7 * (3 ** 2) / math.tan(math.pi / 7)
print (1.0 / 4) * 5 * (7 ** 2) / math.tan(math.pi / 5)

def max_of_2(a, b):
    if a > b:
        return a
    else:
        return b

def max_of_3(a, b, c):
    return max_of_2(a, max_of_2(b, c))