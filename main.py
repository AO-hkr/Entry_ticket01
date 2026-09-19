shopping_list_title = str(input('Enter shopping list title: ')).capitalize()
shopping_list = f'{'-' * 20}\n{shopping_list_title:^20}\n{'-' * 20}\n'


def menu():
    print(
        '1. Add an item\n'
        '2. Print currently added items\n'
        '3. Finished\n'
        'Enter your choice: ', end=''
    )


menu()

while True:

    user_input = input()

    if not user_input.strip():
        print('\nError: Input must be of an integer type\n')
        menu()
        continue

    choice = int(user_input)

    if choice == 1:
        while True:
            print('Name of item: ', end='')
            user_input = input()

            if not user_input.strip():
                print('\nError: input must be of string type\n')
                continue

            item_name = str(f'{user_input}\n').capitalize()
            shopping_list += item_name
            break
    elif choice == 2:
        print(shopping_list)
    elif choice == 3:
        break

    menu()
