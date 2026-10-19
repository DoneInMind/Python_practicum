def getDict(s):
    m = {}
    for word in s.split():
        m[word] = m.get(word, 0) + 1
    for word, cnt in m.items():
        print(word, cnt)

getDict(input())
