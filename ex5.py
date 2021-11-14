def square(param):
    new_list = list(map(lambda x: x**2,param))
    new_list = list(filter(lambda x: x<=50, new_list))
    return new_list
print(square([7,8,5,3,2,1,6,8]))