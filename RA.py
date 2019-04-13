#Ricart-Agrawala

from random import choice
from random import random
import time

class Process:
    def __init__(self, name, ts,wants_to_go, is_inside=False):
        self.name = name
        self.ts = ts
        self.wants_to_go = wants_to_go
        self.is_inside = is_inside
        
    def __lt__(self,Process):
        return self.ts < Process.ts

    def print_process(self):
        res = "Process " + str(self.name)
        temp = [" does not want to go", " wants to go, ", " is not inside critical section", " is inside critical section"]
        if self.wants_to_go and self.is_inside:
            res += temp[1] + temp[3]
        elif self.wants_to_go == False:
            res += temp[0]
        else:
            res += temp[1] + temp[3]
        res += " and has timestamp  " + str(self.ts)
        return res

    def __str__(self):
        res = str(self.name)
        return res
    
def remove_process_index(queue,process):
    c = 0
    for i in queue:
        if i.name == process.name:
            return c
        c += 1
        
choices = [True,False]
p = list()

for i in range(8):
    p.append(Process(i,random(),choice(choices)))
p[1].wants_to_go, p[1].is_inside = True, False

print("Processes\t\tWants to go\tInside CS\t\tTimestamp")
for process in p:
    print(str(process.name) + "\t\t" + str(process.wants_to_go) + "\t\t " + str(process.is_inside) + "\t\t" + str(process.ts))

p_true = [i for i in p if i.wants_to_go]

cs = [p[1]]
print("Currently in CS: ", cs[-1].name)

queue = []
p_true.pop(remove_process_index(p_true,cs[-1]))

while p_true:
    for i in p:
        if i not in cs and i.wants_to_go == True:
            queue.append(i)

    queue = sorted(queue)
    queue_names = [i.name for i in queue]

    print("Queued Processes: ", queue_names)
    print("Next to go to CS: ", min(queue))
    time.sleep(1)
    print("Process " + str(cs[-1]) + " has come out of CS")
    cs[-1].wants_to_go = False
    cs = [min(queue)]
    queue = list()
    p_true.pop(remove_process_index(p_true,cs[-1]))
    print("Currently in CS: ",cs[-1])    
    print("\n")
