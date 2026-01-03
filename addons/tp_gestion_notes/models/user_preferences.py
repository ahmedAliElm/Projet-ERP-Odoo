from odoo import models, fields, api

class ResUsers(models.Model):
    _inherit = 'res.users'
    
    # Theme preferences will be added after module is stable
    # tp_dark_mode = fields.Boolean(string="Mode sombre", default=False)
    # tp_primary_color = fields.Char(string="Couleur principale", default='#4a90e2')
    # tp_font_size = fields.Selection([...], string="Taille de police", default='14px')
    # tp_theme = fields.Selection([...], string="Thème", default='auto')
