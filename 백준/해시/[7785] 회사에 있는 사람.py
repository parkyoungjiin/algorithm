import sys
input = sys.stdin.readline

n = int(input())

enter_log = {}
for _ in range(n):
    name, log = input().split()

    if enter_log.get(name) == None:
        enter_log[name] = log
    
    else:
        if enter_log[name] == "enter":
            enter_log[name] = "leave"
        else:
            enter_log[name] = "enter"
name_list = []
for name, log in enter_log.items():
    if log == "enter":
        name_list.append(name)
name_list = sorted(name_list, reverse=True)

for name in name_list:
    print(name)