# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: An example of how to work with pickling and error handling.
#              Example will be creating a file with two numbers input
#              from the user and then adding and multiplying the numbers.
#              User will be able to pick what option they want to perform
#              add new data, read the information in the file, or save file.
#              *** EDIT****
#              Changed the math script into a shopping list. User enters information
#              about items to add to list, and how many of that item to add.
#              User can then save the shopping list to a file for use later.
#              The user can also take off an item from the shopping list.
# ChangeLog (Who,When,What):
# LTurner, 8.20.21, Started working on try/except, error handling big example
# LTurner, 8.21.21, Worked on continuing the script for error handling
#                   Changed the function of the program to write a shopping list
# LTurner, 8.22.21, Worked on fixing some code issues, and testing different
#                   functions to make sure they worked
# LTurner, 8.23.21 Updated the read file function with try/except block based on
#                  feedback from the last assignment. Added the use of some custom
#                  error handling to the user inputs.
# LTurner, 8.24.21 Finishing up error handling and cleaned up notes
# ---------------------------------------------------------------------------- #

import pickle

# Data ----------------------------------------------------------------------- #
# Declare variables and constants
file = "shopping.dat"  # file name where the data is to be stored
list_table = []  # list of dictionary rows


# Processing ----------------------------------------------------------------- #
class Processor:

    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name_input, list_of_rows):
        """ Reads data from a file into a list of dictionary rows
        :param file_name_input: (string) with name of file
        :param list_of_rows: (list) list of rows from the file
        :return: list_of_rows and message_output: (list) of dictionary rows, status
        """
        list_of_rows.clear()
        try:
            reader = open(file_name_input, "rb")
            list_of_rows = pickle.load(reader)
            reader.close()
            message_output = "File found and read."
        except FileNotFoundError:
            message_output = "File not found. Please save or create a file."
        return list_of_rows, message_output

    @staticmethod
    def save_data_to_file(file_name, list_of_rows):
        """ Saves the data in the list of dictionaries to a file

         :param: file_name: string, file name
         :param: list_of_rows: list of dictionary rows
         :return: nothing
         """
        saver = open(file_name, "wb")
        pickle.dump(list_of_rows, saver)
        saver.close()

    @staticmethod
    def add_data_to_list(item_list, item_quantity,list_of_rows):
        """ Creates a dictionary row of the inputs, sum, and product

        :param item_list: first user entered number
        :param item_quantity: second user entered number
        :param list_of_rows: list of dictionary rows
        :return:
        """
        row = {"Item": item_list, "Quantity": item_quantity}
        list_of_rows.append(row)
        return list_of_rows

    @staticmethod
    def remove_data_from_list(item_to_remove, list_of_rows):
        """Removes row from the list of rows based on user input

        :param item_to_remove: user entered task
        :param list_of_rows: list of dictionary rows
        :return: list_of_rows: list of dictionary rows,
                found: indication of if a task was deleted
        """
        found = "Item Not Found. No items removed."
        for row in list_of_rows:
            if row['Item'].lower() == item_to_remove.lower():
                list_of_rows.remove(row)
                found = "Item found and removed."
                break
            else:
                continue
        return list_of_rows, found

# Error Handling ---------------------------------------------------------------------#
# Handling of Errors
# These are the custom errors for this program. The error created in this section
# is for having an input from the user that is too low/small.


class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input is too low"""
    pass


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add new items to shopping list
        2) Remove items from shopping list
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user


        :return: choice_input - users inputted choice
        """
        choice_input = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice_input

    @staticmethod
    def two_item_input():
        """ Gets two user item they want to add and number of those
        items to add to the list. There is a loop and try/except block that
        limits what the user can enter for quantity - want a number that is greater than 1

        :return: user inputs (item / number of items)
        """
        item_entered = input('Please enter an item for the shopping list: ')
        while True:
            try:
                number_item = int(input('Please enter the number of that item to add: '))
                if number_item < 1:
                    raise ValueTooSmallError
                break
            except ValueError:
                print('There was an error. Please enter a numeric value.')
            except ValueTooSmallError:
                print('The number entered was less than 1. Please enter larger value.')
        print('You entered:', item_entered, 'and', number_item)
        return item_entered, number_item

    @staticmethod
    def remove_item_input():
        """Gets the users input for what item to remove from shopping list.

        :return:
        """
        removal = input('Please enter the item to remove from shopping list: ')
        return removal

    @staticmethod
    def print_current_items_in_list(list_of_rows):
        """ Shows the current items in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print('\n')
        print("******* The current Shopping List: *******")
        for row in list_of_rows:
            print(row["Item"], "(", row["Quantity"],')')
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

# Main Body of Script  ------------------------------------------------------ #

# Step 1: Open the file where the data is saved, read the data.
# Exception is thrown if the file is not found.


list_table, message = Processor.read_data_from_file(file, list_table)
IO.input_press_to_continue(message)
# error for file name not ending dat for the pickling

while True:

    IO.print_current_items_in_list(list_table)  # Show current data in the list/table
    IO.print_menu_tasks()  # Shows menu
    choice = IO.input_menu_choice()  # Get menu option from user

    if choice.strip() == '1':
        item, quantity = IO.two_item_input()
        list_table = Processor.add_data_to_list(item,quantity, list_table)
        continue

    elif choice.strip() == '2':
        remove_item = IO.remove_item_input()
        list_table, message = Processor.remove_data_from_list(remove_item,list_table)
        IO.input_press_to_continue(message)

    elif choice.strip() == '3':
        choice_y_n = IO.input_yes_no_choice("Save this data to file? (y/n) - ")  # User input if they want to save
        if choice_y_n.lower() == "y":
            Processor.save_data_to_file(file, list_table)
        else:
            IO.input_press_to_continue("Save Cancelled!")  # If user doesn't want to save, provide message.
        continue  # to show the menu

    elif choice.strip() == '4':
        IO.input_press_to_continue("Warning: Unsaved Data Will Be Lost!")  # Warning to the user about reloading
        choice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")  # input from user
        if choice.lower() == 'y':
            list_table, message = Processor.read_data_from_file(file, list_table)
            IO.print_current_items_in_list(list_table)  # print current list of rows
        else:
            IO.input_press_to_continue("File Reload Cancelled!")  # print message to user that file not reloaded
        continue  # to show the menu

    elif choice.strip() == '5':
        choice_y_n = IO.input_yes_no_choice("Are you sure you want to exit? (y/n) - ")
        if choice_y_n.lower() == "y":
            print("Goodbye!")
            break
        else:
            continue

    else:
        IO.input_press_to_continue("Enter a menu option [1-5]")
        continue


