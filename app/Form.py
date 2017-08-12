# -*- coding: UTF-8 -*-

from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectMultipleField, SubmitField, \
    validators, widgets, SelectField, StringField
from DbConsole import get_lingyu_data, get_caiwu_data


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


# recommender choices
class RecommendForm(FlaskForm):

    # 是否查询历史记录
    meet = BooleanField(u"查询是否有捐献记录？", [validators.DataRequired()])

    # 输入名称
    name = StringField(u"捐献者名称", [validators.Optional()])

    # 业务领域
    lingyu_choices = get_lingyu_data()
    lingyu = SelectMultipleField(u"感兴趣投资领域", [validators.Optional()],

                                 choices=lingyu_choices)
    # 财务
    caiwu_choice = get_caiwu_data()

    # 净资产
    jingzichane_choice = caiwu_choice['jingzichan']
    jingzichan = MultiCheckboxField(u"净资产", choices=jingzichane_choice)

    # 收入比列
    shouru_choice = caiwu_choice['shouru']
    shouru = SelectField(u"收入比例", choices=shouru_choice)

    # 支出比列
    zhichu_choice = caiwu_choice['zhichu']
    zhichu = SelectField(u"支出比例", choices=zhichu_choice)

    # 费用比列
    feiyong_choice = caiwu_choice['feiyong']
    feiyong = SelectField(u"费用比例", choices=feiyong_choice)

    submit = SubmitField(u"提交")
