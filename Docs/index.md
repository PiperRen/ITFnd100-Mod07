# Title
LTurner, 8.23.21
Foundations of Programming: Python
Assignment 07


## Introduction
This document will cover how to pickle data in Python and how to work with error handling in Python. 
These topics are important for dealing with more than just a text file and building code that is more robust for the user. 
Pickling allows for use of binary files with Python. Error handling creates a more robust script. 

## Pickling
Python has the ability to pickle data. But what does that mean? In the simplest terms it’s a way to preserve data, 
just as pickling food preserves the food. Pickling is specifically used working with binary data files. 
When using a binary file, one needs a program of some sort to sort through what is in the binary file 
and then dump the data back into a binary file format when saving the data. 

### Binary vs Text Files
Binary files store the data in the form of bytes (non-text), or 0’s and 1’s. 
As you can imagine, text files can only contain textual data. Text files however are less likely to become corrupted
than binary files due to the structure and detail that binary files must be written in. 
A small error in a text file may cause a slight error, but a small error in a binary file can cause the file to not be usable.


![Figure 1.](/Docs/assets/css/Figure1.png)

Figure 1. Example of what a binary file looks like. 
This example shows how much more difficult it is to read a binary file than a text file. (Source: [Wikipedia](https://en.wikipedia.org/wiki/Binary_file))

Binary files are useful because they can be saved to a disk or easily sent to others. 
Binary files should not be used when trying to share code across different coding languages. 
The Pickle protocol is only used in Python, so the code will not work across different languages. 

For more information on binary files including, what they are, advantages over text files, and issues with binary files; 
I read over a CareerKarma article ([CareerKarma article](https://careerkarma.com/blog/what-is-binary-file/)). 
This site also had some great information about text files as well. 
I liked that the article went over both types of files and gave pros and cons of each file type. 

### How to Pickle Files
To start pickling a file, one must start by importing it into Python. This can be done with a simple line of code that can be seen in the below figure. 

![Figure 2.](/Docs/assets/css/Figure2.png)

Figure 2. This is an example of the script needed to be able to start pickling data. 

The script needed to read, write, and append data to or from a binary file is very similar to how to read, write, and append the data to a text file. 
The main difference is the addition of a “b”. See table and figure below for examples of the script. 
A more detailed table can be found on page 201 in Python Programming for the Absolute Beginner, 3rd Edition. 

![Figure 3.](/Docs/assets/css/Figure3.png)

Figure 3. Example script of how to open a binary file in read mode. 

Table 1. Example of the differences between reading, writing, and appending a binary or text file. 

Binary codes are complicated, so I’m first going to go over how to use Python to create a binary file. 
To start with, we will need to import “pickle” to be able to use it (see Figure 2) and then ask Python
to write a variable, list, dictionary, or value to the binary file. 
The convention Python uses is dump - dump the data from the “list_of_rows” into the file. 

![Figure 4.](/Docs/assets/css/Figure4.png)

Figure 4. Example of the script for the function to save the data to the binary file and the function to read the data from the file. 
Both a simple print function and the read from file function both produce the same result. 

With data in the file, I now wanted to read the data back out of the file to check that the save was successful. 
In Figure 4, I read from the file and printed the information back. As with saving data to the file, reading data from the file is very similar 
to the script used for a text file. Open the file, place the data in the file into “list_of_rows”, and then return “list_of_rows”. 

![Figure 5.](/Docs/assets/css/Figure5.png)

Figure 5. Example of the script used to read the data from the binary file into the “list_of_rows”. 
The figure also shows the output from the simple print of the list and the print from the reading of the list from the binary file. 

As demonstrated in this section, reading/writing/appending to a file (binary or text), is similar with some differences. 
First difference is you have to import pickle at the start of your code.  Pickle is always needed when working with binary code. 
Next there is a difference in how you open the file, there is an added “b” to the letting, as seen in Table 1. 
The file extension for a binary file is “dat” instead of “txt” for a text file.

## Structure Error Handling
Errors occur when running scripts and programs. Errors are normal. In Python when it comes to an error, it will throw an exception. 
An exception meaning it found an issue and doesn’t know how to resolve the issue. 
When Python finds the exception, the program or scripts exits, and Python prints out a non-user-friendly exception error. 

![Figure 6.](/Docs/assets/css/Figure6.png)

Figure 6. This is an example of the exception when a file is not found. 

In Figure 5, Python was asked to read the file Error.txt, but since the file doesn’t exist yet, the file can’t be read. 
Python throws an exception and prints out some information about the exception. The hard part about this exception is understanding what it means. 
The final line in the output in Figure 6, states that the program ended. With the program ended, the user cannot continue on with the program. 
To deal with complicated exception statements and to keep the program running, there are two things as coders we can do to improve the functionality of the script. 

First, we can ask Python to print out more information than the standard output from an exception. 
The second thing we can do is use a try/except block to allow the program to keep running even if there is an exception. 
The final step a coder can do is create custom exceptions; this is especially helpful when requiring specific types of inputs from a user such as a numeric value. 

### Try/Except Blocks
To keep the program running for the user, try/except blocks are used to let the code try the script and if it doesn’t work do something else. 
The example error we started with in Figure 6, was file not found error. If the program was used to read information from a file, 
change the data, and then save it back to the file; if there was no file to read the program would just end and the user wouldn’t be able to complete any other tasks. 

To fix this probably of the exception we can use a try/except block to try and read the file, and if there is an exception 
print a message back to the user and continue through the code. An example of this script is in Figure 7 below. 

![Figure 7.](/Docs/assets/css/Figure7.png)

Figure 7. This is an example of the script and output from the try/except block. 

The script asks for the file “Error.txt” to be read, but the file does not exist yet, so Python can’t read it. 
The except block catches that and returns a more friendly note to the user. In this example we already knew what the exception was 
based on previous trials to read the data. What happens when we need more information to figure out what Python is trying to tell us. 

### Information about Exceptions
One of the most helpful things one can do when wanting to know more information is to print it out. 
A try/except block can be set-up to print information out if there is an exception. 
Based on the additional information we can be more specific with the except script. 

![Figure 8.](/Docs/assets/css/Figure8.png)

Figure 8. Example of how to print information about the error, to help understand the exception and how to deal with it. 
The exception is “No such file or directory: ‘Error.txt’” and the type is in the class <FileNotFoundError>. 

With information about the exception printed, it makes it easier to figure out what can be done about the exception. 
  In the example in Figure 8, the error type printed was “FileNotFoundError”. Now that I know what the exception is a 
  I can write a more specific except script to provide input back to the user. 
  An example of that is shown in the previous Figure 7.   
  
### Customizing Exceptions
  
  Python also allows custom exceptions to be raise. 
  If one wanted the user input for a certain variable to only be a float and nothing else, 
  an exception could be called if the user entered something other than a number. 

![Figure 9.](/Docs/assets/css/Figure9.png)

Figure 9. Example of how to write the script to raise a custom exception based on if there is an issue with the input or variable. 
