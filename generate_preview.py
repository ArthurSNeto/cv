import os
import markdown

versions_info = [
    ("fullstack", "01_desenvolvedor_fullstack_senior", "1. Desenvolvedor Fullstack Sênior", "Arthur_Santos_Neto_Desenvolvedor_Fullstack_Senior.pdf"),
    ("csharp", "02_desenvolvedor_csharp_senior", "2. Desenvolvedor C# / .NET Sênior", "Arthur_Santos_Neto_Desenvolvedor_CSharp_Senior.pdf"),
    ("angular", "03_desenvolvedor_angular_senior", "3. Desenvolvedor Angular Sênior", "Arthur_Santos_Neto_Desenvolvedor_Angular_Senior.pdf"),
    ("qa", "04_qa_analyst_pleno", "4. QA Analyst Pleno", "Arthur_Santos_Neto_QA_Analyst_Pleno.pdf")
]

sections_html = []

for v_id, fname, label, pdf_name in versions_info:
    md_file = os.path.join("versoes", f"{fname}.md")
    with open(md_file, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Convert markdown to html
    html_content = markdown.markdown(md_text, extensions=['tables', 'nl2br'])
    
    # Inject page break before Dragon / mid-experience to guarantee clean 2-page split
    # Dragon is the 4th experience
    target_heading = "<h3>Desenvolvedor de Software — PrintWayy (Sistema Dragon)</h3>"
    if target_heading in html_content:
        html_content = html_content.replace(target_heading, f'<div class="page-break"></div>\n{target_heading}')
    elif "PrintWayy (Sistema Dragon)" in html_content:
        # Fallback if markdown generated slightly different header
        idx = html_content.find("PrintWayy (Sistema Dragon)")
        h3_start = html_content.rfind("<h3", 0, idx)
        if h3_start != -1:
            html_content = html_content[:h3_start] + '<div class="page-break"></div>\n' + html_content[h3_start:]

    # Standalone file for this version
    standalone = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>{label} - Arthur Santos Neto</title>
  <link rel="stylesheet" href="../templates/style.css">
  <style>
    .page-break {{ page-break-before: always; break-before: page; }}
    @media print {{
      .page-break {{ page-break-before: always; break-before: page; }}
    }}
  </style>
</head>
<body>
  <div class="toolbar no-print">
    <div class="toolbar-title">
      <span>{label} — Arthur Santos Neto</span>
    </div>
    <div class="toolbar-actions">
      <span style="font-size: 12px; color: #94a3b8;">Dica de impressão: Margens Mínimas / A4</span>
      <button class="btn-print" onclick="window.print()">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>
        Salvar em PDF / Imprimir
      </button>
    </div>
  </div>
  <div class="cv-container">
    {html_content}
  </div>
</body>
</html>"""
    
    with open(os.path.join("versoes", f"{fname}.html"), "w", encoding="utf-8") as f:
        f.write(standalone)

    # Store for preview switcher
    sections_html.append(f"""
    <!-- Versão {label} -->
    <div id="cv-{v_id}" class="cv-version-block" style="display: {'block' if v_id == 'fullstack' else 'none'};">
      <div class="cv-container">
        {html_content}
      </div>
    </div>
    """)

# Now generate templates/preview_cv.html
preview_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Arthur Santos Neto - Visualizador de Currículos</title>
  <link rel="stylesheet" href="style.css">
  <style>
    .page-break {{ page-break-before: always; break-before: page; }}
    @media print {{
      .page-break {{ page-break-before: always; break-before: page; }}
    }}
  </style>
</head>
<body>
  <header class="toolbar no-print">
    <div class="toolbar-title">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
      <span>Central de Currículos ATS (Padrão 2 Páginas A4)</span>
    </div>
    <div class="toolbar-actions">
      <label for="versionSelect" style="font-size: 13px; color: #94a3b8;">Selecionar Versão:</label>
      <select id="versionSelect" class="select-version" onchange="switchVersion(this.value)">
        <option value="fullstack">1. Desenvolvedor Fullstack Sênior</option>
        <option value="csharp">2. Desenvolvedor C# / .NET Sênior</option>
        <option value="angular">3. Desenvolvedor Angular Sênior</option>
        <option value="qa">4. QA Analyst Pleno</option>
      </select>
      <button class="btn-print" onclick="window.print()">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>
        Salvar em PDF (Ctrl+P)
      </button>
    </div>
  </header>

  <div class="no-print" style="max-width: 210mm; margin: 12px auto -10px auto; background: #e0f2fe; border-left: 4px solid #0284c7; padding: 10px 14px; border-radius: 4px; font-size: 12px; color: #0369a1;">
    💡 <strong>Dica de exportação para PDF perfeito:</strong> No menu de impressão do Chrome/Edge (Ctrl+P), selecione <em>Destino: Salvar como PDF</em>, <em>Tamanho do papel: A4</em>, <em>Margens: Mínimas ou Personalizadas</em> e marque <em>Gráficos de segundo plano</em>.
  </div>

  {''.join(sections_html)}

  <script>
    const titles = {{
      'fullstack': 'Arthur_Santos_Neto_Desenvolvedor_Fullstack_Senior',
      'csharp': 'Arthur_Santos_Neto_Desenvolvedor_CSharp_Senior',
      'angular': 'Arthur_Santos_Neto_Desenvolvedor_Angular_Senior',
      'qa': 'Arthur_Santos_Neto_QA_Analyst_Pleno'
    }};

    function switchVersion(key) {{
      const keys = ['fullstack', 'csharp', 'angular', 'qa'];
      keys.forEach(k => {{
        const el = document.getElementById('cv-' + k);
        if (el) {{
          el.style.display = (k === key) ? 'block' : 'none';
        }}
      }});
      document.title = (titles[key] || 'Arthur_Santos_Neto_CV') + '.pdf';
    }}
  </script>
</body>
</html>"""

with open(os.path.join("templates", "preview_cv.html"), "w", encoding="utf-8") as f:
    f.write(preview_html)

print("Generated templates/preview_cv.html and standalone HTMLs successfully.")
