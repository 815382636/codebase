"""
    Flask 轻量级
    Werkzeug工具箱(路由模块)
    Jinja2(模板引擎)
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/<int:id>', methods=['GET', 'POST'])
def index(id=None):
    if id:
        return f'I am {id}'
    content = {
        str: '测试'
    }
    return render_template('index.html', **content)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
