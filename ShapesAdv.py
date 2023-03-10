import math

distance = float(input("친구와 당신의 거리는 얼마입니까? (m) "))
speed = float(input("당신이 던진 공의 속력은 얼마입니까? (m/s) "))
tolerance = 2
for i in range(0, 91):
    angle_r = math.radians(i)
    reach = 2 * speed ** 2 * math.sin(angle_r) * math.cos(angle_r) / 9.8
    if reach > distance - tolerance and reach < distance + tolerance:
        print("나이스 피치!")
    elif reach < distance - tolerance:
        print("충분히 멀리 던지지 못했습니다.")
    else:
        print("너무 멀리 던졌습니다.")