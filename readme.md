- [ ] Neodškrtlo
- [x] Zaškrtlo


##
v Adminovi je uživatelské jméno "1234" a heslo "1234"

## Užitečné příkazy
`python -m pip install django==4.1.1`

`django-admin startproject SDAcia .`

`python3 manage.py runserver` - spuštění serveru

`python3 manage.py startapp viewer` - přidání aplikace

`python3 manage.py makemigrations` - vytvoření migrací

`python3 manage.py migrate` - aplikování migrací

`python3 manage.py shell`

`python manage.py createsuperuser` - vytvoření uživatele pro admin rozhraní

[Dokumentace QuerySet](https://docs.djangoproject.com/en/5.1/ref/models/querysets/)

# Přehled naší django aplikace
![django_overview](django_overview.jpg)

## Musím umět

- Stáhnout Python, nainstalovat django
- Vytvořit django projekt, vytvořit django applikaci
- Vytvořit ORM model ( `models.py` )
- Vytvořit a aplikovat migraci databáze/modelu `python3 manage.py makemigrations` a `python3 manage.py migrate`
- Přidat objekt do DB `Genre.objects.create(name='Horror')`
- Upravit objekt v DB ( vyhledej v prezentaci `.save()` )
- Smazat objekt v DB ( vyhledej v prezentaci `.delete()` ) 
- Vytvořit url v djangu ( `urls.py` )
- Vrátit html šablonu naplněnou daty  ( `view.py` - funkce `hello` )
- Dědění html šablony (v šabloně `form.html` je děděno od `base.html`)
- Filtrování objektů z DB, získání jednoho konkrétního objektu 
- Vytvořit HTML formulář - viz `form.html`
- Vytvořit formulář pomocí třídy (příklad v `forms.py`) a poté ho vykreslit pomocí FormView (viz prezentace vyhledej 'FormView')
- Vložit do šablony statický soubor (css, js, jpg, svg)

## Tipy
- id/primární klíč konkrétního záznamu získám jako **car.pk**
- nalezení tohoto záznamu pak mohu udělat jako **Car.objects.get(pk=car_pk)**

# TASK na 9.9.2024
- Udělat přihlašování a odhlašování [urls.py](https://github.com/alifuk/CZ21_Movies/blob/master/hollymovies/urls.py) řádky login a logout (nezapomenout importy)
- Udělat šablonu přihlašování [viewer/templates/registration/login.html](https://github.com/alifuk/CZ21_Movies/blob/master/viewer/templates/registration/login.html)
- Do SETTINGs nastavit (LOGIN_REDIRECT_URL a LOGOUT_REDIRECT_URL)(https://github.com/alifuk/CZ21_Movies/blob/master/hollymovies/settings.py) 
- Dát nějaké views za dekorátor `@login_required` či `LoginRequiredMixin` pokud se jedná o třídu - viz prezentace

# TASK na 10.9.2024 a 11.9.2024
- Pokud nemám TASK na 9.9.2024, tak udělat ten
- Udělat registraci, změnu hesla viz. urls.py, views.py, forms.py
- V admin rozhraní přidat oprávnění uživateli (není potřeba nic programovat, jen klikat na /admin)
- View nastavit požadované oprávnění (`PermissionRequiredMixin` nebo `@permission_required("polls.add_choice")`)
- Vyzkoušet, blokování stránky, pokud uživatel nemá oprávnění





