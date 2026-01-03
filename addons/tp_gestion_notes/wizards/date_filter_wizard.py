from odoo import models, fields, api
from datetime import datetime

class DateFilterWizard(models.TransientModel):
    _name = 'tp.date.filter.wizard'
    _description = 'Assistant de filtrage par date'
    
    date_selection = fields.Date(
        string="Sélectionner une date",
        required=True,
        default=fields.Date.today,
        help="Sélectionnez la date pour afficher toutes les notes de cette date"
    )
    
    def action_show_notes_by_date(self):
        """Ouvre une vue filtrée des notes pour la date sélectionnée"""
        self.ensure_one()
        
        return {
            'name': f'Notes du {self.date_selection.strftime("%d/%m/%Y")}',
            'type': 'ir.actions.act_window',
            'res_model': 'tp.note.interne',
            'view_mode': 'tree,form,kanban',
            'domain': [('date_note', '=', self.date_selection)],
            'context': {
                'search_default_date_note': self.date_selection,
                'default_date_note': self.date_selection,
            },
            'target': 'current',
        }

