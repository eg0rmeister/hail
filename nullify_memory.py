import pickle
size = 10
a = [[[[0 for i in range(size)] for j in range(size)] for k in range(2)] for _ in range(10)]
for i in range(10):
    a[i].append([[0 for i in range(size)] for j in range(2)])
print(a[0][1])
with open("memory.txt", "wb+") as f:
    pickle.dump(a, f)
with open("settings", "rb") as f:
    a = pickle.load(f)
a = (a[0], a[1], a[2], 0, a[4])
with open("settings", "wb+") as f:
    pickle.dump(a, f)