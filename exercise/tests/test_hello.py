import os
import tempfile
from flask import url_for

import pytest
from ..exercise import hello

@pytest.fixture
def client():
    db_fd, hello.app.config['DATABASE'] = tempfile.mkstemp()
    hello.app.config['TESTING'] = True
    client = hello.app.test_client()

    # with hello.app.app_context():
    #     hello.init_db()

    yield client

    os.close(db_fd)
    os.unlink(hello.app.config['DATABASE'])

def test_index(client):
    rv = client.get('/')
    assert b'Welcome to Index' in rv.data


def test_login(client, username, signature):
    return client.post(url_for('login'), data=dict(
        username='dawn',
        signature='signature signature signature signature'
    ), follow_redirects=True)
