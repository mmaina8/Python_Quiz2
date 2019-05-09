def list(numbers):
	number_list=[number%3 for number in numbers]
	return number_list

def sorted (a,b,c):
	sum = a+b+c
	sum.sort()
	return sum

def divisible_by_three(n):
	numbers = range (1,n+1)
	all_numbers = (numbers/3)
	print (all_numbers)

def nest(x):
	for s in x:
		for a in s:
			print (a)

def smallest(list):
	return min(list)

def duplicate(list):
	list = set (['a','b','a','e','d','b','c','e','f','g','h'])
	return list

def squares():
	s = dict ()
	numbers= range(149,159)
	for number in numbers:
		s[number] = [number*number]
		print (s)

def greet():
	student1 = {'age': 19, 'name': 'Eunice'}
	student2 = {'age': 21, 'name': 'Agnes'}
	student3 =  {'age': 18, 'name': 'Teresa'}
	student4 = {'age': 22, 'name': 'Asha'}
	students = [student1,student2,student3,student4]
	
	for student in students:
		year = 2019-student['age']
		print ("Hello {}, you were born in year {}.".format(student['name'],year))



