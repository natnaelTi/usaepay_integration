from __future__ import unicode_literals
import frappe
import requests
import json
import logging
from frappe.model.document import Document

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
    
@frappe.whitelist(allow_guest=True)
def check_customer(api_details, frappe_customer):
    # return f'Response: {"read"}'
    # Parse the incoming argument through JSON
    api_details_dict = json.loads(api_details)
    api_key = api_details_dict.get("api_key")
    # Replace with actual USAePay API endpoint based on chosen API type 
    api_url = "https://sandbox.usaepay.com/api/customers"

    # Set authentication headers based on USAePay documentation
    headers = {
        "Content-Type": "application/json", 
        "Authorization": "Basic" + api_key,
    }

    # Make API call with appropriate HTTP method and headers
    response = requests.get(api_url, headers=headers)
    logger.debug('Debug message from check_customer')
    # Log the response
    frappe.log_error(f'Response: {response}')
    # return response.status_code

    # # Check for successful response and handle errors
    if response.status_code == 200:
        # Parse response data based on expected format
        customers = response.json().get("customers", [])

        # Process and format customer data for Frappe usage
        usaepay_customer_list = []
        for customer in customers:
            usaepay_customer_list.append({
                "id": customer.get("custid"),
                "first_name": customer.get("first_name"),
                "last_name": customer.get("last_name"),
                "phone": customer.get("phone"),
                "email": customer.get("email"),
                "notes": customer.get("notes"),
                # ...other relevant customer fields
            })

        # Check if customers list is empty
        if not customers:
            return "No customers exist in USAePay", usaepay_customer_list

        # Check if frappe_customer exists in usaepay_customer_list
        for customer_data in usaepay_customer_list:
            if (customer_data["id"] == frappe_customer.get("id") and
                customer_data["first_name"] == frappe_customer.get("first_name") and
                customer_data["last_name"] == frappe_customer.get("last_name") and
                customer_data["email"] == frappe_customer.get("email") and
                customer_data["phone"] == frappe_customer.get("phone")):
                return "Customer exists in USAePay", customer_data

        return "Customer does not exist in USAePay", usaepay_customer_list
    else:
        return "Error: Unable to fetch customers from USAePay", []


# @frappe.whitelist(allow_guest=True)
# def handle_usaepay_response(**kwargs):
#     try:
#         # Extract relevant data from the POST request
#         transaction_id = kwargs.get('UMtranskey')
#         amount = kwargs.get('UMamount')
#         mode_of_payment = 'USAePay'
#         posting_date = 'UMorderdate'
#         party_type = 'Customer'
#         paid_amount = kwargs.get('UMamount')
        

#         # Create a new Payment Entry document
#         payment_entry = frappe.new_doc('Payment Entry')
#         payment_entry.payment_type = 'Receive'
#         payment_entry.mode_of_payment = payment_method
#         payment_entry.reference_no = transaction_id
#         payment_entry.paid_amount = amount
#         payment_entry.references.type = 'Sales Invoice'
#         payment_entry.references.name = kwargs.get('UMinvoice')

#         # You may need to set additional fields based on your ERPNext setup

#         # Save the Payment Entry document
#         payment_entry.insert(ignore_permissions=True)

#         frappe.db.commit()

#         return {"status": "success", "message": "Payment Entry created successfully"}

#     except Exception as e:
#         frappe.log_error("Error handling USAePay response: {}".format(e))
#         return {"status": "error", "message": "Error handling USAePay response"}