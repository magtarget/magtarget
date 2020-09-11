# -*- coding: utf-8 -*-

from odoo import models, fields, api

class leaderboard(models.Model):
    _name = 'leaderboard.leaderboard'

    name = fields.Char(string="Leaderboard Name", required=True)
    Leaderboard_priority = fields.Integer()
    leaderboard_description = fields.Text()
    responsible = fields.Many2one('res.partner', string='Responsible', ondelete='set null', context={}, domain=[('share', '=', False)],)
# another domain filter to limit to internal users:    user = fields.Many2one('res.partner', string='Responsible', ondelete='set null', context={}, domain=[('employee_ids', '!=', False)],)
#    jm_test_field = fields.Float(compute="_value_pc", store=True)
     
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100