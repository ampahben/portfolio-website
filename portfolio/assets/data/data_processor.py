import json
import os
from jsonschema import validate, ValidationError

# JSON Schemas for validation
SCHEMAS = {
    "experience": {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "id": {"type": "number"},
                "company": {"type": "string"},
                "logo": {"type": "string"},
                "position": {"type": "string"},
                "duration": {"type": "string"},
                "location": {"type": "string"},
                "description": {"type": "string"},
                "tech_stack": {"type": "array", "items": {"type": "string"}},
                "achievements": {"type": "array", "items": {"type": "string"}}
            },
            "required": ["id", "company", "position", "description"]
        }
    },
    "projects": {
        "type": "object",
        "properties": {
            "cloud": {"$ref": "#/definitions/projectArray"},
            "cybersecurity": {"$ref": "#/definitions/projectArray"},
            "web": {"$ref": "#/definitions/projectArray"}
        },
        "definitions": {
            "projectArray": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "number"},
                        "title": {"type": "string"},
                        "image": {"type": "string"},
                        "description": {"type": "string"},
                        "tech_stack": {"type": "array", "items": {"type": "string"}},
                        "link": {"type": "string"}
                    },
                    "required": ["id", "title", "description"]
                }
            }
        }
    }
}

def validate_data_files():
    data_dir = "assets/data"
    for filename in os.listdir(data_dir):
        if filename.endswith('.json'):
            filepath = os.path.join(data_dir, filename)
            with open(filepath) as f:
                data = json.load(f)
            
            data_type = filename.split('.')[0]
            if data_type in SCHEMAS:
                try:
                    validate(instance=data, schema=SCHEMAS[data_type])
                    print(f"✅ {filename} is valid")
                except ValidationError as e:
                    print(f"❌ {filename} validation failed: {e.message}")
            else:
                print(f"⚠️ No schema for {filename}")

def generate_markdown_docs():
    """Generates documentation from the data files"""
    docs = "# Portfolio Data Documentation\n\n"
    
    # Experience
    with open("assets/data/experience.json") as f:
        exp_data = json.load(f)
    docs += "## Work Experience\n\n"
    for job in exp_data:
        docs += f"### {job['position']} at {job['company']}\n"
        docs += f"- Duration: {job['duration']}\n"
        docs += f"- Location: {job['location']}\n"
        docs += f"- Description: {job['description']}\n\n"
    
    # Projects
    with open("assets/data/projects.json") as f:
        proj_data = json.load(f)
    docs += "## Projects\n\n"
    for category in proj_data:
        docs += f"### {category.capitalize()} Projects\n"
        for project in proj_data[category]:
            docs += f"- {project['title']}: {project['description']}\n"
        docs += "\n"
    
    with open("DATA_DOCS.md", "w") as f:
        f.write(docs)
    print("Documentation generated in DATA_DOCS.md")

if __name__ == "__main__":
    print("Validating data files...")
    validate_data_files()
    
    print("\nGenerating documentation...")
    generate_markdown_docs()