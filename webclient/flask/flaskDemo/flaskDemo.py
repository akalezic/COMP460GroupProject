from flask import Flask, render_template, url_for, flash, redirect
from flaskDemo.forms import RegistrationForm, LoginForm, SearchForm
from flask import request

from flaskDemo.search import do_search


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
@app.route("/search", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        print(form.search.data)        
        return redirect(url_for('search'))

    return render_template('search.html', title='Search', form=form)


@app.route("/results", methods=['GET', 'POST'])
def results():
    search_string = request.form["search"]      
    results = do_search(search_string)
    

    print(results)
    return render_template('results.html', results = results)


if __name__ == '__main__':
    app.run(debug=True)
