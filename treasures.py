
import random
def treasures(N):
    treasur_idx = random.randint(0,N-1)
    arr = list(map(lambda x: x,range(N)))
    arr.pop(treasur_idx)
    random.shuffle(arr)
    arr = list(map(lambda x: -x if x>treasur_idx else x,arr))
    arr.insert(treasur_idx,"T")
    #print(str(treasur_idx)+ "T at")
    return arr
