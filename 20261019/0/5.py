from collections import Counter

print(*(word for word, cnt in Counter(input().split()).items()))
