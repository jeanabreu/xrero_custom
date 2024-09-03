# -*- coding: utf-8 -*-

import time
from dateutil.relativedelta import relativedelta
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class AccountAgedTrialBalance(models.TransientModel):
    _name = 'account.aged.trial.balance'
    _inherit = 'account.common.partner.report'
    _description = 'Account Aged Trial balance Report'

    period_length = fields.Integer(string='Period Length (days)', required=True, default=30)
    journal_ids = fields.Many2many('account.journal', string='Journals', required=True)
    date_from = fields.Date(default=lambda *a: time.strftime('%Y-%m-%d'))

    # def pre_print_report(self, data):
    #     data['form'].update(self.read(['display_account'])[0])
    #     data['form'].update({
    #         'analytic_account_ids': self.analytic_account_ids.ids,
    #         'partner_ids': self.partner_ids.ids,
    #         'account_ids': self.account_ids.ids,
    #     })
    #     return data

    def _get_report_data(self, data):
        print('3333333333333')
        res = {}
        data = self.pre_print_report(data)
        print('data---------', data)
        data['form'].update(self.read(['period_length'])[0])
        period_length = data['form']['period_length']
        if period_length <= 0:
            raise UserError(_('You must set a period length greater than 0.'))
        if not data['form']['date_from']:
            raise UserError(_('You must set a start date.'))
        start = data['form']['date_from']
        for i in range(5)[::-1]:
            stop = start - relativedelta(days=period_length - 1)
            res[str(i)] = {
                'name': (i != 0 and (str((5 - (i + 1)) * period_length) + '-' + str((5 - i) * period_length)) or (
                            '+' + str(4 * period_length))),
                'stop': start.strftime('%Y-%m-%d'),
                'start': (i != 0 and stop.strftime('%Y-%m-%d') or False),
            }
            start = stop - relativedelta(days=1)
        data['form'].update(res)
        print('data111111', data)
        return data

    def _print_report(self, data):
        data = self._get_report_data(data)
        print('data222222222', data)
        return self.env.ref('accounting_pdf_reports.action_report_aged_partner_balance').\
            with_context(landscape=True).report_action(self, data=data)
