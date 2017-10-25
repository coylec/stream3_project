# Stream 3 Project

- Please note: registration of new users does not work due to a limitation with the email provider. Please see Bugs section below.

## Overview

### What is this site for?
This site was developed to demonstrate full stack web development using front-end and back-end technologies. 
It is a site developed as a prototype for a real world food company who were interested in having their commercial website updated and
adding a webstore.

### What does it do?
The site provides visitors with information about the company and the products they produce. It gives customers and suppliers
a means of contacting the company and allows the company to keep visitors informed of news about new products etc. through
their own blog. It also allows customers to purchase products through the webstore and pay via PayPal.

### How does it work?
The site is built using Django as the framework. The backend is built with Python. Users must register/login to
use the webstore. The frontend incorporates HTML5, CSS and Javascript to give the site a modern look and design.
I used several libraries and packages which are listed below to improve the design and functionality and make the site more secure.

### Testing
The site has been extensively tested in Chrome, Firefox and Safari. Chrome device mode was used to test the site for mobile responsiveness.

## Features

### Existing Features
- Scrolling Nav
- User registration and login
- Account recovery
- Webstore
- Contact Form
- Google Captcha to counter spam bots on contact form
- Blog
- Use of Google maps API
- Disqus comments

## Bugs

### Existing Bugs
- The reset password feature will allow you to go through all the steps needed to reset it but it is not currently changing the password stored in the database.
- Disqus stopped working with the app name I registered and was refusing to load on various attempts to register different names. I reverted to a generic app name that worked previously for the purposes of this project. However because it's a generic name comments from other sites might possibly show up given the way Disqus works.
- On smaller screen sizes the collapsible navigation menu does not close by itself when clicking links to sections of the homepage. It works as expected with other pages.
- The Online Shop and Blog links in the navigation menu do not highlight until the user starts to scroll down the page.
- The users order goes through and cart emptied before the PayPal payment has been processed. This would need to be fixed in a production version.
- At certain smaller screen sizes(IPad) the Account and Logout links on the dropdown navbar appear below the navbar section. It seems to have been caused by me changing the normal Bootstrap navbar breakpoints to fix another issue of the navbar expanding and covering the shopping cart at certain screen sizes.
- Currently new users will not be able to register an account unless they have been added as a verified email recipient with the email provider. Unfortunately after I deployed the site to Heroku I discovered that I cannot verify the domain
with Mailgun unless I have a custom domain. This means that I can only operate it on a sandbox account which will only send emails to verified recipients. 
The registration system for this site relies on the user receiving a verification link via email. The registration system does work so if 
you would like me to add you to the verified recipients for testing purposes please email me [here](mailto:coylec.devwork@gmail.com). Otherwise you can use the 
following credentials to login in order to view the shopping cart etc.:

- Username: test_live

- Password: testing12

## Tech Used

### Some of the tech used includes:
- [Django](https://www.djangoproject.com/)
    - I used Django as my framework for rapid development and pragmatic design 
- [bootstrap](https://getbootstrap.com/)
    - I used **Bootstrap** to give the site a modern, responsive design
- [bootswatch](https://bootswatch.com/)
    - I used an open source theme from **bootswatch** to help with styling
- [startbootstrap](https://startbootstrap.com/)
    - I used part of an open source theme from **startbootstrap** which was edited for my particular needs to help with the scrolling nav design
- [jquery](https://jquery.com/)
    - I used **jQuery** to simplify Javascript programming
- [django-bower](https://github.com/nvbn/django-bower)
    - I used **django-bower** for frontend package management
- [django-anymail](https://github.com/anymail/django-anymail)
    - I used **django-anymail** to integrate Mailgun into the backend to facilitate the sending of emails for the contact form and user registration
- [django-disqus](https://django-disqus.readthedocs.io/en/latest/)
    - I used **django-disqus** to integrate Disqus into the site to facilitate comments on the blog
- [django-forms-bootstrap](https://github.com/pinax/django-forms-bootstrap)
    - I used **django-forms-bootstrap** as a simple bootstap filter for the Django forms
- [django-paypal](https://github.com/spookylukey/django-paypal)
    - I used **django-paypal** to integrate PayPal as the payment system for the webstore
- [django-recaptcha](https://github.com/praekelt/django-recaptcha)
    - I used **django-recaptcha** to integrate a Google reCaptcha form field/widget into the contact form to help prevent spam
- [django-registration](https://django-registration.readthedocs.io/en/2.2/)
    - I used **django-registration** to provide user registration functionality which includes a confirmation email and account activation instructions
- [python-decouple](https://pypi.python.org/pypi/python-decouple)
    - I used **python-decouple** to separate the settings parameters from my source code
- [pillow](https://python-pillow.org/)
    - I used **pillow** to handle image storage and retrieval
- [mailgun](https://www.mailgun.com/)
    - I used the **Mailgun** API for sending emails
- [jquery-confirm](https://craftpip.github.io/jquery-confirm/)
    - I used **jQuery-Confirm** to help provide the user with a pop-up alert before they logout
    
### Getting the code up and running
1. Firstly you will need to clone this repository by running the `git clone <project's Github URL>` command
2. Setup a virtual environment for the project
3. After you've that done you'll need to install the dependencies listed in the requirements.txt file.
4. You will then need to create a .env file in your projects root directory. I have included a sample one which you can rename as .env and add your own secret keys etc. Alternatively you can edit the settings file directly.
5. You will now need to run the `python manage.py migrate` command.
6. Your can view your project on localhost:8000 by running `python manage.py runserver`.
7. Note, if you get an error saying 'no module paypal.standard' please try reinstalling django-paypal.

8. You can check out my site on Heroku [here](https://coylec-streamthree-project.herokuapp.com/).

