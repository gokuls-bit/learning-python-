# py libs practised 
# lamda function 
# square = lambda x: x ** 2
# print(square(5))
# a=["hello", "world", "python", "is", "awesome"]
# final = "::".join(a)
# print(final)
#map filter
l = [1, 2, 3, 4, 5]

square = lambda x: x*x
sqlist = map(square, l)
print(list(sqlist))