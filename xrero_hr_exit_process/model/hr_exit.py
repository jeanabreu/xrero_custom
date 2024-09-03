#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from odoo.exceptions import UserError
# from openerp import models, fields, api, _
# from openerp.exceptions import Warning
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class hr_exit_checklist(models.Model):
    _name = 'hr.exit.checklist'
    _description = 'HR Exit CheckList'
    
    name = fields.Char(string="Name", required=True)
    responsible_user_id = fields.Many2one('res.users', string='Responsible User', required=True)
    notes = fields.Text(string="Notes")
    checklist_line_ids = fields.One2many('hr.exit.checklist.line','checklist_line_id', string='Checklist')

class hr_exit_checklist_line(models.Model):
    _name = 'hr.exit.checklist.line'
    _description = 'HR Exit CheckList Line'
    
    name = fields.Char(string="Name", required=True)
    checklist_line_id = fields.Many2one('hr.exit.checklist', invisible=True)

class hr_exit_line(models.Model):
    _name = 'hr.exit.line'
    _description = "Exit Lines"
    #_inherit = ['mail.thread', 'ir.needaction_mixin']
    _inherit = ['mail.thread', 'mail.activity.mixin']      #   odoo11
    _rec_name = 'checklist_id'
    _order = 'id desc'
    
    
    checklist_id = fields.Many2one('hr.exit.checklist', string="Checklist", required=True)
    notes = fields.Text(string="Remarks")
    state = fields.Selection(selection=[('draft', 'New'),\
                                        ('confirm', 'Confirmed'),\
                                        ('approved', 'Approved'),\
                                        ('reject', 'Rejected'),\
                                        ('cancel', 'Cancelled')],\
                                        string='State', default='draft', track_visibility='onchange')
    exit_id = fields.Many2one('hr.exit')
    responsible_user_id = fields.Many2one('res.users', string='Responsible User', required=True)
    # user_id = fields.Many2one(related="exit_id.user_id",string="User", type='many2one', relation='res.users', \
    #                     readonly=True, store=True)
    user_id = fields.Many2one(related="exit_id.user_id",string="User", type='many2one', relation='res_users', \
                        readonly=True, store=True)
    checklist_line_ids = fields.Many2many('hr.exit.checklist.line',
        'rel_exit_checklist_line', 'exit_line_id', 'checklist_exit_line_id',
        string='Checklist Lines')
    
    @api.onchange('checklist_id')
    def get_checklistline(self):
        self.checklist_line_ids = self.checklist_id.checklist_line_ids
    
    # @api.multi #odoo13
    def checklist_confirm(self):
        self.state = 'confirm'
    
    # @api.multi #odoo13
    def checklist_approved(self):
        self.state = 'approved'
    
    # @api.multi #odoo13
    def checklist_cancel(self):
        self.state = 'cancel'
    
    # @api.multi #odoo13
    def checklist_reject(self):
        self.state = 'reject'
        
