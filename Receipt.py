"""

Southern New Hampshire University
logan.duck@snhu.edu
"""
import locale

locale.setlocale(locale.LC_ALL, 'en_US')

item_prices = {
	'item1' : 1.99,
	'item2' : 2.99,
	'item3' : 3.99
}

all_items_scanned = False

subtotal = 0.0
salesTax = 0.0
grandTotal = 0.0
items = ''

while all_items_scanned != True:
	itemName = input('Enter item name: ')
	itemPrice = item_prices[itemName]
	itemQuantity = int(input('Enter item quantity: '))
	subtotal = subtotal + (itemPrice * itemQuantity)
	salesTax = 0.06 * subtotal
	grandTotal = subtotal + salesTax

	# stores indiv items for printing receipt
	items = items + '\n\t' + itemName
	
	moreItems = input('\nNew item? y/n: ')
	if moreItems == 'n':
		all_items_scanned = True
	elif moreItems != 'n' and moreItems != 'y':
		print('Incorrect input. Expected \'y\' or \'n\'. Ending program..')
		exit()

# print('**********RECEIPT**********\nItems:', items, '\n')
# print('Subtotal: %s' % locale.currency(subtotal))
# print('Sales Tax: %s' % locale.currency(salesTax))
# print('Grand Total: %s' % locale.currency(grandTotal))


receipt = str(('**********RECEIPT**********\nItems:', items, '\n',
			'Subtotal: %s' % locale.currency(subtotal), '\n',
			'Sales Tax: %s' % locale.currency(salesTax), '\n',
			'Grand Total: %s' % locale.currency(grandTotal)))

print(receipt)

