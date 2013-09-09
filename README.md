easyphpmysql
============

EasyPHPMYSQL is a command-line python script that is used to  write a PHP class files that connect and manipulate data in a MYSQL database just by answering a couple question about the #database.  Also, it writes an optional login script for an administrator backend and an optional example script that shows a person how to use the php class.

Note:  This project is in the beta stage; thus, there are probably a couple of bugs that I still need to address

Requirements to use this python script:
---------------------------------------
The following python modules need to be installed to use this script:
* MySQLdb

To install this modules, open the terminal and enter the following:
```
pip install MySQL-python

#if you have Ubuntu, you can enter the following command
sudo apt-get install python-mysqldb
```
Usage of this script:
---------------------
To run and use this script, open the terminal and go to the script folder.  Then enter the following command.
```


What is the host name for the database (ie - localhost)?
localhost


What is the userename for the database?
username

What is the password for the database?
password

What is the name of the database?
testdb

What is the filename for the php class?
test.php

What is the name of the php class?
testclass

Do you want login script in the php class (y)es or (n)o?
yes

What is the name of the table with the login information?
logintable

What is the column name that holds the username?
user

What is the column name that holds the password?
password

Do you want example php files to be wrote to demostrate the php class (y)es or (n)o?
yes

The files has been written. Finished!!

#That is it.  Now you should have a php class file called test.php, a php login script called login.php and an example php file that shows you how to use the php class called example.php

```
