from odoo import fields, models, api
from datetime import date, datetime


class SchoolAbsensi(models.Model):
    _name = 'school.absensi'

    name = fields.Char(string="Pertemuan")
    day = fields.Date(string="Tanggal", required=True, default=date.today())
    date_start = fields.Datetime(string="Jam Mulai")
    date_end = fields.Datetime(string="Jam Selesai")
    state = fields.Selection([('undone', 'Belum Dimulai'), ('ongoing', 'Sedang Berlangsung'), ('done', 'Selesai')],
                             'Status',
                             default='undone')
    pelajaran_id = fields.Many2one(string='Pelajaran', comodel_name='school.pelajaran', required=True)
    kelas_id = fields.Many2one(string='Kelas', comodel_name='school.kelas', required=True)
    guru_id = fields.Many2one(string='Guru', comodel_name='res.users', domain=[('is_guru', '=', True)], required=True,
                              default=lambda self: self.env.user)
    murid_ids = fields.Many2many('res.partner', domain=[('is_murid', '=', True)], string="Murid")

    # Tampilkan Murid yang ada di kelas yang dipilih
    @api.onchange('kelas_id')
    def _onchange_kelas_id(self):
        for rec in self:
            return {'domain': {'murid_ids': [('id', 'in', rec.kelas_id.murid_ids.ids)]}}

    # Tampilkan Guru yang ada di pelajaran yang dipilih
    @api.onchange('pelajaran_id')
    def _onchange_pelajaran_id(self):
        for rec in self:
            return {'domain': {'guru_id': [('id', 'in', rec.pelajaran_id.guru_ids.ids)]}}

    def action_mulai_kelas(self):
        self.state = 'ongoing'
        self.date_start = datetime.now()

    def action_akhiri_kelas(self):
        self.state = 'done'
        self.date_end = datetime.now()
