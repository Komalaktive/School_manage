# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class student(models.Model):
#     _name = 'student.student'
#     _description = 'student.student'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import fields, models

class StudentProfile(models.Model):
    _name = 'student.student'
    _description = 'student.student'

    name = fields.Char(string="Student Name" )
    student_id = fields.Many2one("school.profile",string="School Name")