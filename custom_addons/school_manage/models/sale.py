# -*- coding: utf-8 -*-

from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = "Sale Management"


    sale_description = fields.Char(string='Sale Description')