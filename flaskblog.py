from flask import Flask, render_template, url_for, flash, redirect, session
from forms import  SearchForm
import tweepy
from textblob import TextBlob

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


twdata = []

def TweetBlast(searchterm):
    twdata.clear()
    consumer_key = 'SgJJpWvvQMB0QU2nrRM6by2DM'
    consumer_key_secret = '8aRUfDlqzuoOnY5yaGrcwkStVqoDvxo6aTutXM8LlNfkG0BUZz'
    access_token = '784635562946887681-Gc2iiIEa8QCMxSX9fIUClBARsTBGXdo'
    access_token_secret = 'zbBip5pTugOsMtXlZtGVxlnf8mgEOFlOoJFhLqk2HzlAX'
    auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    # search_term = input("Enter a search keyword: ")
    search_term = searchterm
    public_tweets = api.search(search_term)

    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
        user = {}
        user["text"]=tweet.text
        user["analysis"]=analysis.sentiment
        add_user(user)
    return twdata

def add_user(user):
  twdata.append(user)

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = SearchForm()
    if form.validate_on_submit():
        
        tweet_lis = TweetBlast(form.searchphrase.data)
        sum = 0
        
        for x in tweet_lis:
            if x['analysis'][0] > 0:
                sum = sum + 1
            else :
                sum = sum - 1
        if sum > 0:
            polarity = "Positive"
        else :
            polarity = "Negative"
           
        flash(f'Sentiment analysis for phrase {form.searchphrase.data}. Overall result : {polarity}', 'success')
        session['my_list'] = tweet_lis
        session.modified = True
        return redirect(url_for('result'))
    return render_template('home.html', title='Search', form=form)

@app.route("/result")
def result():
    return render_template('result.html')

# @app.route("/about")
# def about():
#     return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
