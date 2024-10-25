import frappe
from frappe.utils import flt, get_datetime
@frappe.whitelist()
def get_pos_invoices(start, end, pos_profile, user):
    print("HEEEEEEEEEEEEEEEEERE")
    data = frappe.db.sql(
        """
    select
        name, timestamp(posting_date, posting_time) as "timestamp"
    from
        `tabSales Invoice`
    where
        owner = %s and docstatus = 1 and pos_profile = %s
    """,
        (user, pos_profile),
        as_dict=1,
    )

    data = list(filter(lambda d: get_datetime(start) <= get_datetime(d.timestamp) <= get_datetime(end), data))
    # need to get taxes and payments so can't avoid get_doc
    data = [frappe.get_doc("Sales Invoice", d.name).as_dict() for d in data]
    return data