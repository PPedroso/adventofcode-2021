file = open("01_input.txt","r")

values = file.readlines()
values = list(map(lambda n : int(n.strip()), values))

larger_values = 0

for index,value in enumerate(values):
    if(index > 0 and value > values[index-1]):
        larger_values+=1

print("total",len(values))
print("larger than previous",larger_values)
