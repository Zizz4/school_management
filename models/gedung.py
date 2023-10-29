from odoo import fields, models, api


class SchoolGedung(models.Model):
    _name = 'school.gedung'

    name = fields.Char(string="Nama Gedung", required=True)
    kelas_ids = fields.One2many(string="Kelas", comodel_name="school.kelas", inverse_name="gedung_id")
    warna_gedung = fields.Char(string="Warna Gedung")
    panjang_gedung = fields.Integer(string="Panjang Gedung (m)")
    lebar_gedung = fields.Integer(string="Lebar Gedung (m)")
    lantai_gedung = fields.Integer(string="Jumlah Lantai", default=1)
    luas_gedung = fields.Integer(string="Luas (m)", compute="_compute_luas_gedung")

    @api.depends('panjang_gedung', 'lebar_gedung')
    def _compute_luas_gedung(self):
        for record in self:
            record.luas_gedung = record.panjang_gedung * record.lebar_gedung
