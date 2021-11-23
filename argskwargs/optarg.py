def func1(p1,p2):
    print(p1)
    print(p2)


def func2(*args):
    for v1 in args:
        print(v1)

def func3(p1,p2,*args):
    print(p1)
    print(p2)
    for v1 in args:
        print(v1)
    
def func4(*args):
    print(len(args))
    for i in range(len(args)):
        print(args[i])

def func5(**kwargs):
    for key,value in kwargs.items():
        print(key)
        print(value)

func1("a1","a2")
print("--------")
my_array = ["q1","q2","q3","q4"]
print("--------")
func2("b1","b2","b3")
print("--------")
func2(*my_array)
print("--------")
func3("s1","s2",*my_array)
print("--------")
func3(*my_array)
print("--------")
func4(my_array)
print("--------")
dumps = {"key1":"value1","key2":"valu2"}
func5(**dumps)
print("--------")
func5(k1="v1",k2="v2")