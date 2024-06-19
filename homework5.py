immutable_var=(1,2,['a',3],'room')
print(immutable_var)
immutable_var[2][1]=5
print(immutable_var)
#immutable_var[0]=4 # кортеж является неизменяемым объектом, но списки, входящие в кортеж, менять можно.
mutable_list=[6,7,'x','y','green']
print(mutable_list)
mutable_list[4]='red'
print(mutable_list)