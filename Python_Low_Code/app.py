from flask import Flask, request, render_template_string
import json

app = Flask(__name__)

# Define Python classes for HTML elements
class InputText:
    def generate(self):
        return f'<input type="text" name="{self.name}" placeholder="{self.placeholder}">'

class InputDate:
    def generate(self):
        return f'<input type="date" name="{self.name}">'

class InputNumber:
    def generate(self):
        return f'<input type="number" name="{self.name}" min="{self.min_value}" max="{self.max_value}">'

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
    class_name = ''.join([word.capitalize() for word in element_type.split('_')])
    element_class = globals().get(class_name)

    if not element_class:
        raise ValueError(f"Unknown element type: {element_type}")

    element_instance = element_class()
    set_attributes(element_instance, element_data)
    return element_instance

@app.route('/')
def index():
    return render_template_string(open('index.html').read())

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
