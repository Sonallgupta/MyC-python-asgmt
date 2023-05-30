dict = {}

def most_frequent(s):
    for i in s:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    return dict


res = most_frequent("mississippi")
for keys in sorted(res, key=res.get, reverse=True):
    print(keys, "=", res[keys])
