print("*** Fun with permute ***")
inputall= input("input : ").split(",")

results = list(map(int, inputall))

print("Original Cofllection: ",results)

source = [[]]

for i in results:
  new_source = []

  for j in source:
    
    for k in range(len(j)+1):
      new_source.append(j[:k] + [i]+ j[k:])
      source = new_source
      

print("Collection of distinct numbers:\n",source)

