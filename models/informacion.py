# -*- coding: utf-8 -*-

from odoo import models, fields, api

class informacion(models.Model):
    _name = 'odoo_basico.informacion'
    _description = 'Exemplo para informacion'

    name = fields.Char(string="Título:")
    descripcion = fields.Text(string="A descripción:")
    peso = fields.Float(string="Peso en KGs.",default=4.3,digits=(6,2))
    sexo_traducido = fields.Selection([('Mujer','Muller'),('Hombre','Home'),('Otros','Outros')],string="Sexo")
    autorizado = fields.Boolean(string="¿Autorizado?", default=True)
    alto_en_cms = fields.Integer(string="Alto en Cms:")
    ancho_en_cms = fields.Integer(string="Ancho en Cms:")
    longo_en_cms = fields.Integer(string="Longo en Cms:")
    volume = fields.Float(compute="_volume",string="Volume en Metros Cúbicos",digits=(6,6), store=True)
    densidade = fields.Float(compute="_densidade",string="Densidade en Kgs/Metros Cúbicos", store=True)

    @api.depends('alto_en_cms', 'longo_en_cms', 'ancho_en_cms')
    def _volume(self):
      for rexistro in self:
          rexistro.volume =  (float(rexistro.alto_en_cms) * float(rexistro.longo_en_cms) *
                              float(rexistro.ancho_en_cms))/1000000
    @api.depends('peso', 'volume')
    def _densidade(self):
        for rexistro in self:
            if rexistro.volume != 0:
                rexistro.densidade = (float(rexistro.peso) / float(rexistro.volume))
            else:
                rexistro.densidade = 0