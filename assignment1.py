# Program Name: Assignment1.py (use the name the program is saved as)
# Course: IT3883/Section W02
# Student Name: Enjie Jones
# Assignment Number: Lab 1
# Due Date: 01/20/2025
# Purpose: What does the program do (in a few sentences)? It simply uses an empty string and adds to the string upon user input, or clears it again
# List Specific resources used to complete the assignment. Powerpoint slides provided to refresh

buffer = ""

Running = True

while Running:
    print("\n")
    print('1. Append data to input buffer')
    print('2. Clear the input buffer')
    print('3. Display the input buffer')
    print('4. Quit')

    selection = input("Select from the menu above using 1-4: ")

    if selection == '1':
        x = input("Enter the string to append: ")
        buffer += x
    elif selection == '2':
        buffer = ""
        print("Buffer is cleared")
    elif selection == '3':
        print(f'The current input buffer: {buffer}')
    elif selection == '4':
        print("Ok, exiting the program now.")
        break
    else:
        print("Please select a valid choice")