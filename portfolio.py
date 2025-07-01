from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

import secrets
app = Flask(__name__)

# Flask allows us to set a “secret key” value. This value is used to prevent malicious hijacking of your form from an outside submission.
# Flask-WTF’s FlaskForm will automatically create a secure session with CSRF (cross-site request forgery) protection if this key-value is set and the csrf variable is set.
app.secret_key = secrets.token_urlsafe(16)

# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)
# Flask-WTF requires this line
csrf = CSRFProtect(app)

# one class for one form, starts with upper-case and then camel-case
class ProjectForm(FlaskForm):
    name = StringField('Share your project link', validators=[DataRequired(), Length(10, 40)])
    submit = SubmitField('Submit')
@app.route('/')
def home(): # it can be index also
    return render_template('index.html')

@app.route('/project')
def projects():
    project_form = ProjectForm()
    return render_template('project.html', ProjectForm=project_form)

@app.route('/contact', methods=['POST'])
def contact():

    # Get the form data as Python ImmutableDict datatype
    data = request.form

    if 'name' in data:
        return redirect(data['name'])
    else:
        ## Return the extracted information
        return {
            'name'     : data['contact_name'],
            'email' : data['contact_email'],
            'project'    : data['contact_project'],
            'message'      : data['contact_message']
        }

if __name__ == '__main__':
    app.run(debug=True)