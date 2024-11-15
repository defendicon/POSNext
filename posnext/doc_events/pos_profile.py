import frappe


def validate_pf(doc,method):
    if not doc.custom_edit_rate_and_uom:
        doc.custom_use_discount_percentage = 0
        doc.custom_use_discount_amount = 0