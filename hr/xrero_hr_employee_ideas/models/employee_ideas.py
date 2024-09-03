# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from odoo.tools.translate import _
from dateutil.relativedelta import relativedelta
import time
import datetime

AVAILABLE_PRIORITIES = [
    ('0', '0'),
    ('1', 'Very Low'),
    ('2', 'Low'),
    ('3', 'Average'),
    ('4', 'Good'),
    ('5', 'Very Good')
    ]

class HrEmployeeIdeas(models.Model):
    _name = 'hr.ideas'
    _description = "Employee Ideas"
    #_inherit = ['mail.thread', 'ir.needaction_mixin']
    #_inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin'] odoo11
    _inherit = ['mail.thread', 'mail.activity.mixin'] #odoo12
    
    
    name = fields.Char(readonly=True, string="Number", copy=True)
    title = fields.Char(required=True, string="Title", copy=True)
    detail = fields.Text(required=True)
    department_id = fields.Many2one('hr.department', string="Department", required=True)
    created_date = fields.Date(default=lambda *a: time.strftime('%Y-%m-%d'), string="Create Date",required=True)
    dead_line = fields.Date(required=False, string="End Date")
    company_id = fields.Many2one('res.company', required=True, 
                                 default=lambda self: self.env.user.company_id, 
                                 string='Company', readonly=True)
    employee_id = fields.Many2one('hr.employee', string="Employee", required=True, default=lambda self: self.env['hr.employee'].search([('user_id', '=', self.env.uid)], limit=1))
    ideas_review_ids = fields.One2many('employee.idea.review', 'ideas_review_id', string="Ideas_review_ids")
    total_vote = fields.Integer(compute="_votes_count")
    result = fields.Char(default="Not Decided", string="Result")
    idea_type_id = fields.Many2one('hr.idea.type', string="Idea Type", required=True)
    state = fields.Selection([
         ('draft', 'New'),
         ('approval_pending', 'Waiting for Approval'),
         ('open', 'Approved'),
         ('rejected', 'Rejected'),
         ('cancel', 'Closed')], default='draft',
        tracking=True,
        copy=False, string="Status")

    @api.onchange('employee_id')
    def get_department(self):
        self.department_id = self.employee_id.department_id.id

    # @api.model
    # def create(self, vals):
    #     # vals['name'] = self.env['ir.sequence'].next_by_code('hr.ideas')
    #     idea_type_id = vals.get('idea_type_id', False)
    #     ideas_id = self.env['hr.idea.type'].browse(idea_type_id)
    #     todaydate = datetime.date.today()
    #     now = datetime.datetime.now()
    #     start_date = datetime.datetime(now.year, now.month, 1)
    #     end_date = datetime.datetime(todaydate.year,todaydate.month,1)+relativedelta(months=1,days=-1)
    #     employee = vals['employee_id']#self.env['hr.employee'].search([('user_id','=',self.env.user.id)])
    #     employee_id = employee
    #     total_idea = self.env['hr.ideas'].search([('created_date','>=',start_date),('created_date','<=',end_date),('employee_id','=',employee),('idea_type_id','=',ideas_id.idea_type)])
    #     employee_ideas = len(total_idea)
    #     if employee_ideas >= ideas_id.idea_limit:
    #         raise ValidationError(_("You can not create more than (%s) ideas in current months.") % ideas_id.idea_limit)
    #     return super(HrEmployeeIdeas, self).create(vals)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            # vals['name'] = self.env['ir.sequence'].next_by_code('hr.ideas')
            idea_type_id = vals.get('idea_type_id', False)
            ideas_id = self.env['hr.idea.type'].browse(idea_type_id)
            todaydate = datetime.date.today()
            now = datetime.datetime.now()
            start_date = datetime.datetime(now.year, now.month, 1)
            end_date = datetime.datetime(todaydate.year,todaydate.month,1)+relativedelta(months=1,days=-1)
            employee = vals['employee_id']#self.env['hr.employee'].search([('user_id','=',self.env.user.id)])
            employee_id = employee
            total_idea = self.env['hr.ideas'].search([('created_date','>=',start_date),('created_date','<=',end_date),('employee_id','=',employee),('idea_type_id','=',ideas_id.idea_type)])
            employee_ideas = len(total_idea)
            if employee_ideas >= ideas_id.idea_limit:
                raise ValidationError(_("You can not create more than (%s) ideas in current months.") % ideas_id.idea_limit)
        return super(HrEmployeeIdeas, self).create(vals_list)
    
