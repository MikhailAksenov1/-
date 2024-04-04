a = input()
x = a.split(' ')
e = []
for i in range(len(x)):
  if len(x) == 1:
    print(x[i])
  elif i == 0:
    e.append(int(x[i+1]) + int(x[-1]))
  elif i ==len(x)-1:
    e.append(int(x[i-1]) + int(x[0]))
  else:
    e.append(int(x[i-1]) + int(x[i + 1]))
print(' '.join(str(x) for x in e))
