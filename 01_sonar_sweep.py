file = open("01_input.txt","r")

values = file.readlines()

larger_values = 0

for index,value in enumerate(values):
    if(index > 0 and int(value.strip()) > int(values[index-1].strip())):
        larger_values+=1
print(values)
print("total",len(values))
print("larger than previous",larger_values)
