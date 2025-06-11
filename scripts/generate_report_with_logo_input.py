from fpdf import FPDF
import os
from datetime import datetime

class CustomPDF(FPDF):
    def __init__(self, logo_path, customer_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logo_path = logo_path
        self.customer_name = customer_name

    def header(self):
        if os.path.exists(self.logo_path):
            self.image(self.logo_path, 10, 8, 30)
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(40, 40, 40)
        self.cell(0, 10, f"Malware Analyse Report – {self.customer_name}", ln=True, align="C")
        self.ln(15)

    def chapter_title(self, title):
        self.set_font("Helvetica", "B", 12)
        self.set_fill_color(220, 220, 220)
        self.cell(0, 10, title, 0, 1, "L", fill=True)

    def chapter_body(self, body):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(20, 20, 20)
        self.multi_cell(0, 8, body)
        self.ln()

# Eingaben
customer_name = input("🔹 Kundennamen eingeben (z. B. 'Musterfirma AG'): ").strip()
logo_path = input("🖼  Pfad zum Logo (PNG/JPG) eingeben (z. B. '../scripts/logo.png'): ").strip()

# Pfade definieren
project_dir = "../projects/malware-sample-01"
ioc_path = os.path.join(project_dir, "ioc_summary.txt")
yara_path = os.path.join(project_dir, "yara_rule.yar")

# Inhalte laden
with open(ioc_path, "r") as f:
    ioc_text = f.read()

with open(yara_path, "r") as f:
    yara_text = f.read()

# PDF erzeugen
pdf = CustomPDF(logo_path=logo_path, customer_name=customer_name)
pdf.add_page()
pdf.chapter_title("IOC Summary")
pdf.chapter_body(ioc_text)
pdf.chapter_title("YARA-Regel")
pdf.chapter_body(yara_text)

# Speichern mit Datum & Kundenname
today = datetime.now().strftime("%Y-%m-%d")
filename = f"{project_dir}/report_{customer_name.replace(' ', '_')}_{today}.pdf"
pdf.output(filename)

print(f"✅ Report gespeichert unter: {filename}")
