import dis


doublelt = lambda x: x*2

print(doublelt(5))

def doubeltfunc(x):
    return x*2


print(doublelt)
print(dis.dis(doublelt))

print(doubeltfunc)
print(dis.dis(doubeltfunc))


my_list = [1, 5, 4, 6 ,8 ]

newlist = filter( lambda x: (x%2 == 0)  , my_list)
newlist = list(newlist)

print(newlist)