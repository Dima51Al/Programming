l = 0
r = 0


def dell(s):
    return float(s.split("/")[0]) / float(s.split("/")[1])


def umn(s):
    return float(s.split("*")[0]) * float(s.split("*")[1])

s = "345/345*2+2*6*2"
while s.count("*") + s.count("/") > 0:
    if s[r] in "+-":
        r+=1
        l = r

    if s[r] == "/":
        r += 1
        while s[r] in "0123456789.,":
            r += 1
            if len(s) == r:
                break
        vir = dell(s[l:r])
        s = s[:l] + str(vir) + s[r:]
        print(s)
        r = 0
        l = 0
    if s[r] == "*":
        r += 1
        while s[r] in "0123456789.,":
            r += 1
            if len(s) == r:
                break
        vir = umn(s[l:r])
        s = s[:l] + str(vir) + s[r:]
        print(s)
        r = 0
        l = 0
    r+=1