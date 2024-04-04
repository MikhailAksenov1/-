def modify_list(l):
    for i in range(-len(l),0):
          if l[i] % 2 == 0:
            l[i] = l[i]//2
          else:
            l.remove(l[i])
