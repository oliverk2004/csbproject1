# csbproject1

Cyber Security Base Project 1 -kurssin repositorio. 

Käytän tehtävässä OWASP listaa vuodelta 2021: https://owasp.org/Top10/2021/



## help for me with the project
### Django: Activating models
The three-step guide to making model changes:
- Change your models (in models.py)
- Run python manage.py makemigrations to create migrations for those changes
- Run python manage.py migrate to apply those changes to the database.

### A shortcut: render()
The render() function takes the request object as its first argument, a template as its second argument and a dictionary as its optional third argument. It returns an HTTPResponse object of the given template rendered with the given context.

### Adding stylesheet and styles overall
Make sure that in settings.py file you have 
```bash
STATIC_URL = '/static/'
```
not
```bash
STATIC_URL = 'static/'
```