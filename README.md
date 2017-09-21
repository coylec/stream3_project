# Stream 3 Project

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
The site has been extensively tested in Chrome, Firefox and Safari. Also made use of some Django tests to text the blog.

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
    - I used **django-anymail** to integrate Mailgun into my backend to facilitate the sending of emails for the contact form and user registration.
- [django-disqus](https://django-disqus.readthedocs.io/en/latest/)
    - I used **django-disqus** to integrate Disqus into the site to facilitate comments on the blog
- [django-forms-bootstrap](https://github.com/pinax/django-forms-bootstrap)
    - I used **django-forms-bootstrap** as a simple bootstap filter for the Django forms
- [django-paypal](https://github.com/spookylukey/django-paypal)
    - I used **django-paypal** to integrate PayPal as the payment system for the webstore
- [django-recaptcha](https://github.com/praekelt/django-recaptcha)
    - I used **django-captcha** to integrate a Google reCaptcha form field/widget into the contact form to help prevent spam
- [django-registration](https://django-registration.readthedocs.io/en/2.2/)
    - I used **django-registration** to provide user registration functionality which includes a confirmation email and account activation instructions
- [python-decouple](https://pypi.python.org/pypi/python-decouple)
    - I used **python-decouple** to separate the settings parameters from my source code
- [pillow](https://python-pillow.org/)
    - I used **pillow** to handle image storage and retrieval
- [mailgun](https://www.mailgun.com/)
    - I used the **Mailgun** API for sending emails.
- [jquery-confirm](https://craftpip.github.io/jquery-confirm/)
    - I used **jQuery-Confirm** to help provide the user with a pop-up alert before they logout.
    
### Getting the code up and running


