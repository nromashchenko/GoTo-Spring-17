d = {"emotion1": 40, "emotion2": 30}


lst = list(d.items())
lst = sorted(lst, key=lambda x:x[1], reverse=True)
print(lst[0][0])