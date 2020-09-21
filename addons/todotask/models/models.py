# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Todocategory(models.Model):
    _name = "todo.category"
    _description = "Todo tasks categories"
    
    name = fields.Char(string="Category name", required=True)

    

class todotask(models.Model):
    _name = 'todo.task'

    name = fields.Char(string="Things to do")
    is_done = fields.Boolean(string="Done")
    priority = fields.Selection([('todo', 'Things on hand'),('normal', 'Normal'),('urgent', 'Urgent')], default='todo', string='Urgent Level')
    deadline = fields.Datetime(string="Deadline")
    is_expired = fields.Boolean(string="Expired", compute="_compute_is_expired")
    category_id = fields.Many2one("todo.category", string="Category")
    
    @api.depends("deadline")
    @api.multi
    def _compute_is_expired(self):
        for rec in self:
            if rec.deadline:
                rec.is_expired = rec.deadline < fields.Datetime.now()
            else:
                rec.is_expired = False
    

#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100