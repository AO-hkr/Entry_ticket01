shopping_list_title = str(input('Enter shopping list title: '))
shopping_list = f'{'-' * 20}\n{shopping_list_title:^20}\n{'-' * 20}\n'
curr_items = ''
curr_total = 0
curr_units = 0
curr_lowest = 0
curr_highest = 0


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

    choice = int(user_input)

    if choice == 1:
        while True:

            print('Name of item: ', end='')
            user_input = input()

            if not user_input.strip():
                print('\nError: Invalid choice, please try again.\n')
                continue

            item_name = str(f'{user_input}')

            print('Price of item: ', end='')
            user_input = input()

            if not user_input.strip():
                print('\nError: invalid choice, please try again\n')
                continue

            item_price = str(f'{user_input}')

            print('Number of items: ', end='')
            user_input = input()

            if not user_input.strip() or not user_input.isdigit():
                print('\nError: invalid choice, please try again\n')
                continue

            item_number = str(f'{user_input}')

            if float(item_price) < curr_lowest or curr_lowest == 0:
                curr_lowest = float(item_price)
                
            if float(item_price) > curr_highest:
                curr_highest = float(item_price)

            curr_units += int(item_number)
            curr_total += float(item_price) * int(item_number)
            curr_items += f'{item_name}\n'
            shopping_list += item_name
            break
    elif choice == 2:
        print(f'Currently added items:\n{curr_items}')
    elif choice == 3:
        shopping_list += f'\nTotal cost: {float(curr_total):.2f} sek'
        shopping_list += f'\nUnits     : {curr_units}'
        shopping_list += (
            f'\nPrice info: {curr_lowest:.2f} (Low) / '
            f'{curr_highest:.2f} (High) / '
            f'{curr_total/curr_units:.2f} (Average) SEK'
            )
        print(shopping_list)
        break
    else:
        print('\nError: Invalid choice, please try again.\n')
        menu()
        continue

    menu()
