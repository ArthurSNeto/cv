import os
import markdown

css_path = os.path.join("templates", "style.css")
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

versions = [
    ("fullstack", "01_desenvolvedor_fullstack_senior", "Desenvolvedor Fullstack Sênior"),
    ("csharp", "02_desenvolvedor_csharp_senior", "Desenvolvedor C# / .NET Sênior"),
    ("angular", "03_desenvolvedor_angular_senior", "Desenvolvedor Angular Sênior"),
    ("qa", "04_qa_analyst_pleno", "QA Analyst Pleno")
]

md_html_parts = {}

for key, fname, label in versions:
    md_file = os.path.join("versoes", f"{fname}.md")
    with open(md_file, "r", encoding="utf-8") as f:
        md_text = f.read()
    
    # Parse Markdown
    html = markdown.markdown(md_text, extensions=['tables'])
    md_html_parts[key] = (fname, label, html)

# Generate individual standalone HTMLs
for key, (fname, label, html) in md_html_parts.items():
    standalone_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Arthur Santos Neto - {label}</title>
  <link rel="stylesheet" href="../templates/style.css">
  <style>
    .cv-container {{
      width: 210mm;
      margin: 20px auto;
      background: #fff;
      padding: 14mm 16mm;
      box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    }}
    @media print {{
      .cv-container {{
        width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
        box-shadow: none !important;
      }}
      .no-print {{ display: none !important; }}
      @page {{ size: A4; margin: 10mm 12mm; }}
    }}
    h1 {{ font-size: 18pt; color: #1e293b; text-transform: uppercase; margin-bottom: 2px; }}
    h2 {{ font-size: 10.5pt; color: #1e293b; border-bottom: 1px solid #cbd5e1; padding-bottom: 3px; margin-top: 12px; margin-bottom: 6px; text-transform: uppercase; }}
    h3 {{ font-size: 9.5pt; color: #0f766e; margin-top: 8px; margin-bottom: 2px; }}
    p {{ font-size: 8.8pt; line-height: 1.35; margin-bottom: 5px; text-align: justify; }}
    ul {{ padding-left: 18px; margin-bottom: 6px; }}
    li {{ font-size: 8.6pt; line-height: 1.3; margin-bottom: 3px; text-align: justify; }}
    hr {{ border: none; border-top: 2px solid #1e293b; margin: 8px 0; }}
    em {{ color: #64748b; font-size: 8pt; }}
    a {{ color: #0f766e; text-decoration: none; }}
  </style>
</head>
<body>
  <div class="toolbar no-print" style="position: sticky; top:0; background:#0f172a; color:#fff; padding:10px 20px; display:flex; justify-content:space-between; align-items:center;">
    <strong>Arthur Santos Neto - {label}</strong>
    <button onclick="window.print()" style="background:#0d9488; color:#fff; border:none; padding:8px 16px; border-radius:4px; font-weight:600; cursor:pointer;">
      Imprimir / Salvar em PDF (Ctrl+P)
    </button>
  </div>
  <div class="cv-container">
    {html}
  </div>
</body>
</html>"""
    out_path = os.path.join("versoes", f"{fname}.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(standalone_html)
    print(f"Generated {out_path}")

print("All standalone HTML files generated successfully.")
