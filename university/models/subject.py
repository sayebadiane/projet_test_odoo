from odoo import api, fields, models, _, tools

class Subject(models.Model):
    _name = 'university.subject'

    name = fields.Char()
    code = fields.Char()

    department_id = fields.Many2one('university.department')
    professor_ids = fields.Many2many('university.professor',relation='subj_prof_rel',column1='name',column2='f_name')