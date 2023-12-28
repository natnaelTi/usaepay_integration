from . import __version__ as app_version
from __future__ import unicode_literals

app_name = "usaepay_integration"
app_title = "Usaepay Integration"
app_publisher = "Natnael Tilaye"
app_description = "USAePay and ERPNext integration module"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "natnaeltilaye30@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/usaepay_integration/css/usaepay_integration.css"
# app_include_js = "/assets/usaepay_integration/js/usaepay_integration.js"

# include js, css files in header of web template
# web_include_css = "/assets/usaepay_integration/css/usaepay_integration.css"
# web_include_js = "/assets/usaepay_integration/js/usaepay_integration.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "usaepay_integration/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "usaepay_integration.install.before_install"
# after_install = "usaepay_integration.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "usaepay_integration.uninstall.before_uninstall"
# after_uninstall = "usaepay_integration.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "usaepay_integration.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Includes all DocTypes listed in fixtures
# ---------------
fixtures = [
	"API Type",
	"USAePay Available APIs",
	"USAePay Lead Source Connection"
]

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"usaepay_integration.tasks.all"
#	],
#	"daily": [
#		"usaepay_integration.tasks.daily"
#	],
#	"hourly": [
#		"usaepay_integration.tasks.hourly"
#	],
#	"weekly": [
#		"usaepay_integration.tasks.weekly"
#	]
#	"monthly": [
#		"usaepay_integration.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "usaepay_integration.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "usaepay_integration.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "usaepay_integration.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Request Events
# ----------------
# before_request = ["usaepay_integration.utils.before_request"]
# after_request = ["usaepay_integration.utils.after_request"]

# Job Events
# ----------
# before_job = ["usaepay_integration.utils.before_job"]
# after_job = ["usaepay_integration.utils.after_job"]

# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"usaepay_integration.auth.validate"
# ]

def get_url():
    return "/api/method/usaepay_integration.usaepay_integration.handle_usaepay_response"

