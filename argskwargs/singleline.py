

print((lambda x: x + 3)(3))
'''
func lambda(x):
    return x+3

lambda(3)

'''

# [ expression + context ]

print([i**2 for i in range(10) if i%2==0])

print([i**2 for i in range(10)])


print([(x, y) for x in range(3) for y in range(3)])

print([x.lower() for x in ['I', 'AM', 'NOT', 'SHOUTING']])

employees = {'Alice' : 100000,
             'Bob' : 99817,
             'Carol' : 122908,
             'Frank' : 88123,
             'Eve' : 93121}

top_earners = [(k, v) for k, v in employees.items() if v >= 100000]


print(top_earners)

text = '''
Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''

w = [[x for x in line.split() if len(x)>3] for line in text.split('\n')]

print(w)


# all values are true
lis1 = [10, 20, 30, 40]
print(any(lis1))

# all values are false
lis2 = [0, False]
print(any(lis2))


print("------")
print([i**2 for i in range(10) if i%2==0])

print([i for i in range(10) if i%2==0 and i>3])