# -*- coding: utf-8 -*-

from odoo import models, fields, api

class informacion(models.Model):
    _name = 'odoo_basico.informacion'
    _description = 'Exemplo para infomacion'

    name = fields.Char(string="Título:")
    descripcion = fields.Text(string="A descripción:")


