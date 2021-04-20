import pickle
import neuro
def fun(number_of_living = 10, aoi = 10, aoo = 2):
    a = []
    for i in range(number_of_living):
        a.append(neuro.Neuro(aoo, aoi))
    with open("memory.txt", "wb+") as f:
        pickle.dump(a, f)
        print("fu")
    with open("settings", "rb") as f:
        a = pickle.load(f)
    a = (a[0], a[1], a[2], 0, a[4])
    with open("settings", "wb+") as f:
        pickle.dump(a, f)
if __name__ == "__main__":
    fun(10, 10, 2)