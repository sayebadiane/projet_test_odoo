from odoo import api, fields, models, _, tools

class Professor(models.Model):
    _name = 'university.professor'

    l_name = fields.Char('Last name')
    f_name = fields.Char('Fistt name')
    sexe = fields.Selection([('male','Male'),('female','Female')])
    identity_card = fields.Char('identity card')
    address = fields.Text('Adress')
    birthday = fields.Date('Birthday')
    start_date = fields.Datetime('start date')
    email = fields.Char()
    phone =fields.Char()

    department_id = fields.Many2one('university.department')
    subject_id = fields.Many2one('university.subject')
    classroom_ids = fields.Many2many('university.classroom',relation='prof_class_rel',column1='f_name',column2='name')