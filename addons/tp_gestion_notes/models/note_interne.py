from odoo import models, fields, api
from datetime import datetime, timedelta

class TpNoteInterne(models.Model):
    _name = "tp.note.interne"
    _description = "Note Interne"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date_note desc, create_date desc'
    
    titre = fields.Char(string="Titre", required=True, tracking=True, index=True)
    contenu = fields.Html(string="Contenu")
    auteur_id = fields.Many2one("res.users", string="Auteur", default=lambda self: self.env.user, tracking=True, index=True)
    date_note = fields.Date(string="Date", default=fields.Date.today, tracking=True, index=True)
    
    statut = fields.Selection([
        ("brouillon", "Brouillon"),
        ("publie", "Publié"),
        ("archive", "Archivé"),
    ], string="Statut", default="brouillon", tracking=True, index=True)
    
    # Nouveaux champs améliorés
    priority = fields.Selection([
        ('0', 'Basse'),
        ('1', 'Normale'),
        ('2', 'Haute'),
        ('3', 'Urgente'),
    ], string="Priorité", default='1', tracking=True, index=True)
    
    is_favorite = fields.Boolean(string="Favori", default=False, tracking=True, index=True)
    
    date_echeance = fields.Date(string="Date d'échéance", tracking=True)
    
    is_overdue = fields.Boolean(string="En retard", compute="_compute_is_overdue", store=False)
    
    # Champs pour le thème
    theme_couleur = fields.Selection([
        ("bleu", "Bleu"),
        ("vert", "Vert"),
        ("rouge", "Rouge"),
        ("violet", "Violet"),
    ], string="Couleur du thème", default="bleu")
    
    is_dark_mode = fields.Boolean(string="Mode sombre", default=False)
    
    description = fields.Text(string="Description")
    
    # Champs calculés pour l'affichage
    display_name = fields.Char(string="Nom d'affichage", compute="_compute_display_name", store=False)
    
    @api.depends('titre', 'statut', 'priority')
    def _compute_display_name(self):
        for record in self:
            priority_icon = {
                '0': '',
                '1': '',
                '2': '⚡',
                '3': '🔥',
            }.get(record.priority, '')
            record.display_name = f"{priority_icon} {record.titre or 'Sans titre'}"
    
    @api.depends('date_echeance', 'statut')
    def _compute_is_overdue(self):
        today = fields.Date.today()
        for record in self:
            record.is_overdue = (
                record.date_echeance 
                and record.date_echeance < today 
                and record.statut != 'archive'
            )
    
    @api.constrains('date_note', 'date_echeance')
    def _check_dates(self):
        for record in self:
            if record.date_note and record.date_note < fields.Date.today():
                raise models.ValidationError("La date de la note ne peut pas être antérieure à la date d'aujourd'hui.")
            if record.date_echeance and record.date_note and record.date_echeance < record.date_note:
                raise models.ValidationError("La date d'échéance ne peut pas être antérieure à la date de la note.")

    def action_toggle_favorite(self):
        """Toggle le statut favori d'une note"""
        for record in self:
            record.is_favorite = not record.is_favorite
            message = "ajoutée aux favoris" if record.is_favorite else "retirée des favoris"
            record.message_post(
                body=f"Note {message}",
                subject=f"Favori - {record.titre}"
            )
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Favori',
                'message': f"Note {'ajoutée aux' if self.is_favorite else 'retirée des'} favoris",
                'type': 'success',
                'sticky': False,
            }
        }

    def action_publier(self):
        """Publie la note avec notification améliorée"""
        for record in self:
            if record.statut == 'brouillon':
                record.statut = "publie"
                record.message_post(
                    body=f"Note publiée le {fields.Date.today().strftime('%d/%m/%Y')}",
                    subject="Publication de note"
                )
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Succès',
                'message': f"{len(self)} note(s) publiée(s) avec succès",
                'type': 'success',
                'sticky': False,
            }
        }
    
    def action_archiver(self):
        """Archive la note avec notification"""
        for record in self:
            if record.statut == 'publie':
                record.statut = "archive"
                record.message_post(
                    body=f"Note archivée le {fields.Date.today().strftime('%d/%m/%Y')}",
                    subject="Archivage de note"
                )
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Succès',
                'message': f"{len(self)} note(s) archivée(s) avec succès",
                'type': 'success',
                'sticky': False,
            }
        }
    
    def action_restaurer(self):
        """Restaure une note archivée"""
        for record in self:
            if record.statut == 'archive':
                record.statut = "publie"
                record.message_post(
                    body=f"Note restaurée le {fields.Date.today().strftime('%d/%m/%Y')}",
                    subject="Restauration de note"
                )
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Succès',
                'message': f"{len(self)} note(s) restaurée(s) avec succès",
                'type': 'success',
                'sticky': False,
            }
        }

    def action_supprimer(self):
        """Supprime la note avec confirmation améliorée"""
        count = len(self)
        for record in self:
            record.unlink()
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Suppression',
                'message': f"{count} note(s) supprimée(s) avec succès",
                'type': 'success',
                'sticky': False,
            }
        }
    
    @api.model
    def get_statistics(self):
        """Retourne les statistiques des notes pour le dashboard"""
        user_notes = self.search([('auteur_id', '=', self.env.user.id)])
        stats = {
            'total': len(user_notes),
            'brouillon': len(user_notes.filtered(lambda n: n.statut == 'brouillon')),
            'publie': len(user_notes.filtered(lambda n: n.statut == 'publie')),
            'archive': len(user_notes.filtered(lambda n: n.statut == 'archive')),
        }
        
        # Ajouter les statistiques des nouveaux champs si disponibles
        try:
            stats['favoris'] = len(user_notes.filtered(lambda n: n.is_favorite))
        except:
            stats['favoris'] = 0
            
        try:
            stats['urgentes'] = len(user_notes.filtered(lambda n: n.priority == '3'))
        except:
            stats['urgentes'] = 0
            
        try:
            stats['en_retard'] = len(user_notes.filtered(lambda n: n.is_overdue))
        except:
            stats['en_retard'] = 0
            
        return stats
