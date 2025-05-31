from fpdf import FPDF
import os

def generate_pdf(title, category, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=title, ln=1, align='C')
    pdf.cell(200, 10, txt="Project Documentation", ln=2, align='C')
    pdf.cell(200, 10, txt=" ", ln=3)
    pdf.multi_cell(0, 10, txt=f"This is placeholder documentation for the {title} project. Replace this with your actual project documentation including architecture diagrams, implementation details, and any relevant technical specifications.")
    
    os.makedirs(f"assets/projects/{category}", exist_ok=True)
    pdf.output(f"assets/projects/{category}/{filename}-documentation.pdf")

# Generate all PDFs
projects = [
    ("VPC Setup", "cloud", "vpc-setup"),
    ("Private Subnet", "cloud", "private-subnet"),
    # Add all other projects in the same format
]

for title, category, filename in projects:
    generate_pdf(title, category, filename)

print("Generated all PDF placeholders!")