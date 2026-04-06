num = [1,2,3,4,5,6,7,8,9,10]
even_num = [n for n in num if n % 2 == 0]
print(even_num)

fruits = ["apple","banana","cherry"]
len_fruits = [len(fruit) for fruit in fruits]
print(len_fruits)

numbers = [1,2,3,4,5]
squared = [num ** 2 for num in numbers if num > 3]
print(squared)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cubed = list(map(lambda x: x ** 3 , nums))
grea_5 = list(filter(lambda x: x > 5 , nums))
grea_r_cubed = list(map(lambda x: x ** 3,filter(lambda x: x > 5 , nums)))
print(cubed)
print(grea_5) 