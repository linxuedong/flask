from flask import Flask, url_for, request, render_template, abort, make_response
from flask import render_template_string, session, redirect, g
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = b'hello'


@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html')
    return 'Welcome to Index.Please loggin in.'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        signature = request.form['signature']
        if not username:
            error = "Username should not empyt."
            return error
        else:
            session['username'] = username
            session['signature'] = signature
            return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/hello')
def hello():
    return render_template_string('hello world!!!')


@app.route('/hello/<string:name>')
def show_user(name):
    return 'Hello {} !'.format(name)


@app.route('/post/<int:post_id>')
def post_detail(post_id):
    return 'This is {} post.'.format(str(post_id))


@app.route('/<path:subpath>')
def show_subpath(subpath):
    if subpath == 'not_found':
        abort(404)
    return 'Subpath is: %s.' %subpath

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>页面不存在</h1>", 404

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('./staticfile/' + secure_filename(f.filename))
    return render_template('upload.html')


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login', next='/'))
    print(url_for('show_user', name='Dawn'))


with app.test_request_context('/hello', method='POST'):
    print('=====request=======')
    assert request.path == '/hello'
    assert request.method == 'POST'


@app.template_filter('string_cut')
def string_cut(s):
    return s[:10]


@app.context_processor
def utility_processor():
    def format_price(amount, currency=u'€'):
        return u'{0:.2f}{1}'.format(amount, currency)
    return dict(format_price=format_price)
