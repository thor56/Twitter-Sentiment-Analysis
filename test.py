from flask import Flask, render_template, url_for, redirect
from forms import InputForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '0b0b6d1a'

@app.route('/', methods=['GET','POST'])
def home():
    form = InputForm()
    if form.validate_on_submit:
        return redirect(url_for('about'))
    return render_template('home.html', form=form)

@app.route('/about')
def about():
     return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
