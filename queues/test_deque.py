# using collections.desque as a FIFO queue

from collections import deque
q1 = deque()

q1.append('eat')
q1.append('sleep')
q1.append('code')

print(q1)

q1.popleft()
q1.popleft()
print(q1)