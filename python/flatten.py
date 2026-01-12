x = [1,2,[3,4],5,6,[7,8],9]
res = []
for i in x:
    if isinstance(i, list):
        for item in i:
            res.append(item)
    elif isinstance(i, int):
        res.append(i)

print(res)
