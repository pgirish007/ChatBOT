from flask import Flask, request, render_template_string
import json
import importlib

app = Flask(__name__)

def set_attributes(instance, attributes):
    for attr, value in attributes.items():
        if isinstance(value, dict):
            nested_instance = getattr(instance, attr, None)
            if nested_instance is None:
                setattr(instance, attr, value)
            else:
                set_attributes(nested_instance, value)
        elif isinstance(value, (list, tuple)):
            setattr(instance, attr, value)
        else:
            setattr(instance, attr, value)

def create_element(element_data):
    element_type = element_data.pop('type')
    module_name = f'elements.{element_type.lower()}'  # e.g., elements.input_text
    class_name = ''.join([word.capitalize() for word in element_type.split('_')])  # e.g., InputText
    
    try:
        module = importlib.import_module(module_name)
        element_class = getattr(module, class_name)
    except (ModuleNotFoundError, AttributeError) as e:
        raise ValueError(f"Unknown element type: {element_type}")

    element_instance = element_class()
    set_attributes(element_instance, element_data)
    return element_instance

@app.route('/')
def index():
    return render_template_string(open('templates/index.html').read())

@app.route('/generate', methods=['POST'])
def generate():
    json_data = request.form.get('json_data')
    try:
        data = json.loads(json_data)
        collection = data.get('collection', {})
        elements = collection.get('elements', {})
        
        html_elements = []
        for section, element_list in elements.items():
            for element_data in element_list:
                html_elements.append(create_element(element_data).generate())
        
        form_html = "\n".join(html_elements)
        return render_template_string('<html><body>{{ form_html|safe }}</body></html>', form_html=form_html)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)


'''
example json:
{
    "collection": {
        "type": "test",
        "elements": {
            "title": [
                {"label": "Services", "name":"Girish","placeholder":"This is Girish Pandit", "type": "INPUT_TEXT"}
            ]
        }
    }
}
'''
