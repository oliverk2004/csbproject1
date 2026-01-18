# CSB Project1
LINK TO THIS REPOSITORY: https://github.com/oliverk2004/csbproject1
## Introduction
Cyber Security Base Project 1 -course repo.
I use in this project OWASP list from the year 2021: https://owasp.org/Top10/2021/
The project is based on backend. 

In this web application, you can vote your favorite Christmas meal in different categories. The application has a lot improvments and functions to be done still but with this applications, five quite common cyber security flaws can be demonstrated. Flaws occur in backend and frontend has a lot of todos but in this project those are not necessary. 

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

**NOTE!:** You have to first fix the **Flaw 4 (CSRF)** to use users in this web application.

## Broken Access Control (FLAW 1)
Access control enforces policy such that users cannot act outside of their intended permissions [1]. For example, user has access on viewing sensitive data or performing adminstrative actions, which easily causes security concerns. Furthermore, weak passwords and authentication policy are included under Broken Access Control. Sometimes data is stored in path variables which can be modified to give several users access to that data. 

This Christmas Meal Voting -app has one serious flaw on access control. User must be logged in before voting so the user won't manipulate the results because every user has only one vote to give on each question. This problem can be fixed by adding *@login_required* in views.py to method *vote*.

### Links to the flaw in this project:
1. Login requirement to see the question: https://github.com/oliverk2004/csbproject1/blob/main/polls/views.py#L31-L44
2. Login decorator in vote method: https://github.com/oliverk2004/csbproject1/blob/main/polls/views.py#L61-L62

### FIX: 
Uncommenting these two sections changes the application so that a user has to log in to be able see the question and after that to vote. 

## Security Misconfiguration (FLAW 2)
Security misconfiguration includes a wide range of issues. Issues may have been explictly misdefined by the programmers or could have been left unchanged. It includes questions such as 'who has access to the server where the web application is running?', 'who has access to the server where the database or other components are running?', 'are the software components and libraries as well as the operating systems up to date?', 'are the used passwords high quality?' [2]. 

Django-based web applications includes a *settings.py* file. It can be configured according to the needed user and administrator use cases. Nevertheless, *settings.py* file with the default settings, is not so safe. 

### Links to the flaw in this project:
- Debug enabled: https://github.com/oliverk2004/csbproject1/blob/main/config/settings.py#L26-L27
- Undefined hosts: https://github.com/oliverk2004/csbproject1/blob/main/config/settings.py#L29-L30

### FIX:
To fix this flaw, we have to make a couple corrections in *settings.py* file. 
1. Set DEBUG to False (its default value is True) to not allow attackers to see useful information about the website. For example trying to view a nonexistent page like http://127.0.0.1:8000/hacking_the_page. 
2. Variable ALLOWED_HOSTS is undefined which means that anyone is allowed to run the server. 

**Note!** that application is not working if DEBUG = False and ALLOWED_HOSTS is still = []. You must define ALLOWED_HOSTS as your localhost.

## Identification and Authentication Failures (FLAW 3)
Identification and authentication failures are security vulnerabilities that can occur when a system or application fails to identify or authenticate a user correctly. A hacker can easily obtain and use anyone's credentials through brute force, if the authentication methods are weak enough. OWASP says that where possible, implement multi-factor authentication to prevent automated credential stuffing, brute force, and stolen credential reuse attacks [4]. For me, it would take too much time to implement for example two-factor authentication system into this web application. Therefore we must create strong passwords.

### Links to the flaw in this project:
1. Password validators: https://github.com/oliverk2004/csbproject1/blob/main/config/settings.py#L90-L105

### FIX:
To fix this flaw is very simple. Uncomment the lines in *settings.py* file to use Django's strict password control. Now the app is requiring new user to set password within the limits of:
- Your password can’t be too similar to your other personal information.
- Your password must contain at least 8 characters.
- Your password can’t be a commonly used password.
- Your password can’t be entirely numeric.

**Note!** that *Log in* and *Sign up* are not working if the flaw 4 it not fixed. More information in *CSRF (FLAW 4)* down below. 

*There is no ability (yet) to change your password (except admin) which you would increase the security further...*

## CSRF (FLAW 4)
Cross-Site Request Forgery (CSRF) is a flaw that, is not so common nowadays because there is more secure web frameworks. In CSRF, user can send unauthorized web requests to a website through other website where the user is authenticated. This lets the attackers access the data as they were you as a user. CSRF attacks target functionality that causes a state change on the server, such as changing the victim's email address or password, or purchasing something [3]. CSRF attacks are possible in this project because built-in CSRF protection is disabled. 

### Links to the flaw in this project:
- Add CSRF tokens:  
  1. https://github.com/oliverk2004/csbproject1/blob/main/templates/registration/signup.html#L10
  2. https://github.com/oliverk2004/csbproject1/blob/main/polls/templates/polls/index.html#L17
  3. https://github.com/oliverk2004/csbproject1/blob/main/templates/registration/login.html#L14

- SameSite Cookies: https://github.com/oliverk2004/csbproject1/blob/main/config/settings.py#L132

### FIX:
Luckily this flaw is easy to fix. In *index.html*, *login.html* and *signup.html* files, remove the comments around {% csrf_token %} to enable the protection. Also, delete the final row in *settings.py* file "SESSION_COOKIE_SAMESITE = None". Now it is set back to default, enabling additional CSRF protection. 

## Cross-Site Scripting (FLAW 5)
Cross-Site Scripting attacks (XSS) are a type of injection, in which malicious scripts are injected into otherwise bening and trusted websites [5]. These attacks can enable session hijacking, allowing th attackers to impersonate users. This application contains a potential XSS vulnerability where user-supplied input is rendered in a template using the *safe* filter. This disables Django's automatic HTML escaping. As a result, an attacker can submit malicious code which is reflected back to the user's browser and executed when the page is rendered. 

### Links to the flaw in this project:
  1. https://github.com/oliverk2004/csbproject1/blob/main/polls/templates/polls/detail.html#L14-L15


### FIX:
To fix this, you have to delete 'safe' filter and either add Django's templates filter 'escape' or just delete 'safe' instead. This change ensures that user-supplied input is rendered as plain text rather than executable code. Therefore, Cross-Site Scripting attacks can be prevented. 


## Conclusion
Overall, this project was interesting to make, and I believe that I learned a lot new about the flaws with this hands-on project. The application itself, could be better and more wider when talking about the functions. 

## References:
1. https://owasp.org/Top10/2021/A01_2021-Broken_Access_Control/
2. https://cybersecuritybase.mooc.fi/module-2.3/1-security
3. https://owasp.org/www-community/attacks/csrf
4. https://owasp.org/Top10/2021/A07_2021-Identification_and_Authentication_Failures/#example-attack-scenarios
5. https://owasp.org/www-community/attacks/xss/
