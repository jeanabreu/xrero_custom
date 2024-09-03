# -*- coding: utf-8 -*-
#################################################################################
#
#   Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#   See LICENSE file for full copyright and licensing details.
#   License URL : <https://store.webkul.com/license.html/>
# 
#################################################################################
from odoo.tools.translate import _
from odoo import api, fields, models
import datetime

class ProductTemplate(models.Model):
	_inherit = 'product.template'

	not_returnable = fields.Boolean('Not Returnable')

class PosOrder(models.Model):
	_inherit = 'pos.order'

	is_return_order = fields.Boolean(string='Return Order',copy=False)
	return_order_id = fields.Many2one('pos.order','Return Order Of',readonly=True,copy=False)
	return_status = fields.Selection([('-','Not Returned'),('Fully-Returned','Fully-Returned'),('Partially-Returned','Partially-Returned'),('Non-Returnable','Non-Returnable')],default='-',copy=False,string='Return Status')

	@api.model
	def _process_order(self, order, draft, existing_order):
	#-------- for order return code start-----------------
		data = order.get('data')
		if data.get('is_return_order'):
			data['amount_paid'] = 0
			for line in data.get('lines'):
				line_dict = line[2]
				line_dict['qty'] = line_dict['qty']
				if line_dict.get('original_line_id'):
					original_line = self.env['pos.order.line'].browse(line_dict.get('original_line_id'))
					original_line.line_qty_returned += abs(line_dict['qty'])
			for statement in data.get('statement_ids'):
				statement_dict = statement[2]
				if data['amount_total'] <0:
					statement_dict['amount'] = statement_dict['amount'] * -1
				else:
					statement_dict['amount'] = statement_dict['amount']
			if data['amount_total'] <0:
				data['amount_tax'] = data.get('amount_tax')
				data['amount_return'] = 0
				data['amount_total'] = data.get('amount_total')
	#----------  for order return code end  --------
		res = super(PosOrder,self)._process_order(order,draft, existing_order)
		return res

	@api.model
	def _order_fields(self,ui_order):
		fields_return = super(PosOrder,self)._order_fields(ui_order)
		fields_return.update({
			'is_return_order':ui_order.get('is_return_order') or False,
			'return_order_id':ui_order.get('return_order_id') or False,
			'return_status':ui_order.get('return_status') or False,
			})
		return fields_return

class PosOrderLine(models.Model):
	_inherit = 'pos.order.line'
	
	line_qty_returned = fields.Integer('Line Returned', default=0)
	original_line_id = fields.Many2one('pos.order.line', "Original line")

	@api.model
	def _order_line_fields(self,line,session_id=None):
		fields_return = super(PosOrderLine,self)._order_line_fields(line,session_id)
		fields_return[2].update({'line_qty_returned':line[2].get('line_qty_returned','')})
		fields_return[2].update({'original_line_id':line[2].get('original_line_id','')})
		return fields_return

class PosSession(models.Model):
	_inherit = 'pos.session'

	def _pos_ui_models_to_load(self):
		result = super()._pos_ui_models_to_load()
		new_model_pos_payment = 'pos.payment'
		if new_model_pos_payment not in result:
			result.append(new_model_pos_payment)
		return result

	def _loader_params_pos_payment(self):
		domain_list = []
		model_fields = ['id', 'name', 'payment_method_id', 'amount']
		return {'search_params': {'domain': domain_list, 'fields': model_fields}}

	def _get_pos_ui_pos_payment(self, params):
		pos_payments = self.env['pos.payment'].search_read(**params['search_params'])
		return pos_payments

	def _loader_params_product_product(self):
		result = super()._loader_params_product_product()
		result['search_params']['fields'].extend(['not_returnable'])
		return result

	def _loader_params_pos_order(self):
		result = super()._loader_params_pos_order()
		domain_list = []
		if self.config_id.order_loading_options == 'n_days':
			today = datetime.datetime.today()
			validation_date = today + datetime.timedelta(days=(-1*int(self.config_id.number_of_days)))
			domain_list = [('date_order','>',fields.Datetime.to_string(validation_date)),
							('state', 'not in', ['draft', 'cancel']),
							('is_return_order', '=', False)]
		elif self.config_id.order_loading_options == 'current_session':
			domain_list = [('session_id', '=', self.name),
				('state', 'not in', ['draft', 'cancel']),
				('is_return_order', '=', False)]
		else:
			domain_list = [('state', 'not in', ['draft', 'cancel']),
				('is_return_order', '=', False)]
		result['search_params']['domain'] = domain_list
		result['search_params']['fields'].extend(['return_order_id', 'payment_ids', 'is_return_order', 'return_status', 'amount_total'])
		return result

	def _loader_params_pos_order_line(self):
		result = super()._loader_params_pos_order_line()
		result['search_params']['fields'].extend(['line_qty_returned'])
		return result