coded_flows_metadata = {
    "display_name": "LOAD ENV",
    "description": "Loading environement variables.",
    "type": "control",
    "icon": "settings-code",
    "requirements": ["python-dotenv"],
    "options": [
        {
            "name": "filename",
            "display_name": "File name",
            "type": "input",
            "default": ".env",
        }
    ],
}


def load_env(options):
    pass
