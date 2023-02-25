def count_chars(arg):
    lst = [(i, arg.count(i)) for i in arg if arg.count(i) > 1]
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list


string = 'heljhhghjhhgyppouuytlo'
print(count_chars(string))

