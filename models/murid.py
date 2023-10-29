from odoo import fields, models, api


class SchoolMurid(models.Model):
    _inherit = 'res.partner'

    is_murid = fields.Boolean(string="Murid")
    nis = fields.Char(string="NIS")
    age = fields.Integer(string="Umur")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string="Gender")
    kelas_id = fields.Many2one(string="Kelas", comodel_name="school.kelas")
