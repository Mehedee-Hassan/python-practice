from collections import deque


dq = deque()
dq.append(1)
dq.append(12)
dq.append(13)
dq.append(14)

dq.appendleft(23)

# for a in dq:
# 	print(a)
print(dq[2])

print(dq)