#   @api.multi
    @api.depends('ideas_review_ids')
    def _votes_count(self):
        self.total_vote = len(self.ideas_review_ids)

#   @api.multi
    def action_view_votes(self):
        self.ensure_one()
        #action = self.env.ref('hr_employee_ideas.action_employe_idea_review')
        action = self.env['ir.actions.act_window']._for_xml_id('xrero_hr_employee_ideas.action_employe_idea_review')
        # result = {
        #     'name': action.name,
        #     'help': action.help,
        #     'type': action.type,
        #   #  'view_type': action.view_type,
        #     'view_mode': action.view_mode,
        #     'target': action.target,
        #     'res_model': action.res_model,
        # }
        action['domain'] = "[('id','in',%s)]" % self.ideas_review_ids.ids
        return action
#         
#   @api.multi
    def action_voting_post(self):
        self.state = 'approval_pending'
        #employee = self.env['hr.employee'].search([('user_id','=',self.env.user.id)])
        #self.employee_id = employee
        #self.department_id = employee.department_id.id
        self.name = self.env['ir.sequence'].next_by_code('hr.ideas')

#   @api.one
    def action_open(self):
        self.state = 'open'
        partner_ids = []
        #group_id = self.env['ir.model.data'].get_object_reference('base', 'group_user')
        group_id = self.env['ir.model.data']._xmlid_to_res_id('base.group_user', raise_if_not_found=False)
        res_users = self.env['res.users']
        user_ids = res_users.sudo().search(
            [ ('groups_id', 'in', group_id)])
        partner_ids = list(set(u.partner_id.id for u in user_ids))
        self.message_post(
            body =_('%s idea is posted by %s! So please give your valuable \
                    time and vote for this idea if you are allowed to vote in idea type %s .') % (self.title, self.employee_id.name, self.idea_type_id.idea_type),
            partner_ids = partner_ids,
            # subtype_xml = 'mail.mt_comment'
            subtype_xmlid = 'mail.mt_comment'
        )
        return True
   
#   @api.one
    def action_rejected(self):
        self.state = 'rejected'
        
#   @api.multi
    def action_cancel(self):
        self.state = 'cancel'
        employee = self.env['hr.employee'].search([('user_id','=', self.env.user.id)])
#        if self.employee_id != employee:
#            raise ValidationError("You cannot close this idea.")
        very_good = 0
        good = 0
        average = 0
        low = 0
        very_low = 0
        for line in self.ideas_review_ids:
            if line.rating == '5':
                very_good += 1
            elif line.rating == '4':
                good += 1
            elif line.rating == '3':
                average += 1
            elif line.rating == '2':
                low += 1
            elif line.rating == '1':
                very_low += 1
        total_voting = very_good + good + average + low + very_low
        minimum_vot = self.idea_type_id.maximum_vote
        if minimum_vot <= total_voting:
            self.result = "Win"
        else:
            self.result = "Loss"

class IdeasReview(models.Model):
    _name = 'employee.idea.review'
    _description = 'Employee Idea Review'

    ideas_review_id = fields.Many2one('hr.ideas', string="Review")
    employee_id = fields.Many2one('hr.employee', string="Employee")
    department_id = fields.Many2one('hr.department', string="Department")
    comments = fields.Text()
    rating = fields.Selection(AVAILABLE_PRIORITIES, index=True)
    
class IdeaType(models.Model):
    _name = 'hr.idea.type'
    _rec_name = 'idea_type'
    _description = 'Idea Type'

    idea_type = fields.Char(string="Name", required=True)
    minimum_vote = fields.Integer(string="Minimum Votes", required=True,
                                  help="Set the minimum vote for the idea type.")
    maximum_vote = fields.Integer(string="Maximum Votes", required=True,
                                  help="Set the maximum vote for the idea type.")
    idea_limit = fields.Integer(default=5, string="Total Ideas", 
                                help="Set the total idea limits on current month for this type of ideas")
    department_ids = fields.Many2many('hr.department', string="Departments")
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
