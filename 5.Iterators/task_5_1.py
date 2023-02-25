# Реализуйте цикл, который будет перебирать все значения итерабельного объекта iterable.

digit_box = list(range(20))
iterable_ = iter(digit_box)

for item in range(len(digit_box)):
    print(next(iterable_), end=' ')
print()
for item in digit_box:
    print(item, end=' ')
