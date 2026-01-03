{
    "name": "TP – Gestion des Notes Internes (Dark Theme)",
    "version": "3.2",
    "summary": "Module pédagogique pour gérer les notes internes avec thème sombre",
    "category": "Training",
    "author": "Votre Nom",
    "website": "https://www.votresite.com",
    "depends": ["base", "web", "mail"],
    "data": [
        "security/ir.model.access.csv",
        "views/note_views.xml",
        "views/date_filter_wizard.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "tp_gestion_notes/static/src/css/dark_theme.css",
            "tp_gestion_notes/static/src/css/components.css",
            "tp_gestion_notes/static/src/js/theme_config.js",
            "tp_gestion_notes/static/src/js/dark_theme.js",
        ],
    },
    "demo": [],
    "qweb": [],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
    "price": 0,
    "currency": "EUR",
}

