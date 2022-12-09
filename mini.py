def findangle(inp):
    inp[0]=inp[0]%12
    h=(inp[0]*360)//12+(inp[1]*360)//(12*60)
    m=(inp[1]*360)//(60)
    angle=abs(h-m)
    if angle>180:
        angle=360-angle
    return angle
inp=[int(x) for x in input('Hour:Minutes = ').split(':')]
print('Angle between hour hand and minute hand =',findangle(inp))

