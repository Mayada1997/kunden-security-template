
from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Malware Analyse Report", 0, 1, "C")

    def chapter_title(self, title):
        self.set_font("Arial", "B", 11)
        self.cell(0, 10, title, 0, 1, "L")

    def chapter_body(self, body):
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 8, body)
        self.ln()

# Datenquelle aus Projektordner
project_path = "../projects/malware-sample-01"
ioc_file = os.path.join(project_path, "ioc_summary.txt")
yara_file = os.path.join(project_path, "yara_rule.yar")

# Inhalt lesen
with open(ioc_file, "r") as f:
    ioc_data = f.read()

with open(yara_file, "r") as f:
    yara_data = f.read()

# Report erzeugen
pdf = PDF()
pdf.add_page()
pdf.chapter_title("IOC Summary")
pdf.chapter_body(ioc_data)
pdf.chapter_title("YARA-Regel")
pdf.chapter_body(yara_data)

# Speichern
output_path = os.path.join(project_path, "auto_generated_report.pdf")
pdf.output(output_path)
print(f"✅ Report erstellt unter: {output_path}")
