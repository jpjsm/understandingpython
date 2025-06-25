from queue import Queue


q = Queue(maxsize=0)
for i in range(10):
    q.put(i)

while not q.empty():
    print(q.get())

print("done")
