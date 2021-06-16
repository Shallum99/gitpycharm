try:
    from itertools import combinations
    from collections import Counter

    def cook(li):
        li.sort()
        n = len(li)
        if n==1:
            return li[-1]
        elif n==2:
            return li[-1]
        elif n==3:
            ok = combinations(li, 2)
            ol = []
            for i in ok:
                ol.append(sum(i))
            ol.sort()
            return ol[0]
        else:
            ok = combinations(li, 2)
            ol = []
            for i in ok:
                ol.append(sum(i))
            lol = dict()
            pl = sorted(list(set(ol)))
            if ol == pl:
                return min(ol)
            else:
                res = max(set(ol), key=ol.count)
                return res

    T = int(input())
    hah = []
    for i in range(T):
        input()
        li = list(map(int, input().rstrip().split()))
        aa = cook(li)
        hah.append(aa)
    for i in hah:
        print(i)
except:
    pass