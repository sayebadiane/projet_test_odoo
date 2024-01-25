# -*- coding: utf-8 -*-
from odoo.exceptions import UserError, ValidationError
from odoo import api, fields, models, _, tools

class Unikerp(models.Model):
        _inherit = 'res.partner'

        poduct_owner = fields.Boolean(string='Poduct Owner')
        scrum_master = fields.Boolean(string='Scrum Master')
        developper = fields.Boolean(string='Developper')
        stakeholders = fields.Boolean(string='Parties Prenantes')    

        @api.constrains('poduct_owner', 'scrum_master')
        def _check_profiles(self):
            for partner in self:
                if partner.poduct_owner and partner.scrum_master:
                    raise ValidationError("Un contact ne peut pas avoir à la fois le profil de Product Owner et de Scrum Master.")    
                
                
        @api.constrains('stakeholders')
        def _check_profile_consistency(self):
            if self.stakeholders and any([self.poduct_owner, self.scrum_master, self.developper]):
                raise models.ValidationError("Un contact avec le profil Parties Prenantes ne peut pas avoir un autre profil.")
                