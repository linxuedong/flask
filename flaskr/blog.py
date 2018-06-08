from flask import (
    Blueprint, render_template
)
from flaskr.db import get_db

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT * FROM post'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)
