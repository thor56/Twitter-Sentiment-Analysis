from flask import Flask, render_template, url_for, flash, redirect, session
from forms import RegistrationForm, LoginForm, SearchForm
import tweepy
from textblob import TextBlob

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]
tweets_lis = []
tweet_dict = {}
consumer_key = 'SgJJpWvvQMB0QU2nrRM6by2DM'
consumer_key_secret = '8aRUfDlqzuoOnY5yaGrcwkStVqoDvxo6aTutXM8LlNfkG0BUZz'
access_token = '784635562946887681-Gc2iiIEa8QCMxSX9fIUClBARsTBGXdo'
access_token_secret = 'zbBip5pTugOsMtXlZtGVxlnf8mgEOFlOoJFhLqk2HzlAX'
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# search_term = input("Enter a search keyword: ")
search_term = "donald"
public_tweets = api.search(search_term)
res = public_tweets
userdata = { "data":[]}

def add_user(user):
  userdata["data"].append(user)

for tweet in public_tweets:
    tweet_dict['text'] = tweet.text
    analysis = TextBlob(tweet.text)
    tweet_dict['ana'] = analysis.sentiment
    tweets_lis.append(tweet_dict)
    user = {}
    user["name"]=tweet.text
    user["age"]=analysis.sentiment
    add_user(user)
    # print(tweets_lis)
    if analysis.sentiment[0]>0:
            print ('Positive')
    else:
            print ('Negative')
    print("")



#print(userdata)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/result")
def result():
    return render_template('result.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/search", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        flash(f'Sentiment analysis for phrase {form.searchphrase.data}!', 'success')
        session['my_list'] = tweets_lis
        print(tweets_lis)
        return redirect(url_for('result'))
    return render_template('search.html', title='Search', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
