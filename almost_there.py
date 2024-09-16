def almost_there(n):
    return (abs(100-n)<=10)or(abs(200-n)<=10)
# check
print(almost_there(104))
# check
print(almost_there(150))
# check
print(almost_there(209))