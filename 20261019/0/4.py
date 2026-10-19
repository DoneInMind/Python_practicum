from collections import Counter

def getDict(s):
    for word, cnt in Counter(s.split()).items():
        print(word, cnt)

getDict(input())
