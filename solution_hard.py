from treasures import treasures

#O(n)
def solution_hard(arr):
    count = 0
    for n in arr:
        count+=1
        if n =="T": return count
