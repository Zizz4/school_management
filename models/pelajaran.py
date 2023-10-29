from odoo import fields, models, api


class SchoolPelajaran(models.Model):
    _name = 'school.pelajaran'

    name = fields.Char('Mata Pelajaran', required=True)
    guru_ids = fields.Many2many('res.users', domain=[('is_guru', '=', True)], string="Pengajar")
