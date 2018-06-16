# [QuickStart Document](http://flask.pocoo.org/docs/1.0/quickstart/)

## Run application

Flask command
```
export FLASK_APP=hello.py
flask run
```

or Python's `-m` switch with Flask
```
export FLASK_APP=hello.py
python -m flask run
```

## Debug Mode
在 Debug Mode 状态下，修改了代码不需要每次重启。
>  Debug support the server will reload itself on code changes

Debug 模式永远不要用于 Production machines。

## Route
```
@app.route('/projects/')
def projects():
    return 'The project page, which has trailing slash.'

@app.route('/about')
def about():
    return 'The about page without trailing slash.'
```
定义 route 时，像访问 projects 页面，url 中有没有结尾的 `/` 都会被 redirect 到 projects 页。
而像访问 about 页面，访问 url 为'/about/' 会看到 404 页面。

## URL Building
为什么使用 `url_for`：
1. 避免 hard-coding
2. 改变 url 时，不需要修改所有的 hard-coded URLs
3. 可以处理 `special characters and Unicode data`
4. 都为绝对路径


## HTTP Methods
> By default, a route only answers to `GET` requests. You can use the `methods` argument of the `route()` decorator to handle different HTTP methods.

## Template:
> Flask will look for templates in the `templates` folder.  


> Inside templates you also have access to the request, session and g [1] objects as well as the get_flashed_messages() function.
