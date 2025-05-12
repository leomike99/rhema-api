from flask import Blueprint, send_file
from fpdf import FPDF
import os

export_bp = Blueprint('export', __name__)

@export_bp.route('/api/export/pdf', methods=['GET'])
def export_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt="Liste de présence", ln=True, align='C')
    pdf.cell(200, 10, txt="Exemple de contenu exporté.", ln=True, align='L')

    output_path = "export_presence.pdf"
    pdf.output(output_path)

    return send_file(output_path, as_attachment=True)
