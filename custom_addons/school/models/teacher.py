
from odoo import fields, models

class Teacher(models.Model):
    _name = 'teacher.teacher'
    _description = 'teacher.teacher'

    name = fields.Char(string="teacher Name" )
    language = fields.Char(string="Language")
    student_id = fields.Many2one("student.student",string="student")