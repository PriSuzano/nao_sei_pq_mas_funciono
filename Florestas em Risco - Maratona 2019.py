n = int(input())

segmentos = {}
for i in range(n):
    segmentos[i] = list(map(int, input().split(' ')))

p = int(input())

nlogonia = list(map(int, input().split(' ')))

area_nlogonia = abs(nlogonia[0]-nlogonia[2])*abs(nlogonia[1]-nlogonia[3])

def intersect(a, b):

    x5 = max(a[0], b[0]) 
    y5 = max(a[1], b[1]) 

    x6 = min(a[2], b[2]) 
    y6 = min(a[3], b[3]) 

    if (x5 > x6 or y5 > y6) : 
        return None
    
    return x5, y5, x6, y6

rect = {}
r = 0
area = 0
while area < (area_nlogonia*p/100):
    r+=1
    for i in range(n):
        if segmentos[i][0]-r >= 0:
            x1 = segmentos[i][0] + r
        else:
            x1 = segmentos[i][0] - r

        if segmentos[i][1]-r >= 0:
            y1 = segmentos[i][1] + r
        else:
            y1 = segmentos[i][1] - r

        x2 = segmentos[i][2] + r
        y2 = segmentos[i][3] + r
        
        a = [x1, y1, x2, y2]

        rect[i] = intersect(a, nlogonia)

    area = 0
    rect_calc = list(rect.values())

    if len(rect_calc) == 1:
        area = abs(rect_calc[0][0]-rect_calc[0][2])*abs(rect_calc[0][1]-rect_calc[0][3])
    
    else:
        while len(rect_calc) > 1:
            
            a = rect_calc[0]
            del rect_calc[0]

            b = rect_calc[0]
            del rect_calc[0]

            area += abs(a[0]-a[2])*abs(a[1]-a[3])
            area += abs(b[0]-b[2])*abs(b[1]-b[3])

            resp = intersect(a, b)

            if resp != None:
                rect_calc.append(resp)
                area -= abs(resp[0]-resp[2])*abs(resp[1]-resp[3])
        
        if len(rect_calc) == 1:
            area -= abs(rect_calc[0][0]-rect_calc[0][2])*abs(rect_calc[0][1]-rect_calc[0][3])

print(r)