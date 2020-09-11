# -*- coding: utf-8 -*-

from odoo import models, fields, api

class leaderboard(models.Model):
    _name = 'leaderboard.leaderboard'

    name = fields.Char(string="Leaderboard Name", required=True)
    Leaderboard_priority = fields.Integer()
    leaderboard_description = fields.Text()
    user = fields.Many2one('res.partner', string='Publisher', ondelete='set null', context={}, domain=[],)

#    jm_test_field = fields.Float(compute="_value_pc", store=True)
     
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100