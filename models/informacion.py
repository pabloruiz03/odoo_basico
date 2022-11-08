# -*- coding: utf-8 -*-

from odoo import models, fields, api

class informacion(models.Model):
    _name = 'odoo_basico.informacion'
    _description = 'Exemplo para infomacion'

    name = fields.Char(string="Título:")
    descripcion = fields.Text(string="A descripción:")
    alto_en_cms = fields.Integer(string="Alto en Centímetros:")
    ancho_en_cms = fields.Integer(string="Ancho en Centímetros:")
    longo_en_cms = fields.Integer(string="Longo en Centímetros:")


