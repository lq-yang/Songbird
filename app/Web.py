# -*- coding: UTF-8 -*-
import os
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from Config import Config

# ---- initialize ----
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)


# --------------------

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    from Form import RecommendForm
    form = RecommendForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        meet = form.meet.data
        # 业务领域数据
        lingyu = form.lingyu.data
        # 财务数据
        jingzichan = form.jingzichan.data
        shouru = form.shouru.data
        zhichu = form.zhichu.data
        feiyong = form.feiyong.data
        res = {}
        print "yes" if meet else "no"
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
