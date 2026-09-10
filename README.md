# Repositório de Currículos & Otimização ATS — Arthur Santos Neto

Repositório centralizado para gestão, versionamento e exportação de currículos profissionais de **Arthur Santos Neto**, calibrados para atender aos critérios de ranqueamento dos principais sistemas ATS (*Applicant Tracking Systems*) e aos padrões de avaliação de Tech Recruiters e lideranças de engenharia.

**Repositório Oficial:** [https://github.com/ArthurSNeto/cv.git](https://github.com/ArthurSNeto/cv.git)

---

## 📁 Estrutura do Repositório

```text
curriculum/
├── .gitignore                          # Regras de exclusão do Git
├── README.md                           # Documentação central do projeto
├── analise_ats_e_diagnostico.md        # Diagnóstico detalhado, guia ATS e estratégias
├── build_html.py                       # Script utilitário para compilar Markdown em HTML
├── generate_preview.py                 # Gerador da central de visualização e PDFs
├── original/                           # Arquivos originais mantidos como referência
│   ├── Arthur_CV.pdf                   # Versão original em Português (3 páginas)
│   └── Arthur_CV_EN.pdf                # Versão original em Inglês
├── versoes/                            # As 4 versões segmentadas (Markdown + HTML)
│   ├── 01_desenvolvedor_fullstack_senior.md / .html
│   ├── 02_desenvolvedor_csharp_senior.md / .html
│   ├── 03_desenvolvedor_angular_senior.md / .html
│   └── 04_qa_analyst_pleno.md / .html
└── templates/                          # Templates de renderização e impressão
    ├── preview_cv.html                 # Central interativa com seletor de versões
    └── style.css                       # Folha de estilos otimizada para 2 páginas A4
```

---

## 🎯 As 4 Versões Especializadas

Cada versão foi formulada a partir da mesma base real de experiência, ajustando a ênfase técnica, as palavras-chave prioritárias e a narrativa de impacto:

1. **Desenvolvedor Fullstack Sênior** (`versoes/01_desenvolvedor_fullstack_senior.md`):
   - **Foco:** Equilíbrio arquitetural completo entre backend (.NET 6/7/8) e frontend (Angular/React), nuvem (Azure DevOps/AWS) e liderança técnica.
   - **Público:** Vagas de Desenvolvedor Fullstack Sênior, Tech Lead e Engenheiro de Software Sênior.

2. **Desenvolvedor C# / .NET Sênior** (`versoes/02_desenvolvedor_csharp_senior.md`):
   - **Foco:** Profundidade no ecossistema C# / .NET (ASP.NET Core, EF Core, SQL Server avançado, Clean Architecture, DDD, multi-tenancy, concorrência, Hangfire e alta performance).
   - **Público:** Vagas de Backend Sênior, Especialista .NET e Arquiteto de Software Backend.

3. **Desenvolvedor Angular Sênior** (`versoes/03_desenvolvedor_angular_senior.md`):
   - **Foco:** Frontend moderno (Angular 13+, TypeScript, RxJS, componentização, Kendo UI, gestão reativa de estado, SPA modular e testes de interface).
   - **Público:** Vagas de Frontend Sênior e Especialista Angular.

4. **QA Analyst Pleno / SDET** (`versoes/04_qa_analyst_pleno.md`):
   - **Foco:** Garantia de qualidade com background técnico de desenvolvimento (*Shift-Left Testing*). Automação com Selenium, xUnit, NUnit, Moq, validação de APIs com Postman e *Quality Gates* em CI/CD.
   - **Público:** Vagas de QA Analyst Pleno, Engenheiro de Qualidade e SDET Pleno.

---

## 📊 Principais Melhorias Implementadas (Resumo do Diagnóstico)

- **Redução de 3 para 2 páginas:** Eliminação de páginas quebradas e espaços em branco, gerando documentos densos de alto impacto visual e leitura de 6-10 segundos.
- **Resolução do Hiato Temporal (1 ano e 6 meses):** Reposicionamento do período de estudos como **Engenharia de Software Independente / Consultoria Full Stack & IA**, evidenciando produtos reais (extensões de navegador, landing pages, backends C#) e a adoção pioneira de ferramentas de IA Generativa (GitHub Copilot, Google Antigravity).
- **Padronização de Dados:**
  - LinkedIn: `https://linkedin.com/in/arthursneto`
  - GitHub: `https://github.com/ArthurSNeto`
  - Certificação EF SET: Padronizada no nível real **64/100 (C1 Proficient)**.
- **Eliminação de Anti-Padrões de Senioridade:** Substituição de expressões como *"primeira experiência com deploy Linux"* por narrativas de competência e impacto arquitetural.
- **Destaque de Métricas Reais:**
  - Impacto em escala educacional: **2.800+ unidades municipais e 438 mil estudantes**.
  - Otimização de CI/CD: Redução de build de **15 min para 5 min** (66% mais rápido).
  - Performance SQL Server: Redução de **40% no tempo de resposta**.
  - Resolução de gargalos críticos: Redução de latência de **>60s para 20-30s** no Cosmos DB.
  - Liderança técnica e mentoria de **6 a 8 desenvolvedores**.

Para ler o diagnóstico completo e as dicas de entrevista, consulte [analise_ats_e_diagnostico.md](analise_ats_e_diagnostico.md).

---

## 🖨️ Como Visualizar e Gerar os PDFs (2 Páginas Perfeitas)

1. **Via Central Interativa (Recomendado):**
   - Abra o arquivo `templates/preview_cv.html` em seu navegador favorito (Google Chrome ou Microsoft Edge).
   - Utilize o seletor no topo da página para escolher a versão desejada.
   - Clique no botão **"Salvar em PDF (Ctrl+P)"**.
   - No diálogo de impressão:
     - **Destino:** Salvar como PDF
     - **Páginas:** Todas (serão exatamente 2 páginas)
     - **Tamanho do papel:** A4
     - **Margens:** Mínimas ou Personalizadas (se necessário, ajuste a escala para 95% ou 100%)
     - **Opções:** Marcar *"Gráficos de segundo plano"*

2. **Via Arquivos Standalone:**
   - Cada versão possui seu próprio arquivo HTML em `versoes/*.html` pronto para impressão direta.

3. **Recompilar os HTMLs após edições nos Markdown:**
   Caso faça alterações nos arquivos `.md`, basta executar no terminal:
   ```bash
   python generate_preview.py
   ```
