def faci(n):
    result = 1
    while n > 1:
        result = n * result
        n -= 1
    return result


def facr(n):
    if n == 1:
        return n
    return n * facr(n - 1)


def fib(n):  # wrong wrong wrong
    result = 1
    while n > 0:
        result = n + n - 1
        n -= 1
    return result


def fibr(n):
    if n == 0 or n == 1:
        return 1
    return fibr(n - 1) + fibr(n - 2)

# print faci(4)
# print facr(4)

# print fib(6)
# print fibr(6)

class B:
    pass
class C(B):
    pass
class D(C):
    pass

for c in [B, C, D]:
    try:
        raise c()
    except D:
        print "D"
    except C:
        print "C"
    except B:
        print "B"

for element in [1, 2, 3]:
    print element
for element in (1, 2, 3):
    print element
for key,val in {'one':1, 'two':2}.iteritems():
    print key, val
for char in "123":
    print char
for line in open("myfile.txt"):
    print line,
