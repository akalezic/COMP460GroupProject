from flask import Flask, render_template, url_for, flash, redirect, request
from flaskDemo.forms import SearchForm
from flaskDemo.search import do_search

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/")
@app.route("/search", methods=['GET', 'POST'])
def search():
    form = SearchForm() #creates search from object from created forms
    if form.validate_on_submit(): #if form vaild when enter we
        print(form.search.data)
        return redirect(url_for('search'))
    return render_template('search.html', title='Search', form=form)

@app.route("/results", methods=['GET', 'POST'])
def results():
    search_string = request.form["search"]      
    results = do_search(search_string)
    print(results)
    form = SearchForm() #creates search from object from created forms
    if form.validate_on_submit(): #if form vaild when enter we
        print(form.search.data)
    return render_template('results.html', results = results, form=form)

if __name__ == '__main__':
    app.run(debug=True)
