# -*- coding: utf-8 -*-
from odoo import http

# class Leaderboard(http.Controller):
#     @http.route('/leaderboard/leaderboard/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/leaderboard/leaderboard/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('leaderboard.listing', {
#             'root': '/leaderboard/leaderboard',
#             'objects': http.request.env['leaderboard.leaderboard'].search([]),
#         })

#     @http.route('/leaderboard/leaderboard/objects/<model("leaderboard.leaderboard"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('leaderboard.object', {
#             'object': obj
#         })