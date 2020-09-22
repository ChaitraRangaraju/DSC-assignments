from collections import Counter

def gloves(n,ar):
    n = Counter(ar)
    return sum(i//2 for i in n.values())

n = input()
ar = list(map(int,input().split()))
print(gloves(n,ar))
