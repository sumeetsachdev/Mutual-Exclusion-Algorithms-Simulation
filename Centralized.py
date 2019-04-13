from random import randint
import time

process = [i for i in range(8)]
queue = list()
message_count = 0

coord = randint(min(process),max(process))
print("Co-ordinator is ", coord)
print("\n")
process.pop(process.index(coord))

process_in_cs = randint(min(process), max(process))
critical_section = [process_in_cs]
print("Currently in CS: ", critical_section[-1])
process.pop(process.index(process_in_cs))

while process:
    print("Sending the message to co-ordinator...")
    time.sleep(1)
    print(str(critical_section[-1]) + " has come out of critical section")
    critical_section = list()
    queue = []
    for p in process:
        if len(critical_section) == 0:
            print("Access granted by co-ordinator. Process entering critical section...")
            critical_section.append(p)
            message_count += 2                                  #one message request to co-ordinator and one confirmation from co-ordinator
            print("Currently in CS: ", critical_section[-1])
        else:
            if p not in queue:
                queue.append(p)
            message_count += 1                                  #one message request to co-ordinator and no confirmation from coordinator
    process.pop(process.index(critical_section[-1]))
    print("Queued Processes: ",queue)
    print("\n")

print(message_count)
