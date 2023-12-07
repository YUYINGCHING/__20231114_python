import math
def circle_area(r):
    a = r**2*math.pi
    return a

import pyinputplus as pyip
radius1 = pyip.inputFloat("請輸入半徑")
print(radius1)
area = circle_area(radius1)
print(f"半徑{radius1},園面積是{area}")
