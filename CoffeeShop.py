def display_menu():
  print('====== Our Menu ======')
  
  print('\n1 - Coffee: R$10,90')
  print('2 - Cappuccino: R$12,00')
  print('3 - Coffee with Mint: R$13,99')
  print('4 - Latte: R$19,90')
  print('5 - Coffee with Milk: R$15.00')
  print('0 - Close Order')
  
  print('-' * 30)
  
def get_price(item):
  if item == 1:
    return 10.90
  
  elif item == 2:
    return 12.00
  
  elif item == 3:
    return 13.99
  
  elif item == 4:
    return 19.90
  
  elif item == 5:
    return 15.00
  
  else:
    return 0.00
  
def coffee_shop():
  total = 0
  while True:
    display_menu()
    try:
      choice = int(input('\nChoose the item number you want, or press 0 for close! '))
      
    except ValueError:
      print('\nPlease, write a valid number! ')
      continue
    
    if choice == 0:
      break
    
    elif choice in [1, 2, 3, 4, 5]:
      price = get_price(choice)
      total += price
      
      print(f'\nitem added to cart. Price: R${price:.2f}')
      
    else:
      print('\nInvalid. Try again.')
      
  print(f'\nTotal to pay: R${total:.2f}')
  print('Thank you!!')

coffee_shop()
   
  
  

