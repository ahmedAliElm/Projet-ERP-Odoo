from odoo import models, fields, api

class ThemeConfigWizard(models.TransientModel):
    _name = 'tp.theme.config.wizard'
    _description = 'Assistant de configuration du thème'
    
    dark_mode = fields.Boolean(string="Mode sombre", default=False)
    primary_color = fields.Char(string="Couleur principale", default='#4a90e2')
    font_size = fields.Selection([
        ('12px', 'Petit'),
        ('14px', 'Moyen'),
        ('16px', 'Grand'),
    ], string="Taille de police", default='14px')
    apply_to_all = fields.Boolean(string="Appliquer à toutes mes notes", default=True)
    
    def action_apply_theme(self):
        """Applique les paramètres du thème"""
        self.ensure_one()
        
        # For now, just apply to notes without user preferences
        # User preferences will be added once the module is stable
        if self.apply_to_all:
            user = self.env.user
            notes = self.env['tp.note.interne'].search([('auteur_id', '=', user.id)])
            notes.write({'is_dark_mode': self.dark_mode})
        
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Configuration du thème',
                'message': 'Vos préférences ont été enregistrées',
                'type': 'success',
                'sticky': False,
            }
        }
    
    def action_preview_theme(self):
        """Prévisualise le thème"""
        self.ensure_one()
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Aperçu',
                'message': 'Fonction de prévisualisation à venir',
                'type': 'info',
                'sticky': False,
            }
        }
