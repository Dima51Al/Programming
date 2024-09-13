


def dell(s):
    return float(s.split("/")[0]) / float(s.split("/")[1])


def umn(s):
    return float(s.split("*")[0]) * float(s.split("*")[1])

def summ(s):
    return float(s.split("+")[0]) + float(s.split("+")[1])
def minus(s):
    return float(s.split("-")[0]) - float(s.split("-")[1])


def mega(s):
    l = 0
    r = 0
    while s.count("*") + s.count("/") > 0:

        if s[r] in "+-":
            r += 1
            l = r

        if s[r] == "/":
            r += 1

            if s[r]=="-":
                r+=1

            while s[r] in "0123456789.,":
                r += 1
                if len(s) == r:
                    break
            vir = dell(s[l:r])
            s = s[:l] + str(vir) + s[r:]

            r = 0
            l = 0
        if s[r] == "*":
            if s[r]=="-":
                r+=1
            r += 1
            while s[r] in "0123456789.,":
                r += 1
                if len(s) == r:
                    break
            vir = umn(s[l:r])
            s = s[:l] + str(vir) + s[r:]

            r = 0
            l = 0
        r += 1
    while (s.count("+") + s.count("-")-s[0].count("-")) > 0:

        if s[r] == "-":
            r += 1
            while s[r] in "0123456789.,":
                r += 1
                if len(s) == r:
                    break
            vir = minus(s[l:r])
            s = s[:l] + str(vir) + s[r:]

            r = 0
            l = 0
        if s[r] == "+":
            r += 1
            while s[r] in "0123456789.,":
                r += 1
                if len(s) == r:
                    break
            vir = summ(s[l:r])
            s = s[:l] + str(vir) + s[r:]

            r = 0
            l = 0
        r += 1
    return s


def algoritm(s):
    while s.count("(") + s.count(")") > 0:
        L = 0
        R = 0
        while s[R]!=")":
            R += 1
            if s[R] == "(":
                L = R
        vir = mega(s[L+1:R])
        s = s[:L] + str(vir) + s[R+1:]
    return mega(s)



print(algoritm(input()))


