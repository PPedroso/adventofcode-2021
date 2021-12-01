file = open("02_input.txt","r")

values = file.readlines()
values = list(map(lambda n : int(n.strip()),values))

larger_values = 0



for index,value in enumerate(values):
    if(index > 2):
      if((value + values[index-1] + values[index-2]) > (values[index-1] + values[index-2] + values[index-3])):
        larger_values+=1

print("total",len(values))
print("larger than previous",larger_values)
