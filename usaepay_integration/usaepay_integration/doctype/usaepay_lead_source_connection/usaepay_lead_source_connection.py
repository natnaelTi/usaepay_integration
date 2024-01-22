# Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
@app.route('/process_payment', methods=['POST'])
class USAePayLeadSourceConnection(Document):
	def process_payment(api_details, post_data):
		try:
			# Construct headers with API key
			headers = {'Authorization': f'Bearer {api_details.api_key}'}

			# Make the POST request to the USAePay API
			response = requests.post('https://sandbox.usaepay.com/api/v2/transactions', json=post_data, headers=headers)


			if response.status_code == 200:
				return jsonify({'status': 'success', 'response': response.json()})
			else:
				return jsonify({'error': f'Failed to process payment. Status Code: {response.status_code}', 'response': response.text}), response.status_code

			# Added colon to fix "Expected expression" error
		except Exception as e:
			return jsonify({'error': str(e)}), 500