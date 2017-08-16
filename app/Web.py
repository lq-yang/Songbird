# -*- coding: UTF-8 -*-
import os
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from Config import Config
from Util import prepare_all
from Recommender import ModelFactory

# ---- initialize ----
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
CSRFProtect(app)
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

    if request.method == 'POST':
        if form.validate_on_submit():
            meet = form.meet.data

            # 业务领域数据
            lingyu = form.lingyu.data

            # 财务数据
            caiwu_res = {}
            caiwu_res["jingzichan"] = form.jingzichan.data
            caiwu_res["shouru"] = form.shouru.data
            caiwu_res["zhichu"] = form.zhichu.data
            caiwu_res["feiyong"] = form.feiyong.data
            caiwu_array = model.predict("caiwu", caiwu_res)


            return redirect(url_for('result'))
        else:
            print form.errors
    return render_template("recommend.html", form=form)


@app.route("/result", methods=['GET'])
def result():
    return render_template("result.html")


@app.route('/info/<int:id>')
def show_info(id):
    return '<html><h1>This is the info of: %s</h1></html>' % id


if __name__ == '__main__':
    data_res, model_res = prepare_all()
    model = ModelFactory(data_res, model_res)
    app.run(debug=True)













