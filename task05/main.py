shopping_list_title = str(input('Enter shopping list title: '))
shopping_list = f'{'-' * 20}\n{shopping_list_title:^20}\n{'-' * 20}\n'
curr_items = ''


def menu():
    print(
        '1. Add an item\n'
        '2. Print currently added items\n'
        '3. Finished\n'
        'C. Calculate price\n'
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
            print(shopping_list)
            break
        else:
            print('\nError: Invalid choice, please try again.\n')
            menu()
            continue
    elif choice.lower() == 'c':
        sum = 0
        min = 0
        max = 0
        for i in range(0, 3):
            while (val := int(input(f'Enter price for item {i+1}: '))) < 0:
                print('\nERROR: Prices must be positive numbers. Try again!')

            if val < min or min == 0:
                min = val
            if val > max:
                max = val
            sum += val
        print(f'Total price:{sum:>5} SEK')
        print(f'Min: {min}, Max: {max}, Average: {sum/3:.2f}')
    menu()
