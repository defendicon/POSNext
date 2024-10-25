import frappe
from erpnext.accounts.doctype.sales_invoice.sales_invoice import (
    SalesInvoice,
    update_multi_mode_option
)
from six import iteritems
from frappe import msgprint
class PosnextSalesInvoice(SalesInvoice):
    @frappe.whitelist()
    def reset_mode_of_payments(self):
        if self.pos_profile:
            pos_profile = frappe.get_cached_doc("POS Profile", self.pos_profile)
            update_multi_mode_option(self, pos_profile)
            self.paid_amount = 0
