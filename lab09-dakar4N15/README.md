# Laboratory 9

## Laboratory Objectives
1. Explore and use various tools such as: GitHub, VirtualBox, Tuffix, Linux Terminal, and Atom.
1. Write a Python program using:
     1. unittest module
1. Run and test a Python program.

## Getting Started
1. Open the Terminal program in Tuffix.
1. Change the present working directory to the `Documents` directory by typing the following command at the command prompt:

    ```
    cd Documents
    ```

1. Make a copy of this Github repository on your computer using the `git` and `clone` commands that you will input to the terminal. The commands take a URL as a parameter to specify where it can get a copy of the repository. You can find the URL by clicking on the green *Clone or download* button at the top right part of this page. Copy the URL and replace the example text shown below. Note that `username` should be replaced with your own Github username. When you hit <kbd>Enter</kbd> it will ask you to provide your Github username and token. Once done, you will have a copy of the repository on your computer.
    ```
    git clone https://github.com/CSUF-CPSC223P-STMAY-2023S/lab09-username.git
    ```
1. Navigate into the new directory using the command line. Note that `username` should be replaced with your own Github username.  As a shortcut, you can type the first few letters of the folder name and press <kbd>Tab</kbd> so that it auto completes the folder name for you.

     ```
     cd lab09-username
     ```
     
## Program Instructions
1. Write a custom unittest Class that tests a giving `si` module which has a `SimpleInteger` class with the following functions:
   <pre>
   <i><b>add(a, b)</b></i> -> returns a + b<br>
   <i><b>subtract(a, b)</b></i> -> returns a - b<br>
   <i><b>multiply(a, b)</b></i> -> returns a * b<br>
   <i><b>isequal(a, b)</b></i> -> returns True if a == b otherwise False<br>
   <i><b>isgreaterthan(a, b)</b></i> -> returns True if a > b otherwise False<br>
   <i>Note: All functions return a None if either a or b are not integers.</i>
   </pre>
3. Create a `test` module to meet the following requirements (note: use all previous lab assignment test.py files as a reference):
     1. Create a file named `test.py`.
          1. Import the `unittest` and `io` built in modules, and the given `si` module.
          1. Define a class named `Test01_add_valid_data` that inherits from `unittest.TestCase`.  
               1. Define a member function named `test_list_int` to meet the following requirements:
                    1. Create an object instance of the `SimpleInteger` class.
                    1. Call the objects `add` function providing any two integers, say 1 and 2 and saves the return value.
                    1. Call the unittest's `self.assertEqual` function passing it the expected value (3) and the actual value (the return value).
                    1. Note: You can use the docstring to identify what the specific unit is testing and the expected output for a given input.
          1. Define a class named `Test02_add_invalid_data` that inherits from `unittest.TestCase`.  
               1. Define a member function named `test_list_int` to meet the following requirements:
                    1. Create an object instance of the `SimpleInteger` class.
                    1. Call the objects `add` function providing at least one floating point, say 1.5 and 2 and saves the return value.
                    1. Call the unittest's `self.assertEqual` function passing it the expected value (None) and the actual value (the return value).
          1. Define a class named `Test03_subtract_valid_data` that inherits from `unittest.TestCase`.  
               1. Define a member function named `test_list_int` to meet the following requirements:
                    1. Create an object instance of the `SimpleInteger` class.
                    1. Call the objects `subtract` function providing any two integers, say 3 and 7 and saves the return value.
                    1. Call the unittest's `self.assertEqual` function passing it the expected value (-4) and the actual value (the return value).
          1. Define a class named `Test04_subtract_invalid_data` that inherits from `unittest.TestCase`.  
               1. Define a member function named `test_list_int` to meet the following requirements:
                    1. Create an object instance of the `SimpleInteger` class.
                    1. Call the objects `subtract` function providing at least one floating point, say 3.5 and 7 and saves the return value.
                    1. Call the unittest's `self.assertEqual` function passing it the expected value (None) and the actual value (the return value).
          1. Define a class named `Test05_multiply_valid_data` that inherits from `unittest.TestCase`.  
               1. Define a member function named `test_list_int` to meet the following requirements:
                    1. Create an object instance of the `SimpleInteger` class.
                    1. Call the objects `multiply` function providing any two integers, say 5 and 3 and saves the return value.
                    1. Call the unittest's `self.assertEqual` function passing it the expected value (15) and the actual value (the return value).
          1. Define a class named `Test06_multiply_invalid_data` that inherits from `unittest.TestCase`.  
               1. Define a member function named `test_list_int` to meet the following requirements:
                    1. Create an object instance of the `SimpleInteger` class.
                    1. Call the objects `multiply` function providing at least one floating point, say 5.5 and 3 and saves the return value.
                    1. Call the unittest's `self.assertEqual` function passing it the expected value (None) and the actual value (the return value).
          1. Define a class named `Test07_isequal_valid_true_data` that inherits from `unittest.TestCase`.  
               1. Define a member function named `test_list_int` to meet the following requirements:
                    1. Create an object instance of the `SimpleInteger` class.
                    1. Call the objects `isequal` function providing any single integer two times, say 7 and 7 and saves the return value.
                    1. Call the unittest's `self.assertEqual` function passing it the expected value (True) and the actual value (the return value).
          1. Define a class named `Test08_isequal_valid_false_data` that inherits from `unittest.TestCase`.  
               1. Define a member function named `test_list_int` to meet the following requirements:
                    1. Create an object instance of the `SimpleInteger` class.
                    1. Call the objects `isequal` function providing any two unique integers, say 7 and 8 and saves the return value.
                    1. Call the unittest's `self.assertEqual` function passing it the expected value (False) and the actual value (the return value).
          1. Define a class named `Test09_isequal_invalid_data` that inherits from `unittest.TestCase`.  
               1. Define a member function named `test_list_int` to meet the following requirements:
                    1. Create an object instance of the `SimpleInteger` class.
                    1. Call the objects `isequal` function providing at least one floating point, say 7.5 and 7 and saves the return value.
                    1. Call the unittest's `self.assertEqual` function passing it the expected value (None) and the actual value (the return value).
          1. Define a class named `Test10_isgreaterthan_valid_true_data` that inherits from `unittest.TestCase`.  
               1. Define a member function named `test_list_int` to meet the following requirements:
                    1. Create an object instance of the `SimpleInteger` class.
                    1. Call the objects `isgreaterthan` function providing any integer followed by any integer less than the first, say 10 and 6 and saves the return value.
                    1. Call the unittest's `self.assertEqual` function passing it the expected value (True) and the actual value (the return value).
          1. Define a class named `Test11_isgreaterthan_valid_false_data` that inherits from `unittest.TestCase`.  
               1. Define a member function named `test_list_int` to meet the following requirements:
                    1. Create an object instance of the `SimpleInteger` class.
                    1. Call the objects `isgreaterthan` function providing any integer followed by any integer equal to or greater than the first, say 10 and 10 and saves the return value.
                    1. Call the unittest's `self.assertEqual` function passing it the expected value (False) and the actual value (the return value).
          1. Define a class named `Test12_isgreaterthan_invalid_data` that inherits from `unittest.TestCase`.  
               1. Define a member function named `test_list_int` to meet the following requirements:
                    1. Create an object instance of the `SimpleInteger` class.
                    1. Call the objects `isgreaterthan` function providing at least one floating point, say 10.5 and 6 and saves the return value.
                    1. Call the unittest's `self.assertEqual` function passing it the expected value (None) and the actual value (the return value).
          1. Include the following code at the bottom of the module file:
                <pre>
                if __name__ == '__main__':
                   with open('test.txt', "w") as f:
                       runner = unittest.TextTestRunner(f)
                       unittest.main(testRunner=runner)
               </pre>
