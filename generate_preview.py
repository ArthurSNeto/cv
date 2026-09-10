import os
import markdown
import subprocess

# Read CSS content to inline directly into all HTML files (Zero cache issues!)
css_path = os.path.join("templates", "style.css")
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

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
    target_heading = "<h3>Desenvolvedor Fullstack Pleno — PrintWayy (Sistema Dragon)</h3>"
    if target_heading in html_content:
        html_content = html_content.replace(target_heading, f'<div class="page-break"></div>\n{target_heading}')
    elif "PrintWayy (Sistema Dragon)" in html_content:
        idx = html_content.find("PrintWayy (Sistema Dragon)")
        h3_start = html_content.rfind("<h3", 0, idx)
        if h3_start != -1:
            html_content = html_content[:h3_start] + '<div class="page-break"></div>\n' + html_content[h3_start:]

    # Standalone file with INLINED CSS (guarantees 100% cache-free rendering)
    standalone = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>{label} - Arthur Santos Neto</title>
  <style>
{css_content}
  </style>
</head>
<body>
  <div class="toolbar no-print">
    <div class="toolbar-title">
      <span>{label} — Arthur Santos Neto</span>
    </div>
    <div class="toolbar-actions">
      <button class="btn-print" onclick="window.print()">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>
        Salvar em PDF / Imprimir
      </button>
    </div>
  </div>

  <div class="no-print instruction-card">
    <strong style="font-size: 13.5px; display: block; margin-bottom: 4px; color: #92400e;">⚠️ Como remover o cabeçalho e rodapé (Data, URL, Título e Página 1/2):</strong>
    <ol style="margin-left: 20px; line-height: 1.5; font-size: 12.5px; color: #78350f;">
      <li>Na janela de impressão (Ctrl+P), clique em <strong>"Mais definições"</strong> (<em>More settings</em>).</li>
      <li><strong>DESMARQUE</strong> a opção <strong>"Cabeçalhos e rodapés"</strong> (<em>Headers and footers</em>).</li>
      <li><strong>MARQUE</strong> a opção <strong>"Gráficos de segundo plano"</strong> (<em>Background graphics</em>).</li>
      <li>Em <strong>Margens</strong>, escolha <strong>"Mínimas"</strong> ou <strong>"Personalizadas"</strong>.</li>
    </ol>
  </div>

  <div class="cv-container">
    {html_content}
  </div>
</body>
</html>"""
    
    html_out = os.path.join("versoes", f"{fname}.html")
    with open(html_out, "w", encoding="utf-8") as f:
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

# Generate preview_cv.html with INLINED CSS
preview_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Arthur Santos Neto - Visualizador de Currículos</title>
  <style>
{css_content}
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

  <div class="no-print instruction-card">
    <strong style="font-size: 13.5px; display: block; margin-bottom: 4px; color: #92400e;">💡 Dicas para salvar o PDF perfeito no Chrome/Edge:</strong>
    <ol style="margin-left: 20px; line-height: 1.5; font-size: 12.5px; color: #78350f;">
      <li>Clique em <strong>Salvar em PDF</strong> (ou pressione <strong>Ctrl+P</strong>).</li>
      <li>Expanda <strong>"Mais definições"</strong> (<em>More settings</em>).</li>
      <li><strong>DESMARQUE "Cabeçalhos e rodapés"</strong> (remove data, URL e número de página).</li>
      <li><strong>MARQUE "Gráficos de segundo plano"</strong> (mantém linhas e destaques).</li>
      <li>Em <strong>Margens</strong>, selecione <strong>"Mínimas"</strong> ou <strong>"Personalizadas"</strong>.</li>
    </ol>
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

print("HTML files regenerated with inlined CSS.")

# Automatically export all 4 PDFs directly using headless Chrome
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if os.path.exists(chrome_path):
    print("\nExporting all 4 PDFs directly via Chrome headless...")
    pdf_dir = os.path.join("versoes", "pdf")
    os.makedirs(pdf_dir, exist_ok=True)
    for v_id, fname, label, pdf_name in versions_info:
        html_file = os.path.abspath(os.path.join("versoes", f"{fname}.html"))
        pdf_file = os.path.abspath(os.path.join(pdf_dir, pdf_name))
        cmd = f'cmd.exe /c ""{chrome_path}" --headless=new --no-pdf-header-footer --print-to-pdf="{pdf_file}" "{html_file}""'
        subprocess.run(cmd, shell=True)
        if os.path.exists(pdf_file):
            print(f" -> Generated: {pdf_file} ({os.path.getsize(pdf_file)} bytes)")
print("Done!")
