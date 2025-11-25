{
    "name": "DIN5008 Report Overrides",
    "summary": "Replaces DIN5008 external layout, invoice and sale order reports.",
    "version": "1.0.0",
    "category": "Reporting",
    "author": "Michael Plöckinger",
    "company": "MPI GmbH",
    "website": "https://wottle.example.com",
    "license": "LGPL-3",
    "depends": [
        "account",
        "sale",
        "l10n_din5008"
    ],
    "data": [
        "views/external_layout_din5008.xml",
        "views/report_invoice_document.xml",
        "views/report_saleorder_document.xml"
    ],
    "installable": True,
    "application": False,
}
