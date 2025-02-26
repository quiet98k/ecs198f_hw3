def foo_bar_baz(n: int) -> str:
    return_str = ""
    for i in range(1, n + 1, 1):
        if (i % 3 == 0) and (i % 5 == 0):
            return_str += "Baz"
        elif i % 3 == 0:
            return_str += "Foo"
        elif i % 5 == 0:
            return_str += "Bar"
        else:
            return_str += str(i)
        if i < n:
            return_str += " "
    return return_str

# for i in range(-10, 1001):
#     print(foo_bar_baz(i))