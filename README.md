# Contact Book MongoDB 
### Description:
I plan to allow the user to input contacts for people, including; a phone number, a email address and a home address, which will be verified through regular expressions before being uploaded to a MongoDB database.

This project was completed as my final project for CS50p Introduction to Programming with Python. I decided on this project as I wanted to become familiar with a non-relational database after only using SQL-based databases in the past.

Below is a description of what each part of each file accomplishes.

# main.py
retrieve_database() establishes a connection with the mongodb database I created for this project.

get_name() verifies that the name the user has provided is valid.

get_address() verifies that the address the user has provided is valid through regular expression checks.

get_mobile verifies that the mobile the user has provided is valid through regular expression checks.

get_email verifies that the email the user has provided is valid through regular expression checks.

inp() collects the type of CRUD method that the user would like to perform on the database.

main() asks the user for their method via inp(), and then based on the input will update the mongodb database with either a create, read, update or delete method. Each of these methods goes through testing, and then uses various pymongo methods to update the mongodb database.

# requirements.txt
Lists the libraries and packages required for this script to work

# mongo.env
Contains the pseudo username and password needed to access the mongodb.