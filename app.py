from flask import Flask,abort,render_template, request, url_for, flash, redirect
from markupsafe import escape
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "Your_secret_string"

@app.route('/')

def hello():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())


@app.route('/about/')
def about():
    return '<h3>This is a Flask web application.</h3>'



@app.route('/capitalize/<word>/')
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))

@app.route('/add/<int:n1>/<int:n2>/')
def add(n1, n2):
    return '<h1>{}</h1>'.format(n1 + n2)



@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    try:
        return '<h2>Hi {}</h2>'.format(users[user_id])
    except IndexError:
        abort(404)



@app.route('/comments/')
def comments():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]

    return render_template('comments.html', comments=comments)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title=request.form['title']
        content=request.form['content']

        if not title:
            flash('Title is required')
        elif not content:
            flash('Content is required')
        else:
            messages.append({'title': title,'content': content})
            return redirect(url_for('index'))
    return render_template('create.html')



if __name__ == "__main__":

    app.run(debug=True)