from queue import Queue


q = Queue()
q.put('eat')
q.put('sleep')
q.put('code')

print(q)

print(q.get())
print(q.get())
print(q.get())
print(q.get_nowait())
print(q.get())
