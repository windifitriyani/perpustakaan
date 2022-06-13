from odoo import api, fields, models


class PengembalianBuku(models.Model):
    _name = 'pengembalian.buku'
    _description = 'New Description'

    name = fields.Char(compute='_compute_nama_peminjam', string='Nama Peminjam')
    id_pinjam = fields.Many2one(comodel_name='peminjaman.buku', string='ID Buku')
    
    @api.depends('id_pinjam')
    def _compute_nama_peminjam(self):
        for record in self:
            record.name = self.env['peminjaman.buku'].search([('id', '=', record.id_pinjam.id)]).mapped('peminjam')

    tgl_pengembalian = fields.Date(string='', default=fields.Date.today())

   