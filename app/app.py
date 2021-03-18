from flask import Flask
from flask import request, render_template, url_for, abort, redirect, session, escape
# from werkzeug import secure_filename

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
@app.route('/<name>')
def index(name=None):
    if 'username' in session:
        # return render_template('index.html', name=escape(session['username'])), 200
        return render_template('index.html', name=f"Great {escape(session['username'])}"), 200

    return render_template('index.html', name=name), 200

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            username = request.form['username']

            session['username'] = username

            return log_theUser_in(username)
        else:
            error = 'Invalid username/password'

        searchword = request.args.get('key', 'please')
        if searchword:
            return render_template('index.html', name="kracken")

    return render_template('login.html', error=error)

def valid_login(username, password):
    return username == "kracken"

def log_theUser_in(username):
    return redirect(url_for('index', name=username))
    # return render_template('index.html', name=username)

@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file1']
        f.save(f"uploads/{f.filename}")

@app.route('/home')
def home():
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404        

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)