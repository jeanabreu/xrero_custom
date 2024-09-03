# -*- coding: utf-8 -*-


from copy import deepcopy
from odoo import models, api, _, fields

class AccountChartOfAccountReportIn(models.AbstractModel):
    _inherit = "account.coa.report"

    filter_branch = True