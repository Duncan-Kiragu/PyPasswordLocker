# PyPasswordLocker

## Built by [Duncan Kiragu](https://github.com/Duncan-Kiragu/)

## Description 
PyPasswordLocker is a python application run on the terminal that allows the users to create a password vault whereby the user can store account details such as usernames and passwords for different sites; The application can also generate a random 8 character password which users can copy and use as their default password and which is stored in the pypasswordlocker for future rference


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display codes for navigation | **In terminal: $./password_locker.py** | Welcome, choose an option: CA-Create Account, LI-Log In, EX-Exit |

| **Enter: CA** | Enter your first name, last name and password |

| **Enter: li** | Enter your account name and password |


| **Successful login** | 
Choose an option: CC - Create Credential,

 DC - Display Credentials, 
 
 COPY - Copy Credential,
 
  EX - exit,
  
   DT - delete credential |


**Enter: CC** | Enter the site name, your username and password |


**Enter: DC** | Prints a list of saved credentials |


**Enter: COPY** | Enter the site name of the credential you wish to copy. |
|**Enter: EX**|


**Enter: EX** | Exit the current navigation stage |


## Installation requirements
* Python 3.8.2 - Downloaded from (python.org)
* Pip
* Pyperclip
* Xclip

### Project access
* Download the zip folder available on clicking the green clone/download button 
	(https://github.com/Duncan-Kiragu/PyPasswordLocker/archive/master.zip)

* In your terminal or cmd

        $ git clone https://github.com/Duncan-Kiragu/PyPasswordLocker.git
        $ cd PyPasswordLocker

### Project running

* To run the PyApp, in your terminal:

	$ chmod +x PyPasswordLocker.py
        $ ./PyPasswordLocker.py
        

### App testing

* The PyApp used unittesting to test its files

* However, more tests can be run on the terminal or cmd using

	 $ python3.6 user_credentials_test.py


## Known bugs

Does not make use of a GUI

## Technologies Used

* Python 3.8.2
* Pyperclip 1.8.0
* XTerm Ubuntu terminal

## Contact-information

> Ask for collaboration or correction: reach out to *mathenge089@gmail.com*

## License

Copyright 2020 *Duncan Kiragu*

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.