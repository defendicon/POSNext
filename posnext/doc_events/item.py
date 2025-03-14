import frappe


def validate_item(doc, method):
    for x in doc.custom_items:
        x.parent_item_name = doc.item_name
        x.parent_item_description = doc.description
        x.parent_oem_part_number = doc.custom_oem_part_number


@frappe.whitelist()
def get_product_bundle_with_items(item_code):
    bundle = frappe.db.get_value("Product Bundle", {"new_item_code": item_code}, "name")

    if not bundle:
        return None  

    bundle_doc = frappe.get_doc("Product Bundle", bundle)

    bundle_items = []
    for item in bundle_doc.items:
        bundle_items.append({
            "item_code": item.item_code,
            "qty": item.qty,
            "uom": item.uom
        })

    return {
        "name": bundle_doc.name,
        "new_item_code": bundle_doc.new_item_code,
        "items": bundle_items
    }