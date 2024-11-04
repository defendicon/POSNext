import frappe


def validate_item(doc, method):
    for x in doc.custom_items:
        x.parent_item_name = doc.item_name