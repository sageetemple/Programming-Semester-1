def mystery(n, a, d):
   if n == 1:
       return a
   else:
       return d + mystery(n -1, a, d)
print(mystery(3,2,6))
