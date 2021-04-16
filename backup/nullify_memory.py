import pickle
def fun(size, number_of_living):
    size = 10
    a = [[[[0 for i in range(size)] for j in range(size)] for k in range(2)] for _ in range(number_of_living)]
    for i in range(number_of_living):
        a[i].append([[0 for i in range(size)] for j in range(2)])
    print(a[0][1])
    with open("memory.txt", "wb+") as f:
        pickle.dump(a, f)
    with open("settings", "rb") as f:
        a = pickle.load(f)
    a = (a[0], a[1], a[2], 0, a[4])
    with open("settings", "wb+") as f:
        pickle.dump(a, f)
if __name__ == "__main__":
    fun(10, 10)