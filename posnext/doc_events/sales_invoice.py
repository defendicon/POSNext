import frappe


def validate_si(doc,method):
    if doc.is_return and doc.is_pos:
        doc.update_outstanding_for_self = 0