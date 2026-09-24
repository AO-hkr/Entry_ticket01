shopping_list_title = str(input('Enter shopping list title: '))
shopping_list = f'{'-' * 20}\n{shopping_list_title:^20}\n{'-' * 20}\n'
curr_items = ''
reset_count = 0


def menu():
    print(
        '1. Add an item\n'
        '2. Print currently added items\n'
        '3. Finished\n'
        'R. Reset shopping list\n'
        'T. Reset from template\n'
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
            while True:
                print('Name of item: ', end='')
                user_input = input()

                if not user_input.strip():
                    print('\nError: Invalid choice, please try again.\n')
                    continue

                item_name = str(f'{user_input}\n')
                curr_items += item_name
                shopping_list += item_name
                break
        elif choice == 2:
            print(f'Currently added items:\n{curr_items}')
        elif choice == 3:
            if reset_count > 0:
                shopping_list += (
                    '<< Shopping list was reset '
                    f'{reset_count} time(s) >>')
            else:
                shopping_list += '<< Shopping list was never reset >>'
            print(shopping_list)
            break
        else:
            print('\nError: Invalid choice, please try again.\n')
            menu()
            continue
    else:
        if choice.lower() == 'r':
            while (
                    answer := str(input('Are you sure (y/n)? '))
                    ).lower() != 'y' or answer.lower() != 'n':

                if answer.lower() == 'y':
                    shopping_list = (
                        f'{'-' * 20}\n{shopping_list_title:^20}\n{'-' * 20}\n'
                        )
                    curr_items = ''
                    reset_count += 1
                    break
                elif answer == 'n':
                    break
        if choice.lower() == 't':
            while True:
                print(
                    '1) Sweets\n'
                    '2) Fruits')

                user_input = input()
                if not user_input.strip():
                    print('\nError: Invalid choice, please try again.\n')
                    continue

                if user_input.isdigit():
                    choice = int(user_input)
                else:
                    print('\nError: Invalid choice, please try again.\n')
                    continue

                shopping_list = (
                                    f'{'-' * 20}\n'
                                    f'{shopping_list_title:^20}\n'
                                    f'{'-' * 20}\n'
                                )
                curr_items = 3
                if choice == 1:           
                    shopping_list += 'Dumle\nJapp\nBilar\n'
                    reset_count += 1
                    break
                elif choice == 2:
                    shopping_list += 'Apple\nPear\nBanana\n'
                    reset_count += 1
                    break
                else:
                    print('\nInvalid option, pick 1 or 2.\n')
                    continue

    menu()
