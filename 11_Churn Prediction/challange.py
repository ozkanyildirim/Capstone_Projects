def paren(left, right=None):
    if right is None:
        right = left  # allows calls with one argument

    if left == right == 0: # base case
        yield ""

    else:
        if left > 0:
            for p in paren(left-1, right): # first recursion
                yield "("+p

        if right > left:
            for p in paren(left, right-1): # second recursion
                yield ")"+p
a = [v for v in paren(5)]
print(a)

n=3
lst = [i for i in range(1, n*2+1)]
p = [[]]
c= []
d= []
e =[]
for i in range(len(lst)):
    p = [[a] + b for a in lst for b in p if a not in b]
for j in p:
    if j[0] == lst[0] and j[-1] == lst[-1]:
        c.append(j)
for i in c:
    for j, k in enumerate(i):
        if k % 2 == 0:
            i[j] = ")"
        else:
            i[j] = "("
for k in c:
    for j in range(len(lst)):
        if "".join(k) not in d and k[:j].count("(") < k[:j].count(")"):
            d.append("".join(k))
        elif "".join(k) not in e:
            e.append("".join(k))
for i in d:
    e.remove(i)
print(e)