1. Run the unit testing program to ensure that your unitest runs as expected:

    ```
    ./test.sh
    ```
       
    The unit testing will output the results of unittest classes you created.  It will log the results in the `test.txt` file. You will need to edit your unittest source code to fix any errors and run `./test.sh` repeatedly until it passes all the test.

## Submission
Periodically throughout the exercise, and when you have completed the exercise, **submit the complete repository to Github**.

   <pre>git add .<br>git commit -m "<i>your comment</i>"<br>git push</pre>

In case it asks you  to configure global variables for an email and name, just copy the commands it provides then replace the dummy text with your email and Github token.

   <pre>git config --global user.email "<i>tuffy@csu.fullerton.edu</i>"<br>git config --global user.name "<i>Tuffy Titan</i>"<br>git commit -m "<i>your comment</i>"<br>git push</pre>

When you completed the final Github push, go back into github.com through the browser interface and ensure all your files have been correctly updated.  You should have the following files:
```
test.py
test.txt
```
    
## Grading
1. All points add up to a total of 100 points possible as detailed below.  Partial credit will be given where applicable.

| Points | Description |
| --- | --- |
|50|initial git clone of this repository to your Tuffix machine|
|21|test.py file submitted and meets the program requirements |
|5|test.txt file submitted and meets the program requirements |
|2|unit test passes Test01_add_valid_data|
|2|unit test passes Test02_add_invalid_data|
|2|unit test passes Test03_subtract_valid_data|
|2|unit test passes Test04_subtract_invalid_data|
|2|unit test passes Test05_multiply_valid_data|
|2|unit test passes Test06_multiply_invalid_data|
|2|unit test passes Test07_isequal_valid_true_data|
|2|unit test passes Test08_isequal_valid_false_data|
|2|unit test passes Test09_isequal_invalid_data|
|2|unit test passes Test10_isgreaterthan_valid_true_data|
|2|unit test passes Test11_isgreaterthan_valid_false_data|
|2|unit test passes Test12_isgreaterthan_invalid_data|
