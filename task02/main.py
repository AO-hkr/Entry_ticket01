shopping_list_title = str(input('Enter shopping list title: '))
shopping_list = f'{'-' * 20}\n{shopping_list_title:^20}\n{'-' * 20}\n'
curr_items = ''
counter = 0


def menu():
    print(
        '1. Add an item\n'
        '2. Print currently added items\n'
        '3. Finished\n'
        'S. Show number of added items\n'
        'Enter your choice: ', end=''
    )


menu()

while True:

    user_input = input()

    if not user_input.strip():
        print('\nError: Invalid choice, please try again.\n')
        menu()
        continue

    choice = user_input

    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            if counter >= 10:
                print('\nERROR: The list is full, your item was not added\n')
                continue
            while True:
                print('Name of item: ', end='')
                user_input = input()

                if not user_input.strip():
                    print('\nError: Invalid choice, please try again.\n')
                    continue

                item_name = str(f'{user_input}\n')
                curr_items += item_name
                shopping_list += item_name
                counter += 1
                break
        elif choice == 2:
            print(f'Currently added items:\n{curr_items}')
        elif choice == 3:
            print(shopping_list)
            break
        else:
            print('\nError: Invalid choice, please try again.\n')
            menu()
            continue
    elif choice.isalpha():
        if choice == 'S' or choice == 's':
            print(
                f'Currently the list contains {counter} item(s)\n'
                f'[{'*'*counter:10}]'
            )

    menu()
