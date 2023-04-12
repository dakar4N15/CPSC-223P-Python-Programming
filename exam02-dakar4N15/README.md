# Exam 2

## Rules of Behavior
1. Do not communicate with anyone during the exam (no email, no social media, no Discord, no texting, no phones, no talking, no passing notes, no internet communicating).  If there is any evidence of communicating with anyone during the exam you will receive a zero.
1. You **must** turn off your cell phone and store it away.
1. Your submission **must** be solely you own work without the assistance of anyone by any means.
1. All programming code **must** be written in Python.
1. You **must** use Tuffix to unit test your program.
1. All your code **must** be pushed to Github by the scheduled end of class today.  Any submissions after that time will not be considered.
1. You may use your book.
1. You may use the Internet as a **reference only**.
1. If you have questions, approach the instructor desk.

## Getting Started
1. Open the Terminal program in Tuffix.
1. Change the present working directory to the `Documents` directory by typing the following command at the command prompt:

    ```
    cd Documents
    ```
1. Make a copy of this Github repository on your computer using the `git` and `clone` commands that you will input to the terminal. The commands take a URL as a parameter to specify where it can get a copy of the repository. You can find the URL by clicking on the green *Clone or download* button at the top right part of this page. Copy the URL and replace the example text shown below. Note that `username` should be replaced with your own Github username. When you hit <kbd>Enter</kbd> it will ask you to provide your Github username and token. Once done, you will have a copy of the repository on your computer.
    ```
    git clone https://github.com/CSUF-CPSC223P-STMAY-2023S/exam02-username.git
    ```
1. Navigate into the new directory using the command line. Note that `username` should be replaced with your own Github username.  As a shortcut, you can type the first few letters of the folder name and press <kbd>Tab</kbd> so that it auto completes the folder name for you.

     ```
     cd exam02-username
     ```
     
## Program Instructions
1. Your are given an `appointments.dat` file which contains a JSON encoded dictionary of appointments.  The data structure is as follows:
     ```
	appointments dictionary:
		key: phone number as string (containing a 10 digit integer)
		value : appointment list

	appointment list:
        element 0: first name as a string
        element 1: last name as a sting
        element 2: date and time as a string, formatted as YYYY-MM-DD HH:mm where HH is 24-hour time
     ```
     While this data file is given, your class should accept any data that meets the above dictionary data structure.
1. A `main.py` is given which creates an instance object of your class, calls the `get_appointments` member function, and prints out the results in a tabular format.  You may use this file to help you build your class and can make any edits to this file. The `main.py` file will not be gradded.  You will only be required to create the appointments module and class as outlined below.
1. Create a `appointments` module to meet the following requirements:
     1. Create a file named `appointments.py`.
          1. Define a class named `Appointments`.  
               1. Define a member function named `__init__` to meet the following requirements:
                    1. Take a self object as a positional parameter.
                    1. Take a filename string as a positional parameter.
                    1. Set a member variable equal to the filename.
                    1. Set a member variable equal to an empty data dictionary.
                    1. Open the filename and load the JSON decoded contents into the empty data dictionary.
                    1. Cleanly manage the `FileNotFoundError` if the filename does not exist.
               1. Define a member function named `add_appointment` to meet the following requirements:
                    1. Take a self object as a positional parameter.
		    1. Take a string as a keyword `phone` parameter.
		    1. Take a string as a keyword `first` parameter.
		    1. Take a string as a keyword `last` parameter.
		    1. Take a string as a keyword `appt_datetime` parameter.
                    1. If the phone number string does not contain 10 numeric digits the function should return a `False`.
                    1. If the phone number already exists in the data dictionary the function should return a `False`.
                    1. If the appointment date and time is invalid the function should return a `False`.
                    1. Add the data to the member variable data dictionary using the data structure outline above.
                    1. Write the JSON encoded contents of the member variable data dictionary to the filename that was set to the member variable.
                    1. Return a `True`.
               1. Define a member function named `delete_appointment` to meet the following requirements:
                    1. Take a self object as a positional parameter.
		    1. Take a string as a keyword `phone` parameter.
                    1. If the phone number string does not contain 10 numeric digits the function should return a `False`.
                    1. If the phone number does not exist in the data dictionary the function should return a `False`.
                    1. Remove the the phone number dictionary element from the member variable data dictionary.
                    1. Write the JSON encoded contents of the member variable data dictionary to the filename that was set to the member variable.
                    13. Return a `True`.
               1. Define a member function named `get_appointments` to meet the following requirements:
                    1. Take a self object as a positional parameter.
		    1. Take a string as a keyword `appt_date` parameter.
                    1. If the supplied appointment date is invalid the function should return an empty list.
                    1. Return a list of appointments for all appointments in the member variable data dictionary that match the supplied date.  The list should have the following elements in order:
                         1. date formatted as "October 3, 2021"
                         1. time formatted as "4:05 pm"
                         1. phone number formatted as "(800)692-7753"
                         1. name formatted first name and last name as "Steve Jobs"
                    2. If there are no appointments on the appointment date the function should return an empty list.
