from odoo import api, fields, models


class PeminjamanBuku(models.Model):
    _name = 'peminjaman.buku'
    _description = 'New Description'


    name = fields.Char(string='ID Peminjam', required=True)
    tanggal_pinjam = fields.Datetime('Tanggal Peminjaman', default = fields.Datetime.now)
    tanggal_kembali = fields.Date(string='Tanggal Pengembalian', default = fields.Date.today())
    peminjam = fields.Char(string='Peminjam')