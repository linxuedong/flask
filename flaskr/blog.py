from flask import (
    Blueprint, render_template, flash, request, redirect, url_for, g, abort
)
from flaskr.db import get_db
from flaskr.auth import login_required

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT * FROM post'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = '请输入标题'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (author_id, title, body) VALUES (?, ?, ?)',
                (g.user['id'], title, body)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')


def get_post(id):
    post = get_db().execute(
        'SELECT * FROM post WHERE id = ?', (id,)
    ).fetchone()

    if post is None:
        abort(404, "文章不存在。")

    return post


@bp.route('/<int:id>')
def detail(id):
    post = get_post(id)
    return render_template('blog/detail.html', post=post)


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)
    print(post['id'])
    print(g.user['id'])
    if post['author_id'] != g.user['id']:
        abort(403, 'You are not author, you can\'t update.')

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if title is None:
            error = 'Title is not null.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)
