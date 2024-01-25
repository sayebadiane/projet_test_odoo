from odoo import api, fields, models, _, tools

class UnikerpEvents(models.Model):
    _name = 'unikerp.events'

    name = fields.Many2one('unikerp.spring',string="nom")
    evenement = fields.Selection([
        ('spring_planning', 'spring planning'),
        ('daily_stand_up', 'daily stand up'),
        ('spring_review', 'spring review'),
        ('sprint_retrospective', 'sprint retrospective')
    ],
    string="Evenement")
    product_owner_partner = fields.Many2one('res.partner', string='Product Owner Partner', domain=[('poduct_owner', '=', True)] )
    scrum_master_partner = fields.Many2one('res.partner', string='Scrum Master', domain=[('scrum_master', '=', True)] )
    developer_partner = fields.Many2many('res.partner','partner', string='Developer Partners', domain=[('developper', '=', True)] )
    parties_prenantes_partner = fields.Many2many('res.partner', string='parties prenants Partners', domain=[('stakeholders', '=', True)])
    duree_evenement = fields.Char( string='Durée evenment', compute='_compute_duree', store=True)

    @api.depends('name')
    def _compute_duree(self):
        for record in self:
            if record.name and record.evenement:
                if record.name.duree_sprint == '1 semaine':
                    if record.evenement== 'spring_planning':
                        record.duree_evenement = '1 heures'
                    elif record.evenement == 'daily_stand_up':
                        record.duree_evenement = '15 minutes'
                    elif record.evenement == 'spring_review':
                        record.duree_evenement = '1 heure'
                    elif record.evenement == 'sprint_retrospective':   
                        record.duree_evenement = '1 heures'
                if record.name.duree_sprint == '2 semaine':
                    if record.evenement== 'spring_planning':
                        record.duree_evenement = '2 heures'
                    elif record.evenement == 'sprint_review':
                        record.duree_evenement = '2 heures'
                    elif record.evenement == 'daily_stand_up':
                        record.duree_evenement = '15 minutes'
                    elif record.evenement == 'sprint_retrospective':   
                        record.duree_evenement = '2 heures'
                if record.name.duree_sprint == '1 mois':
                    if record.evenement== 'spring_planning':
                        record.duree_evenement = '4 heures'
                    elif record.evenement == 'sprint_review':
                        record.duree_evenement = '3 heures'
                    elif record.evenement == 'daily_stand_up':
                        record.duree_evenement = '15 minutes'
                    elif record.evenement == 'sprint_retrospective':   
                        record.duree_evenement = '4 heures'
            


   