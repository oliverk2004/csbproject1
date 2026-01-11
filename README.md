# CSB Project1

## Introduction
Cyber Security Base Project 1 -course repo.
I use in this project OWASP list from the year 2021: https://owasp.org/Top10/2021/
The project is based on backend. 

### How to run the project (on Windows)
This web app is made using Python and Django so therefore you should first read the [installation guide](https://cybersecuritybase.mooc.fi/installation-guide) so you have installed the required libraries and dependencies. It is used in this course (MOOC Cyber Security Base 2025). 

Open a command prompt or bash and clone this repository by entering:
```
git clone https://github.com/oliverk2004/csbproject1.git
```
Next you must navigate to the directory where you cloned the repository. 
When you are in the directory, run these following commands one after another to make the necessary migrations:
```
python manage.py makemigrations
python manage.py migrate
```
Last but not least, start the server:
```
python manage.py runserver
```
The website is running on your localhost server: http://localhost:8000/

## Flaw 1: Broken Access Control
Access control enforces policy such that users cannot act outside of their intended permissions [[1](https://owasp.org/Top10/2021/A01_2021-Broken_Access_Control/)]. For example, user has access on viewing sensitive data or performing adminstrative actions, which easily causes security concerns. 

This Christmas Meal Voting -app has one serious flaw on access control. User must be logged in before voting so the user won't manipulate the results because every user has only one vote to give on each question. This problem can be fixed by adding @login_required in views.py in **ADD METHDOS HERE!**. 

## Flaw 2: Security Misconfiguration
Security misconfiguration includes a wide range of issues. Issues may have been explictly misdefined by the programmers or could have been left unchanged. 


## Flaw 3: Identification and Authentication Failures
Identification and authentication failures are security vulnerabilities that can occur when a system or application fails to identify or authenticate a user correctly [2]. A hacker can easily obtain and use anyone's credentials through brute force, if the authentication methods are weak enough. 


**Links to the flaw in this project:**
- Password validators: **ADD LINK HERE**
- Secure session cookies: **ADD LINK HERE**



### Sources:
1. (https://owasp.org/Top10/2021/A01_2021-Broken_Access_Control/)
