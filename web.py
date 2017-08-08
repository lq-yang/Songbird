# -*- coding: UTF-8 -*-
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap

from form import RecommendForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'xxcchh930729'
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    form = RecommendForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        is_meet = form.meet.data
        lingyu = form.lingyu.data
        print "yes" if is_meet else "no"
        flash(u"收到推荐请求")
        return redirect(url_for('result'))
    return render_template("recommend.html", form=form)


@app.route("/result", methods=['GET'])
def result():
    return render_template("result.html")


@app.route('/info/<int:id>')
def show_info(id):
    return '<html><h1>This is the info of: %s</h1></html>' % id


if __name__ == '__main__':
    app.run(debug=True)
