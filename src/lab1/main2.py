def algoritm(s):
    while s.count("(") + s.count(")") > 0:
        L = 0
        R = 0
        while s[R]!=")":
            R += 1
            if s[R] == "(":
                L = R
        print(s[L+1:R])
        s = ""
algoritm("123/(12+6)")