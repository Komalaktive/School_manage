# -*- coding: utf-8 -*-

from odoo import models, fields, api , _
from openerp.exceptions import ValidationError


class StudentInfo(models.Model):
    _name = "school.profile"
    _description = "School Management"

    name = fields.Char(string="School Name", help="this is school Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    is_virtual_class = fields.Boolean(
        string="Virtual class support?", help="this is boolean flag which will"
    )
    school_rank = fields.Integer(
        string="School Rank", help="This is school rank,", default=100
    )
    result = fields.Float(string="Result", help="this is tool tip")
    address = fields.Text(
        string="Address",
        help="this is school address",
        default="This is a default address",
    )
    Principle_msg = fields.Text(string="Principle_msg")
    Teacher_msg = fields.Text(string="Teacher_msg")
    establish_date = fields.Date(string="Establish Date")
    open_date = fields.Datetime(
        "Open Date", help="this is tool tip and select date and time"
    )
    school_type = fields.Selection(
        [("public", "public school"), ("private", "private school")],
        string="Type of school",
        required=True,
        default="public",
    )
    documents = fields.Binary(string="Documents")
    document_name = fields.Char(string="File Name")
    school_image = fields.Image(
        string="upload school Image",
        max_width=50,
        max_height=50,
        verify_resolution=True,
    )
    school_description = fields.Html(string="Description")
    # contact_id = fields.Many2one("res.partner", string="Contact detail")
    school_id = fields.Many2one("school.profile", string="Contact detail")
    # school_reference = fields.Many2one("student.student", string="reference")
    res_partners =  fields.Many2many("res.partner", string="Res partner")
    student_gender = fields.Selection(
        [("Female", "female"), ("Male", "male"), ("Others","others")],
        string="Gender",
        required=True,
    )
    active = fields.Boolean(string="active", default=True)

    @api.model_create_multi
    def create(self, values):   
        print("values of created method ",values)
        print("self",self)    
        rtn = super(StudentInfo, self).create(values)
        print("Return statement", rtn)
        return rtn
    def write(self, values):
        print("values .....",values)
        rtn = super(StudentInfo, self).write(values)
        print("Return data ",rtn)
        return rtn


    # _sql_constraints = [('name_unique','unique(name)',"please enter unique school name, Given school name already exists."),
    # ('email_unique','unique(email)',"please enter unique email id, Given email id already exist."),
    # ('phone_unique','unique(phone)',"please enter another phone number, Given phone number already exist."),
    # ('school_rank', 'CHECK (school_rank>1)', 'School Rank must be positive!')]


    @api.constrains('school_rank')
    def _check_something(self):
        for record in self:
            if record.school_rank < 4:
                raise ValidationError("u r not able to get this rank!!!!")

    @api.constrains('phone')
    def _check_phone_number(self):
        for rec in self:
            if rec.phone and len(rec.phone) != 10:
                raise ValidationError(("Must be enter 10 Digits of Mobile Number!!!!!!!!!!!!"))
        return True

        