# -*- coding: UTF-8 -*-

from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectMultipleField, SubmitField, \
                    validators, widgets


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class RecommendForm(FlaskForm):
    meet = BooleanField(u"查询是否有捐献记录？", [validators.DataRequired()])
    lingyu = SelectMultipleField(u"感兴趣投资领域", [validators.Optional()],
                                 choices=[('py', 'pytho'), ('java', 'Java')])
    jingzichane_choice = [(u"小型", 0), (u"大型", 1)]
    jingzichan = MultiCheckboxField(u"净资产", choices=jingzichane_choice)
    submit = SubmitField(u"提交")
