# python-dev-intern-task-6-portfolio-website-with-flask
Python Developer Internship Task 6 (Portfolio Website with Flask)

## Installations ##
1. >>> pip install Flask
   
## Folder Structure to be Followed ##
1. static/css
2. static/js
3. static/images
4. templates/base.html - this is a layout for other HTML pages.
5. templates/index.html - this is the home page
6. templates/project.html - this is sub-page

## Website Details ##
1. This website contains home page with menus redirecting to sections within the same page. (route = /)
2. One internal page as sample of multi-page website. (route = /project)

## Contact Form ##
Type 1: It can be just an HTML form
The data can be captured in another endpoint (route = /contact)

Type 2: Flask has an extension that makes it easy to create web forms. WTForms is “a flexible forms validation and rendering library for Python Web development.” With Flask-WTF, we get WTForms in Flask.
 - WTForms includes security features for submitting form data.
 - WTForms has built-in validation techniques.
 - WTForms can be combined with Bootstrap to help us make clean-looking, responsive forms for mobile and desktop screens.
 - WTForms is a Python library.
 - Flask-WTF is a Flask extension that brings WTForms into Flask.

Install WTF
>>> pip install Flask-WTF -- import line changes as per field and validation in form
>>> pip install bootstrap-flask for styling, field by field rendering & styling
>>> CSRF, setting secret key {{ form.csrf_token }}
{{ render_form(socialProfileForm) }} creates form tag, csrf_token field, but we can mention form tag separately for method and action

## URLs ##
http://127.0.0.1:5000/
http://127.0.0.1:5000/project
