from odoo import api, fields, models


class Buku(models.Model):
    _name = 'buku'
    _description = 'Daftar Buku yang Tersedia'

    kode = fields.Char(string='Kode Buku', required=True)
    name = fields.Char(string='Judul Buku')
    penulis = fields.Char(string='Penulis Buku')
    penerbit = fields.Char(string='Penerbit Buku')
    tahun = fields.Char(string='Tahun Terbit')
    jenis_buku = fields.Selection(string='Jenis Buku', selection=[('novel', 'Novel'), ('buku cerita', 'Buku Cerita'), ('komik', 'Komik')])
    stok = fields.Integer(string='Stok Buku Tersedia')
    deskripsi = fields.Char(string='Deskripsi Buku')
       
    
    

