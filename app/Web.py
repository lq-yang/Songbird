# -*- coding: UTF-8 -*-
import os
import json
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from Config import Config
from Util import prepare_all
from Recommender import ModelFactory, FilterFactory, SearchFactory

# ---- initialize ----
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
csrf = CSRFProtect(app)
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

            meet = form.meet.data
            interest = form.interest.data

            # 历史捐献数据
            if meet:
                meet_name = form.meet_name.data
                res['rec'] = Model.recommend('rec', meet_name)
                res['rec'] = Filter.get_sort(res['rec'], asc=False)
            else:
                pass

            # 感兴趣基金数据
            if interest:
                interest_name = form.interest_name.data
                res['similarity'] = Model.recommend('similarity', interest_name)
                res['similarity'] = Filter.get_sort(res['similarity'], asc=False)
            else:
                pass

            # 业务领域数据
            lingyu = form.lingyu.data
            res['lingyu'] = Model.recommend('lingyu', lingyu)
            res['lingyu'] = Filter.get_sort(res['lingyu'], asc=True)

            # 财务数据
            caiwu_res = {}
            caiwu_res["jingzichan"] = form.jingzichan.data
            caiwu_res["shouru"] = form.shouru.data
            caiwu_res["zhichu"] = form.zhichu.data
            caiwu_res["feiyong"] = form.feiyong.data
            res['caiwu'] = Model.recommend('caiwu', caiwu_res)

            # 财务详细
            caiwu_ref = {}
            if form.jingzichan_x.data:
                caiwu_ref['jingzichan_x'] = float(form.jingzichan_x.data)
            if form.shouru_x.data:
                caiwu_ref['shouru_x'] = float(form.shouru_x.data)
            if form.zhichu_x.data:
                caiwu_ref['zhichu_x'] = float(form.zhichu_x.data)
            if form.feiyong_x.data:
                caiwu_ref['feiyong_x'] = float(form.feiyong_x.data)

            res['caiwu'] = Filter.get_sort(res['caiwu'], asc=True, array=caiwu_ref)

            # 所在地
            location = form.location.data
            if len(location) > 0:
                Filter.add_constraint('location', location)

            # 主管单位
            management = form.management.data
            if len(management) > 0:
                Filter.add_constraint('management', management)

            # 评价等级
            purity = form.purity.data
            if len(purity) > 0:
                Filter.add_constraint('purity', purity)

            # 排序方案
            plan = request.form['plan']
            if not plan or plan == "":
                plan = 3
            else:
                plan = plan.split('+')
                plan = min(plan)

            # 开始筛选和合并结果
            total = Filter.get_result(res, plan)

            return render_template("result.html", res=res, total=total)
        else:
            pass
        print form.errors
    return render_template("recommend.html", form=form)


@app.route('/info', methods=['GET', 'POST'])
def info():
    from Form import InfoForm
    form = InfoForm(request.form)
    res = {}
    if request.method == 'POST' and form.validate_on_submit():
        name = form.name.data

        # find project info
        res['project'] = Search.get_project_info(name)

        # find basic info
        res['basic'] = Search.get_basic_info(name)

    # 受欢迎基金
    popular = Filter.get_popular()

    # 热门标签基金
    hottag = Filter.get_hottag()

    return render_template("info.html", form=form, res=res, popular=popular, hottag = hottag)


@csrf.exempt
@app.route('/getinfo', methods=['POST'])
def getinfo():
    name = request.get_json()['name']
    name = name.strip()
    basic = Search.get_basic_info(name)
    project = Search.get_project_info(name)
    return json.dumps({'status': 'OK', 'basic': basic, 'project': project})

if __name__ == '__main__':
    data_res, model_res = prepare_all()
    Model = ModelFactory(data_res, model_res)
    Filter = FilterFactory(ref=data_res)
    Search = SearchFactory()
    app.run(debug=True)