class hr_exit(models.Model):
    _name = 'hr.exit'
    _description = "Exit"
    _rec_name = 'employee_id'
    #_inherit = ['mail.thread', 'ir.needaction_mixin']
    _inherit = ['mail.thread', 'mail.activity.mixin']      #   odoo11
    _order = 'id desc'

    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.user.company_id)
    employee_id = fields.Many2one('hr.employee', required=True, string="Employee")
    request_date = fields.Datetime('Request Date', readonly='1', \
                    default=fields.Datetime.now())
    # user_id = fields.Many2one('res.users', string='User', \
    #                     default=lambda self: self.env.user, \
    #                     states={'a_draft':[('readonly', False)]}, readonly=True)
    user_id = fields.Many2one('res.users', string='User', \
        default=lambda self: self.env.user)
    confirm_date = fields.Date(string='Confirm Date(Employee)', \
                        readonly=True, copy=False)
    dept_approved_date = fields.Date(string='Approved Date(Department Manager)', \
                        readonly=True, copy=False)
    validate_date = fields.Date(string='Approved Date(HR Manager)', \
                        readonly=True, copy=False)
    general_validate_date = fields.Date(string='Approved Date(General Manager)', \
                        readonly=True, copy=False)
    
    confirm_by_id = fields.Many2one('res.users', string='Confirm By', readonly=True, copy=False)
    dept_manager_by_id = fields.Many2one('res.users', string='Approved By Department Manager', readonly=True, copy=False)
    hr_manager_by_id = fields.Many2one('res.users', string='Approved By HR Manager', readonly=True, copy=False)
    gen_man_by_id = fields.Many2one('res.users', string='Approved By General Manager', readonly=True, copy=False)
    reason_for_leaving = fields.Char(string='Reason For Leaving',required=True, copy=False, readonly=True)
    last_work_date = fields.Date(string='Last Day of Work')
    survey = fields.Many2one('survey.survey', string="Interview", readonly=True)
    # response_id = fields.Many2one('survey.user_input', "Response", ondelete="set null", oldname="response")
    response_id = fields.Many2one('survey.user_input', "Response", ondelete="set null")
    partner_id = fields.Many2one('res.partner', "Contact", readonly=True)
    
    
    state = fields.Selection(selection=[
                        ('a_draft', 'Draft'), \
                        ('b_confirm', 'Confirmed'), \
                        ('c_approved_dept_manager', 'Approved by Dept Manager'),\
                        ('d_approved_hr_manager', 'Approved by HR Manager'),\
                        ('e_approved_general_manager', 'Approved by General Manager'),\
                        ('f_done', 'Done'),\
                        ('cancel', 'Cancel'),\
                        ('reject', 'Rejected')],string='State', \
                        readonly=True, help='', default='a_draft', \
                        track_visibility='onchange')
    notes = fields.Text(string='Notes')
    # manager_id = fields.Many2one('hr.employee', 'Department Manager', \
    #                     related='employee_id.department_id.manager_id', \
    #                     states={'a_draft':[('readonly', False)]}, readonly=True, store=True,\
    #                     help='This area is automatically filled by the user who \
    #                     will confirm the exit', copy=False)
    manager_id = fields.Many2one('hr.employee', 'Department Manager', \
                        related='employee_id.department_id.manager_id', \
                        readonly=True, store=True,\
                        help='This area is automatically filled by the user who \
                        will confirm the exit', copy=False)
    # department_id = fields.Many2one(
    #      related='employee_id.department_id', \
    #                     string='Department', type='many2one', relation='hr.department', \
    #                     readonly=True, store=True)
    department_id = fields.Many2one(
         related='employee_id.department_id', \
                        string='Department', type='many2one', relation='hr_department', \
                        readonly=True, store=True)
    # job_id = fields.Many2one(
    #     related='employee_id.job_id', \
    #                     string='Job Title', type='many2one', relation='hr.department', \
    #                     readonly=True, store=True)
    job_id = fields.Many2one(
        related='employee_id.job_id', \
                        string='Job Title', type='many2one', relation='hr_department', \
                        readonly=True, store=True)
    checklist_ids = fields.One2many('hr.exit.line', 'exit_id', string="Checklist")
    contract_id = fields.Many2one('hr.contract', string='Contract', readonly=False)
    contract_ids = fields.Many2many('hr.contract','hr_contract_contract_tag')
    
    # @api.multi #odoo13
    def action_makeMeeting(self):
        """ This opens Meeting's calendar view to schedule meeting on current applicant
            @return: Dictionary value for created Meeting view
        """
#         self.ensure_one()
#         partners = self.partner_id | self.user_id.partner_id | self.department_id.manager_id.user_id.partner_id
        
#         category = self.env.ref('hr_recruitment.categ_meet_interview')

        res = self.env['ir.actions.act_window']._for_xml_id('calendar.action_calendar_event')


