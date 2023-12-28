from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

@frappe.whitelist(allow_guest=True)
def handle_usaepay_response(**kwargs):
    try:
        # Extract relevant data from the POST request
        transaction_id = kwargs.get('UMtranskey')
        amount = kwargs.get('UMamount')
        mode_of_payment = 'USAePay'
        posting_date = 'UMorderdate'
        party_type = 'Customer'
        paid_amount = kwargs.get('UMamount')
        

        # Create a new Payment Entry document
        payment_entry = frappe.new_doc('Payment Entry')
        payment_entry.payment_type = 'Receive'
        payment_entry.mode_of_payment = payment_method
        payment_entry.reference_no = transaction_id
        payment_entry.paid_amount = amount
        payment_entry.references.type = 'Sales Invoice'
        payment_entry.references.name = kwargs.get('UMinvoice')

        # You may need to set additional fields based on your ERPNext setup

        # Save the Payment Entry document
        payment_entry.insert(ignore_permissions=True)

        frappe.db.commit()

        return {"status": "success", "message": "Payment Entry created successfully"}

    except Exception as e:
        frappe.log_error("Error handling USAePay response: {}".format(e))
        return {"status": "error", "message": "Error handling USAePay response"}