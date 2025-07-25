
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
def adding (shopping_list):
    item = input("Enter the item to add: ")

    shopping_list.append(item)
    print('user added succsefully!')


def remove(shopping_list):
    user = input("what object you want to remove from the cart :")
    if user in shopping_list:
        shopping_list.remove(user)
    else:
        print('this item isnot in the shopping list')


def show(shopping_list):
    if not shopping_list:
        print('the shopping list is empty')
    else:
        
        for item in shopping_list:
            print(item)


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            
            adding(shopping_list)
        elif choice == '2':
            remove(shopping_list)
            
        elif choice == '3':
            show(shopping_list)
            
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

