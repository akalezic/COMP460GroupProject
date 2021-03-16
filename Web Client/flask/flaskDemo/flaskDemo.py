from flask import Flask, render_template, url_for, flash, redirect
from flaskDemo.forms import RegistrationForm, LoginForm, SearchForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

results1 = list()
result = dict()
result['title']="War"
result['description'] = "blah blah blah blah"
results1.append(result)
result=dict()
result['title']="Peace"
result['description'] = "blah blah blah blah"
results1.append(result)
result=dict()
result['title']="Crime"
result['description'] = "blah blah blah blah"
results1.append(result)
result=dict()
result['title']="Good things"
result['description'] = "blah blah blah blah"
results1.append(result)
result=dict()
result['title']="Bad things"
result['description'] = "blah blah blah blah"
results1.append(result)
result=dict()
result['title']="Fun stuff"
result['description'] = "blah blah blah blah"
results1.append(result)

@app.route("/")
@app.route("/search")
def search():
    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for('search'))
    return render_template('search.html', title='Search', form=form)

@app.route("/results")
def results():
    return render_template('results.html', results = results1)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('search'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('search'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
