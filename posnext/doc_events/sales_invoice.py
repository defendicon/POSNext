import frappe


def validate_si(doc,method):
    if doc.is_return and doc.is_pos:
        doc.update_outstanding_for_self = 0
        if doc.payments:
            doc.payments[0].amount = doc.rounded_total or doc.grand_total
        else:
            mop = frappe.db.get_all("POS Payment Method", {"default": True, "allow_in_returns": True, "parent": doc.pos_profile}, "mode_of_payment")
            if mop:
                doc.append("payments", {
                    "mode_of_payment": mop[0].mode_of_payment,
                    "amount": doc.rounded_total or doc.grand_total
                })


# @frappe.whitelist()
# def validate_taxes(doc, method):
#     if doc.taxes and doc.is_pos:
#         for tax in doc.taxes:
#             if not tax.included_in_print_rate:
#                 tax.included_in_print_rate = 1
#             else:
#                 tax.included_in_print_rate = 0
