my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
variable = 0
while variable <= len(my_list):
    if my_list[variable] > 0:
        print(my_list[variable])
    if my_list[variable] <= -1:
        print('This is the end')
        break
    variable += 1

