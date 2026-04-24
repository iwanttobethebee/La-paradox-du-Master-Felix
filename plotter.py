from treasures import treasures
from solution_hard import solution_hard
from jump_find import jumping
import matplotlib.pyplot as plt 

jump_On =[]
hard_On =[]
for n in range(1,1000,1):
    print(n)
    jump_On.append(sum(list(map( lambda iter: jumping(treasures(n)), range(100))))/100) #average on 1k tries
    hard_On.append(sum(list(map( lambda iter: solution_hard(treasures(n)), range(100))))/100)
    
plt.scatter(list(range(1,1000)), jump_On)
plt.scatter(list(range(1,1000)), hard_On)

plt.savefig("test.png")