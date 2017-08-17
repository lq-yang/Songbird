# -*- coding: UTF-8 -*-
import os
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from Config import Config
from Util import prepare_all
from Recommender import ModelFactory, Filter

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
            res = {}

            # 是否载入历史数据
            meet = form.meet.data

            # 业务领域数据
            lingyu = form.lingyu.data
            res['lingyu'] = model.recommend('lingyu', lingyu)
            res['lingyu'] = filter.get_sort(res['lingyu'])

            # 财务数据
            caiwu_res = {}
            caiwu_res["jingzichan"] = form.jingzichan.data
            caiwu_res["shouru"] = form.shouru.data
            caiwu_res["zhichu"] = form.zhichu.data
            caiwu_res["feiyong"] = form.feiyong.data
            res['caiwu'] = model.recommend('caiwu', caiwu_res)
            res['caiwu'] = filter.get_sort(res['caiwu'])

            return render_template("result.html", res=res)
        else:
            print form.errors
    return render_template("recommend.html", form=form)


@app.route('/info/<int:id>')
def show_info(id):
    return '<html><h1>This is the info of: %s</h1></html>' % id


if __name__ == '__main__':
    data_res, model_res = prepare_all()
    model = ModelFactory(data_res, model_res)
    filter = Filter(data_res['basic'])
    app.run(debug=True)
