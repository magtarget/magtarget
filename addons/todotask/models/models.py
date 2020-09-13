# -*- coding: utf-8 -*-

from odoo import models, fields, api

class todotask(models.Model):
     _name = 'todo.task'

     name = fields.Char(string=u"Things to do")

     is_done = fields.Boolean(string=u"Done")
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100