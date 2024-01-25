from odoo import api, fields, models, _, tools

class Classroom(models.Model):
    _name = 'university.classroom'

    Classroom_name = fields.Char(string='name')
    code = fields.Char()

    student_ids = fields.One2many('university.student','classroom_id')
    professor_ids = fields.Many2many('university.professor',relation='class_prof_rel',column1='f_name',column2='name')
    subject_ids = fields.Many2many('university.subject',relation='class_subj_rel',column1='Classroom_name',column2='name')