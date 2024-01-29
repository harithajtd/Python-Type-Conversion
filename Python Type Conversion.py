#PYTHON TYPE CONVERSION

#1.PYTHON IMPLICIT TYPE CONVERSION

#Converting integer to float
integer=123
float_num=12.3

new_num=integer+float_num
print(new_num)
print('Data type:',type(new_num))

'''____________________________________________________'''



#2.EXPLICIT TYPE CONVERSION

num_str='15'
num_int=15
print('Data type of num_str before tpe casting:',type(num_str))

#Explict_conversion
num_str=int(num_str)

num_sum=num_str+num_int
print('Sum:',num_sum)
print('Data type of num_sum:',type(num_sum))
