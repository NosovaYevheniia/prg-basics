results = [37,51,44,23,78,92,39,84,83,51]

def min_pts(limit):
   return lambda pts: pts>=limit

tuberkulez = list(filter(lambda x: x > 70, results))
print(f"{tuberkulez}")
tif = list(filter(lambda y: y > 40, results))
print(tif)
cinga = list(filter(lambda z: z  > 30, results))
print(cinga)