1. Run the program using the command below and repeat the steps above until you are satisfied your program output meets the above requirements.

    ```
    python3 main.py
    ```


1. Typical output for the program using the given `appointments.dat` file:
     ```
	=============== APPOINTMENTS ================

	Appointment Date: September 12, 2023

	  Time       Phone              Name         
	========  =============  ====================
	  7:00 am  (585)757-4218  Lachlan Graves      
	12:30 pm  (666)403-1404  Lillian Carson      
	  4:15 pm  (738)705-9501  Karie Brandt        
     ```

1. Run the unit testing program to ensure that your program runs as expected.

    ```
    ./test.sh
    ```
       
    The unit testing will output the results of a series of tests using specific input and expected output.  Any error will provide information on where the expected output is different from the actual output.  You will need to edit your source code to fix the error and run `./test.sh` repeatedly until it passes all the test.

## Submission
Periodically throughout the exercise, and when you have completed the exercise, **submit the complete repository to Github**.

   <pre>git add .<br>git commit -m "<i>your comment</i>"<br>git push</pre>

In case it asks you  to configure global variables for an email and name, just copy the commands it provides then replace the dummy text with your email and Github token.

   <pre>git config --global user.email "<i>tuffy@csu.fullerton.edu</i>"<br>git config --global user.name "<i>Tuffy Titan</i>"<br>git commit -m "<i>your comment</i>"<br>git push</pre>

When you completed the final Github push, go back into github.com through the browser interface and ensure all your files have been correctly updated.  You should have the following files:
```
appointments.py
test.txt
```
    
## Grading
1. All points add up to a total of 100 points possible as detailed below.  Partial credit will be given where applicable.

| Points | Description |
| --- | --- |
|50|initial git clone of this repository to your Tuffix machine|
|14|appointments.py file submitted and meets the program requirements |
|3|unit test passes Test01_AddAppointment_GoodDataSaved|
|3|unit test passes Test02_AddAppointment_GoodDataReturnedTrue|
|3|unit test passes Test03_AddAppointment_BadPhoneTooShort|
|3|unit test passes Test04_AddAppointment_BadPhoneContainsAlphas|
|3|unit test passes Test05_AddAppointment_BadPhoneAlreadyExists|
|3|unit test passes Test06_AddAppointment_BadDateTime|
|3|unit test passes Test07_DeleteAppointment_GoodPhone|
|3|unit test passes Test08_DeleteAppointment_BadPhoneTooShort|
|3|unit test passes Test09_DeleteAppointment_BadPhoneDoesNotExist|
|3|unit test passes Test10_GetAppointments_GoodDataFound|
|3|unit test passes Test11_GetAppointments_GoodDataNotFound|
|3|unit test passes Test12_GetAppointments_BadData|
