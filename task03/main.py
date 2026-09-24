shopping_list_title = str(input('Enter shopping list title: '))
shopping_list = f'{'-' * 20}\n{shopping_list_title:^20}\n{'-' * 20}\n'
curr_items = ''
add_amount_errors = 0


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

                item_name = str(f'{user_input}')

                while True:
                    print(f'Amount of {item_name}?: ', end='')
                    user_input = input()

                    if not user_input.strip():
                        print('\nError: Invalid choice, please try again.\n')
                        continue

                    try:
                        user_input = int(user_input)
                    except ValueError:
                        print('\nError: Invalid choice, please try again.\n')
                        continue

                    if user_input < 1 or user_input > 99:
                        print(
                            '\nERROR: You must buy at least 1 but '
                            'not more than 99 of an item. Try again!\n')
                        add_amount_errors += 1
                        continue

                    item_number = str(f'{user_input}')
                    break

                curr_items += f'{item_name}\n'
                shopping_list += (f'{item_name:<10}{'x'}{item_number:>9}\n')
                break
        elif choice == 2:
            print(f'Currently added items:\n{curr_items}')
        elif choice == 3:
            shopping_list += (
                '\nYou gave a number outside the valid '
                f'range a total of {add_amount_errors} time(s)')
            print(shopping_list)
            break
        else:
            print('\nError: Invalid choice, please try again.\n')
            menu()
            continue

    menu()