#         res['context'] = {
#             'search_default_partner_ids': self.partner_id.name,
#             'default_partner_ids': partners.ids,
#             'default_user_id': self.env.uid,
#             'default_name': self.name,
#             'default_categ_ids': category and [category.id] or False,
#         }
        return res
    
    # @api.multi #odoo13
    def action_start_survey(self):
        self.ensure_one()
        # create a response and link it to this applicant
        if not self.response_id:
            response = self.env['survey.user_input'].create({'survey_id': self.survey.id, 'partner_id': self.partner_id.id})
            self.response_id = response.id
        else:
            response = self.response_id
        # grab the token of the response and start surveying
        # return self.survey.with_context(survey_token=response.token).action_start_survey()
        return self.survey.with_context(survey_token=response).action_start_survey()

    # @api.multi #odoo13
    def action_print_survey(self):
        """ If response is available then print this response otherwise print survey form (print template of the survey) """
        self.ensure_one()
        if not self.response_id:
            return self.survey.action_print_survey()
        else:
            response = self.response_id
            return self.survey.with_context(survey_token=response.token).action_print_survey()


    # @api.one #odoo13
    def get_contract_latest(self, employee, date_from, date_to):
        """
        @param employee: browse record of employee
        @param date_from: date field
        @param date_to: date field
        @return: returns the ids of all the contracts for the given employee that need to be considered for the given dates
        """
        contract_obj = self.env['hr.contract']
        clause = []
        #a contract is valid if it ends between the given dates
        clause_1 = ['&',('date_end', '<=', date_to),('date_end','>=', date_from)]
        #OR if it starts between the given dates
        clause_2 = ['&',('date_start', '<=', date_to),('date_start','>=', date_from)]
        #OR if it starts before the date_from and finish after the date_end (or never finish)
        clause_3 = ['&',('date_start','<=', date_from),'|',('date_end', '=', False),('date_end','>=', date_to)]
        clause_final =  [('employee_id', '=', employee.id),'|','|'] + clause_1 + clause_2 + clause_3
        contract_ids = contract_obj.search(clause_final,limit=1)
        return contract_ids
    
    @api.onchange('employee_id', 'state')
    def get_contract(self):
        contract_obj = self.env['hr.contract']
#        if not self.employee_id.address_home_id:
#            raise UserError(_('The employee must have a home address.'))
        # self.partner_id = self.employee_id.address_home_id.id
        all_contract_ids = contract_obj.search([('employee_id', '=', self.employee_id.id)])
        contract_ids = self.get_contract_latest(self.employee_id, self.request_date, self.request_date)
        if contract_ids:
            self.contract_id = contract_ids[0].id
            self.contract_ids = all_contract_ids.ids

    # @api.multi #odoo13
    def exit_approved_by_department(self):
        obj_emp = self.env['hr.employee']
        self.state = 'b_confirm'
        self.dept_approved_date = time.strftime('%Y-%m-%d')

    # @api.multi #odoo13
    def request_set(self):
        self.state = 'a_draft'
    
    # @api.multi #odoo13
    def exit_cancel(self):
        self.state = 'cancel'

    # @api.multi #odoo13
    def get_confirm(self):
        self.state = 'b_confirm'
        self.confirm_date = time.strftime('%Y-%m-%d')
        self.confirm_by_id = self.env.user.id
        
    # @api.multi #odoo13
    def get_apprv_dept_manager(self):
        self.state = 'c_approved_dept_manager'
        self.dept_approved_date = time.strftime('%Y-%m-%d')
        self.dept_manager_by_id = self.env.user.id
        checklist_data = self.env['hr.exit.checklist'].search([])
        for checklist in checklist_data:
            vals= {'checklist_id': checklist.id,
                   'exit_id':self.id,
                   'state': 'confirm',
                   'responsible_user_id': checklist.responsible_user_id.id,
                   'checklist_line_ids': [(6, 0, checklist.checklist_line_ids.ids)]}
            self.env['hr.exit.line'].create(vals)
        
    # @api.multi #odoo13
    def get_apprv_hr_manager(self):
        self.state = 'd_approved_hr_manager'
        self.validate_date = time.strftime('%Y-%m-%d')
        self.hr_manager_by_id = self.env.user.id
        for record in self.checklist_ids:
            if not record.state in ['approved']:
                raise UserError(_('You can not approved this request since there are some checklist to be approved by respected department'))
        
    # @api.multi #odoo13
    def get_apprv_general_manager(self):
        self.state = 'e_approved_general_manager'
        self.general_validate_date = time.strftime('%Y-%m-%d')
        self.gen_man_by_id = self.env.user.id
        
    # @api.multi #odoo13
    def get_done(self):
        self.state = 'f_done'
    
    # @api.multi #odoo13
    def get_reject(self):
        self.state = 'reject'
        
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
