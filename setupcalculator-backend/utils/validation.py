# backend/utils/validation.py
import json

with open('setup_template.json') as f:
    SETUP_TEMPLATE = json.load(f)

def validate_setup(data):
    errors = []
    for category, params in SETUP_TEMPLATE['categories'].items():
        for param_name, param_def in params['parameters'].items():
            value = data.get(param_name)
            if value is None:
                continue
                
            if not (param_def['min'] <= value <= param_def['max']):
                errors.append(f"{param_def['name']} muss zwischen {param_def['min']} und {param_def['max']} liegen")
    
    return errors