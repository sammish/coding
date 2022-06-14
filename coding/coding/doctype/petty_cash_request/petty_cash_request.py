# Copyright (c) 2022, sammish and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class PettyCashRequest(Document):
	@frappe.whitelist()
	def validate(self):
		if not self.employee_account:
			frappe.throw(""" Please make sure you set Petty Cash Account in Employee Master """)
	@frappe.whitelist()
	def on_update_after_submit(self):
		if self.sanctioned_amount > self.request_amount:
			frappe.throw("Sanctioned Amount must not be greater than Request Amount")
	@frappe.whitelist()
	def on_submit(self):
		self.generate_journal_entry()