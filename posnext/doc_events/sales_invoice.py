import frappe


def validate_si(doc,method):
    if doc.is_return and doc.is_pos:
        doc.write_off_amount = 0