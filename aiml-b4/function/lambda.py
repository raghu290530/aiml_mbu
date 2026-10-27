# def sqr(n):
#     return  n*n

sqr = lambda n:n*n
print(sqr(5))
print(sqr(10))

add = lambda a,b : a+b
print(add(5,6))

isEven = lambda n : n%2==0
print(isEven(5))
print(isEven(6))

#map, filter, sorted
li = [2,3,5,9,4,8,5,2]
# resut = list(map(lambda e:e*2,li))
resut = list(map(lambda e:e*2,li))
print(resut)

#filter
resut = list(filter(lambda e:e%2==0,li ))
# resut = list(filter(lambda e:e%2==0,li ))
print(resut)
