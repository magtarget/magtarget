# -*- coding: utf-8 -*-

from odoo import models, fields, api

class leaderboard(models.Model):
     _name = 'leaderboard.leaderboard'

     leaderboard_name = fields.Char(string="Leaderboard Name", required=True)
     Leaderboard_priority = fields.Integer()
     jm_test_field = fields.Float(compute="_value_pc", store=True)
     leaderboard_description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100