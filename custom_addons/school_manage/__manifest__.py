{
    "name": "school manage",
    "version": "14.0.1.0.0",
    "category": "School manage/Employees",
    "summary": "Centralize employee information",
    "description": """
This module contains all the common details of collage student.
    """,
    "website": "https://www.odoo.com/page/employees",
    "depends": [
        "sale",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/school_view.xml",
        "views/sale_view.xml",
    ],
    "demo": [],
    "installable": True,
    "auto_install": False,
    "application": True,
}
