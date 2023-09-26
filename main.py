

def introduction():
  print("Hello there! My name is Chatbot.")
  global name
  global age
  name = input("What is your name? -> ")
  age = input("How old are you?-> ")
  print(f"Nice to meet you {name}, how can I help you?")

def menu():
  print(f"1. Placeholder Option 1\n2. Placeholder Option 2\n3. Placeholder Option 3\n4. Exit the conversation")
  response = input("Enter the number of your choice:")
  return response





condition = True
introduction()
while condition:
  number = menu()
  if number == "1":
    print("Option 1")
    print("Anything else?")
  elif number == "2":
    print("Option 2")
    print("Anything else?")
  elif number == "3":
    print("Option 3")
    print("Anything else?")
  elif number == "4":
    condition = False
    print(f"Have a great day {name}, hope to see earlier than you turn {int(age)+1}.")
  else:
    print("Wrong input")
  
  
 
  
  
  


