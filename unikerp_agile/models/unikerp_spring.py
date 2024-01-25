from odoo import api, fields, models, _, tools

class UnikerpSpring(models.Model):
    _name = 'unikerp.spring'

    nom = fields.Char(string='nom',required=True)
    duree_sprint = fields.Selection([
        ('1 semaine', '1 semaine'),
        ('2 semaine', '2 semaine'),
        ('1 mois', '1 mois'),
    ],
      string=u"Durée Spring")