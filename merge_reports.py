# merge_reports.py - Merge all 5 project PDFs into one portfolio
from pypdf import PdfWriter
from pathlib import Path

# Define PDF paths in order
pdfs = [
    "project_1_covid_trials/covid_trials_eda.pdf",
    "project_2_drugs_side_effects/drugs_side_effects_eda.pdf",
    "project_3_life_expectancy/life_expectancy_eda.pdf",
    "project_4_ocd_patients/ocd_patients_eda.pdf",
    "project_5_tobacco_mortality/tobacco_mortality_eda.pdf",
]

writer = PdfWriter()

for pdf_path in pdfs:
    path = Path(pdf_path)
    if path.exists():
        writer.append(path)
        print(f"✓ Added : {pdf_path}")
    else:
        print(f"✗ Not found : {pdf_path}")

output_path = Path("unified_mentor_portfolio.pdf")
with open(output_path, "wb") as f:
    writer.write(f)

print(f"\n✓ Portfolio merged : {output_path}")
print(f"✓ Total pages      : {len(writer.pages)}")