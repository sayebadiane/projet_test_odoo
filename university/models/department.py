from odoo import api, fields, models, _, tools

class Department(models.Model):
    _name = 'university.department'

    name = fields.Char()
    code = fields.Char()

    professor_ids = fields.One2many('university.professor','department_id')
    subject_ids = fields.One2many('university.subject','department_id')

