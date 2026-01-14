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

## Broken Access Control (FLAW 1)
Access control enforces policy such that users cannot act outside of their intended permissions [[1](https://owasp.org/Top10/2021/A01_2021-Broken_Access_Control/)]. For example, user has access on viewing sensitive data or performing adminstrative actions, which easily causes security concerns. 

This Christmas Meal Voting -app has one serious flaw on access control. User must be logged in before voting so the user won't manipulate the results because every user has only one vote to give on each question. This problem can be fixed by adding @login_required in views.py in **ADD METHDOS HERE!**. 

## Security Misconfiguration (FLAW 2)
Security misconfiguration includes a wide range of issues. Issues may have been explictly misdefined by the programmers or could have been left unchanged. 


## Identification and Authentication Failures (FLAW 3)
Identification and authentication failures are security vulnerabilities that can occur when a system or application fails to identify or authenticate a user correctly [2]. A hacker can easily obtain and use anyone's credentials through brute force, if the authentication methods are weak enough. **Add more texts still...**

### Links to the flaw in this project:
- Password validators: https://github.com/oliverk2004/csbproject1/blob/main/config/settings.py#L87-L102
- Secure session cookies: https://github.com/oliverk2004/csbproject1/blob/main/config/settings.py#L104-L105

### FIX:
To fix this flaw is very simple. Uncomment the lines in *settings.py* file to use Django's strict password control and secure session cookies. After that, all session cookies will be encrypted. Now the app is requiring new user to set password within the limits of:
- Your password can’t be too similar to your other personal information.
- Your password must contain at least 8 characters.
- Your password can’t be a commonly used password.
- Your password can’t be entirely numeric.

*There is no ability (yet) to change your password (except admin) which you would increase the security further...*

## CSRF (FLAW 4)
Cross-Site Request Forgery (CSRF) is a flaw that, is not so common nowadays because there is more secure web frameworks. In CSRF, user can send unauthorized web requests to a website through other website where the user is authenticated. This lets the attackers access the data as they were you as a user. CSRF attacks target functionality that causes a state change on the server, such as changing the victim's email address or password, or purchasing something [3]. CSRF attacks are possible in this project because built-in CSRF protection is disabled. 

### Links to the flaw in this project:
- Add CSRF tokens:
  1. https://github.com/oliverk2004/csbproject1/blob/main/polls/templates/polls/index.html#L17
  2. https://github.com/oliverk2004/csbproject1/blob/main/templates/registration/login.html#L14
  3. https://github.com/oliverk2004/csbproject1/blob/main/templates/registration/signup.html#L10
- SameSite Cookies: https://github.com/oliverk2004/csbproject1/blob/main/config/settings.py#L132

### FIX:
Luckily this flaw is easy to fix. In *index.html* file, remove the comment around {% csrf_token %} to enable the protection. Also, delete the final row in *settings.py* file "SESSION_COOKIE_SAMESITE = None". Now it is set back to default, enabling additional CSRF protection. 


## References:
1. https://owasp.org/Top10/2021/A01_2021-Broken_Access_Control/
2. ?
3. https://owasp.org/www-community/attacks/csrf
