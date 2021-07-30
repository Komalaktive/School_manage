# -*- coding: utf-8 -*-

from odoo import models, fields


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
        string="School Rank", help="This is school rank,", required=True, default=100
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
    
    _sql_constraints = [('name_unique','unique(name)',"please enter unique school name, Given school name already exists."),
    ('email_unique','unique(email)',"please enter unique email id, Given email id already exist."),
    ('phone_unique','unique(phone)',"please enter another phone number, Given phone number already exist.")]
  