immutable_var = 1, 2, 3, 4, 'a', 'b'
print(immutable_var)
immutable_var = ([1, 2, 3, 4], 'a', 'b')
print(immutable_var)
immutable_var [0][1] = 3 #В отличие от списков кортежи неизменяемы. Но если кортеж внутри себя хранит список (изменяемые объекты), то в таком случае можно изменить элемент внутри кортежа.
print(immutable_var)
mutable_list = [1 , 2, 3, 4, 'a', 'b', 'c']
mutable_list[2] = 'run'
print(mutable_list)
