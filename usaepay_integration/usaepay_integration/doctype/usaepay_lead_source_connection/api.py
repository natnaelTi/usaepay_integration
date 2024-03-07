from __future__ import unicode_literals
import frappe
import requests
import json
from frappe.model.document import Document

@frappe.whitelist(allow_guest=True)
def retrieve_usaepay_customer_list(api_details):
    # Log received API details
    frappe.logger().info(f"Received API details: {api_details}")
    
    # Parse JSON string to dictionary
    api_details_dict = json.loads(api_details)
    
    # Log parsed API details
    frappe.logger().info(f"Parsed API details: {api_details_dict}")
    
    # Extract API details
    api_type = api_details_dict.get("api_type")
    api_key = api_details_dict.get("api_key")
    api_pin = api_details_dict.get("api_pin")

    # Replace with actual USAePay API endpoint based on chosen API type
    api_url = "https://sandbox.usaepay.com/api/v2/customers"

    # Set authentication headers based on USAePay documentation
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic " + api_key,
    }

    # Make API call with appropriate HTTP method and headers
    response = requests.get(api_url, headers=headers)

    # Check for successful response and handle errors
    if response.status_code == 200:
        # Parse response data based on expected format
        customers = response.json()["customers"]

        # Process and format customer data for Frappe usage
        frappe_customer_data = []
        for customer in customers:
            frappe_customer_data.append({
                "name": customer["name"],
                "email": customer["email"],
                # ...other relevant customer fields
            })

        return frappe_customer_data
    else:
        frappe.log_error(f"USAePay API error: {response.status_code} - {response.text}")
        return response
