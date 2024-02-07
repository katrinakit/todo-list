# 
# Todo App
# 
# Masivi https://mape.gov.lv/catalog/materials/6501426F-B6EC-44B3-8B93-DC553DAE8886/view?preview=7A90D16F-0A8A-4840-A2E3-5EA4F6D4E194
# Lists https://www.w3schools.com/python/python_lists.asp
# 

def add(shopping_list, item):
  if (len(shopping_list) >=100):
   print("nemelo, nekadam produktam nav tik garšs vārds")
  else:
   # https://www.w3schools.com/python/python_lists_add.asp
   shopping_list.append(item)
  pass


def remove(shopping_list, index):
  # https://www.w3schools.com/python/python_lists_remove.asp
  shopping_list.pop(index)
  pass


def clear(shopping_list):
  # https://www.w3schools.com/python/python_lists_remove.asp
  shopping_list.clear()
  pass


def print_list(shopping_list):
  # https://www.w3schools.com/python/python_lists_loop.asp
  print(shopping_list)
  pass


def show(shopping_list):
  # https://www.w3schools.com/python/python_lists_access.asp
  print(shopping_list[index])
  pass

shopping_list = []
print(shopping_list)
print("pievieno dažus poduktus kuru mums vajag nopirkt lai izveidotu šokolādes kūku")
while True:
  choice = int(input("1. Add\n2. Remove\n3. Clear\n4. Print list\n5. Show item by index\n6. Exit\n"))
  if choice == 1:
    item = input("ko tu gribi pievienot?\n")
    add(shopping_list, item) 
    print(shopping_list)
  elif choice == 2:
    index = int(input("ko tu gribi noņemt?\n"))
    remove(shopping_list, index)
    print_list(shopping_list)
  elif choice == 3:
    clear(shopping_list)
    print_list("saraksts ir tukšs")
  elif choice == 4:
    print(shopping_list)
  elif choice == 5:
    show(shopping_list)
  elif choice == 6:
    print("you couldnt afford a chocolate cake? ur dog will starve without it, oh nvm dogs cant eat chocolate...GOOD JOB YOU SAVED UR DOG")
    break
  else:
    print("Invalid input")
