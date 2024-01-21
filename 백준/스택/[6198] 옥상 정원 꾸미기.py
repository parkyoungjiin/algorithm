buildings = []
for i in range(int(input())): buildings.append(int(input()))
stack = []
result = 0

while buildings:
  b = buildings.pop()

  for i in range(1,len(stack)+1):
    s = stack[len(stack)-i]
    
    if s<b:
      if buildings and max(buildings)<=b:
        stack.pop(len(stack)-i)
      result += 1
    else:
      break

  stack.append(b)

print(result)