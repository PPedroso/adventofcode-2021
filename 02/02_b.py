file = open("02_input.txt","r")

values = file.readlines()
values = list(map(lambda n : (n.strip()).split(), values))


horizontal = 0
depth = 0
aim = 0

for value in values:
    command = value[0]
    command_value =int(value[1]) 
    
    if command == 'forward':
        horizontal+=command_value
        depth+=aim*command_value
    if command == 'up':
        aim-=command_value
        if aim < 0:
            aim = 0
    if command == 'down':
        aim+=command_value
           
print("Horizontal:", horizontal)
print("Depth:", depth)
print("Aim:", aim)
print("Horizontal * Depth:", horizontal * depth)
