import frappe


def validate_item(doc, method):
    for x in doc.custom_items:
        x.parent_item_name = doc.item_name
        x.parent_item_description = doc.description
        x.parent_oem_part_number = doc.custom_oem_part_number