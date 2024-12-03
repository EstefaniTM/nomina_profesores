from odoo import models, fields, api
from odoo.exceptions import UserError

class Profesor(models.Model):
    _name = 'nomina_profesores.profesor'
    _description = 'Docente'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre del profesor', required=True)
    cedula = fields.Char(string='Cédula', required=True)
    cargo = fields.Char(string='Cargo del profesor')
    sueldo = fields.Monetary(string='Sueldo base', currency_field='currency_id')  
    extras = fields.Monetary(string='Extras', currency_field='currency_id')       
    bonos = fields.Monetary(string='Bonos', currency_field='currency_id')          
    sueldo_final = fields.Monetary(string='Sueldo final', compute='_compute_sueldo_final', store=True, currency_field='currency_id')
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', string="Currency", related='company_id.currency_id')
    currency_id1 = fields.Many2one('res.currency', string="Currency", default=lambda self: self.env.ref('base.USD'))


    @api.depends('sueldo', 'extras', 'bonos')
    def _compute_sueldo_final(self):
        for record in self:
            record.sueldo_final = (record.sueldo or 0.0) + (record.extras or 0.0) + (record.bonos or 0.0)