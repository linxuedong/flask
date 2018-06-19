from flask import Flask

app = Flask(__name__)
app.config['TESTING'] = True

app.testing = True

app.config.update(
    TESTING = True,
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
)
