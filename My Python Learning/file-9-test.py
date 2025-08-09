def chai(num):
    def actual(x):
        return x * num
    return actual

f = chai(2)
g = chai(3)

print(f(2))
print(g(4))