import math
def tinh_bmi (can_nang, chieu_cao) :
    bmi=can_nang/math.pow(chieu_cao,2)
    return bmi
bmi=tinh_bmi(49,1.58)
print("bmi:",bmi)

