import random

act_str = '''Independence Day
Children's Day
Repbulic Day'''
act_list = []
percent_list = [0]
add = 0

for act in act_str.split('\n'):
    act_list.append(act)

while True:
    for act in act_list:
        percent = random.randint(5, 50)
        percent_list.append(percent)

    for j in range(0, len(percent_list)): 
        add = add + percent_list[j]

    if add == 100:
        break
    else:
        add = 0
        percent_list = [0]

percent_list.pop(0)
print(percent_list)
