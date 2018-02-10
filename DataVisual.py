"""
6.7 Program: Data visualization (Python 3)
"""
#1
data_title = input('Enter a title for the data: \n')
print('You entered: %s' % data_title + '\n')

#2
column_1 = input('Enter the column 1 header: \n')
print('You entered: %s' % column_1 + '\n')
column_2 = input('Enter the column 2 header: \n')
print('You entered: %s' % column_2 + '\n')

#3 & 4
str_list = []
int_list = []
data_point = input('Enter a data point (-1 to stop input): \n')
while data_point != '-1':
	while ',' not in data_point:
		print('Error: No comma in string.\n')
		data_point = input('Enter a data point (-1 to stop input): \n')

	while data_point.count(',') > 1:
		print('Error: Too many commas in input.\n')
		data_point = input('Enter a data point (-1 to stop input): \n')
	data_str = data_point.split(',')[0]
	data_int = data_point.split(',')[1].strip()
	while data_int.isdigit() == False:
		print('Error: Comma not followed by an integer.\n')
		data_point = input('Enter a data point (-1 to stop input): \n')
		data_str = data_point.split(',')[0]
		data_int = data_point.split(',')[1].strip()
	print('Data string: %s' % data_str)
	print('Data integer: %d' % int(data_int))
	str_list.append(data_str)
	int_list.append(data_int)
	print()
	data_point = input('Enter a data point (-1 to stop input): \n')

#5
print()
print('%33s' % data_title)
print('%(c1)-20s|%(c2)23s' % {'c1': column_1, 'c2': column_2})
print('-' * 44)

index = 0
for author in str_list:
	print('%(c1)-20s|%(c2)23s' % {'c1' : str_list[index], 'c2' : int_list[index]})
	index += 1
print()

for (index, author) in enumerate(str_list):
    print('%20s' % author, '*' * int(int_list[index]))

"""
         Jane Austen ******
     Charles Dickens ********************
    Ernest Hemingway *********
        Jack Kerouac **********************
 F. Scott Fitzgerald ********
        Mary Shelley *******
    Charlotte Bronte *****
          Mark Twain ***********
     Agatha Christie *************************************************************************
        Ian Flemming **************
        J.K. Rowling **************
        Stephen King ******************************************************
         Oscar Wilde *
"""