from flask import Flask, render_template, url_for, redirect, flash
from forms import InputForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '0b0b6d1a'

@app.route('/')
def home():
     return render_template('home.html')

@app.route('/search', methods=['GET','POST'])
def search():
    form = InputForm()
    if form.validate_on_submit:
        flash(f'Sentiment analysis for the term : {form.searchphrase.data}!','success')
        return redirect(url_for('about'))
    return render_template('search.html',title='Search', form=form)

@app.route('/about')
def about():
     return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
