from odoo import api, fields, models, _, tools

class Student(models.Model):
    _name = 'university.student'

    l_name = fields.Char('Last name')
    f_name = fields.Char('Fistt name')
    sexe = fields.Selection([('male','Male'),('female','Female')])
    identity_card = fields.Char('identity card')
    address = fields.Text('Adress')
    birthday = fields.Date('Birthday')
    registration_date = fields.Datetime()
    email = fields.Char()
    phone =fields.Char()

    department_id = fields.Many2one('university.department')
    classroom_id = fields.Many2one('university.classroom')

