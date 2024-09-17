# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ToDoTask(models.Model):
    _name = 'todo.task'
    _description = 'ToDo task'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # add chatter to model

    name = fields.Char(string='Task Name')
    assign_to_id = fields.Many2one('res.partner', string="Assign To")  # relation to res partner or res user
    description = fields.Text(string='Description')
    description_brief = fields.Text(string='Description Brief', compute='_compute_description_brief')
    date = fields.Date(string='Due Date')

    state = fields.Selection([
        ('new', 'New'),
        ('in-progress', 'In Progress'),
        ('completed', 'Completed'),
    ], default='new', string='status')

    @api.depends('description')
    def _compute_description_brief(self):
        for record in self:
            if record.description:
                # Truncate to 100 characters or your desired length
                record.description_brief = record.description[:100] + '...' if len(record.description) > 100 else record.description
            else:
                record.description_brief = ''
