import pickle
def fun(size = 10, number_of_living = 10):
    for i in range
    with open("memory.txt", "wb+") as f:
        pickle.dump(a, f)
    with open("settings", "rb") as f:
        a = pickle.load(f)
    a = (a[0], a[1], a[2], 0, a[4])
    with open("settings", "wb+") as f:
        pickle.dump(a, f)
if __name__ == "__main__":
    fun(10, 10)