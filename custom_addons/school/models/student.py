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


class Student(models.Model):
    _name = "student.student"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Student Management"

    name = fields.Char(string="Student Name")
    student_gender = fields.Selection(
        [("Female", "female"), ("Male", "male"), ("Others", "others")],
        string="Gender",
        required=True,
    )
    roll_no = fields.Integer(string="Roll No")
    address = fields.Char(string="Address")
    color = fields.Integer()
    teacher_ids = fields.One2many(
        "teacher.teacher", "student_id", string="teacher", index=True, tracking=1
    )
