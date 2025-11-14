#!/usr/bin/env python3
"""
LaTeX document generator for PSE teaching materials.
Creates well-formatted PDFs for cheat sheets and problem sets.
"""

import subprocess
from pathlib import Path
from typing import Optional


class LaTeXGenerator:
    """Generates LaTeX documents and compiles them to PDF."""
    
    def __init__(self, output_dir: str = "."):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def create_cheat_sheet_template(self) -> str:
        """Return LaTeX template for cheat sheets."""
        return r"""\documentclass[10pt,landscape,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[margin=0.5in]{geometry}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{multicol}
\usepackage{enumitem}
\usepackage{xcolor}
\usepackage{tcolorbox}
\usepackage{fancyhdr}
\usepackage{hyperref}

\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0.4pt}

\setlength{\parindent}{0pt}
\setlength{\parskip}{0.5em}
\setlist{nosep}

\tcbuselibrary{skins,breakable}
\newtcolorbox{conceptbox}[1]{
  colback=blue!5!white,
  colframe=blue!75!black,
  fonttitle=\bfseries,
  title=#1,
  breakable
}

\newtcolorbox{formulabox}{
  colback=green!5!white,
  colframe=green!65!black,
  breakable
}

\newtcolorbox{notebox}{
  colback=yellow!5!white,
  colframe=orange!75!black,
  breakable
}

\begin{document}

%% CONTENT GOES HERE %%

\end{document}
"""
    
    def create_problem_set_template(self) -> str:
        """Return LaTeX template for problem sets."""
        return r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{enumitem}
\usepackage{xcolor}
\usepackage{tcolorbox}
\usepackage{fancyhdr}
\usepackage{hyperref}
\usepackage{graphicx}

\pagestyle{fancy}
\fancyhf{}
\lhead{PSE Problem Set}
\rhead{\thepage}
\renewcommand{\headrulewidth}{0.4pt}

\setlength{\parindent}{0pt}
\setlength{\parskip}{1em}

\tcbuselibrary{skins,breakable}
\newtcolorbox{problembox}[1]{
  colback=blue!5!white,
  colframe=blue!75!black,
  fonttitle=\bfseries,
  title=Problem #1,
  breakable
}

\newtcolorbox{solutionbox}{
  colback=green!5!white,
  colframe=green!65!black,
  fonttitle=\bfseries,
  title=Solution,
  breakable
}

\newtcolorbox{hintbox}{
  colback=yellow!5!white,
  colframe=orange!75!black,
  fonttitle=\bfseries,
  title=Hint,
  breakable
}

\begin{document}

%% CONTENT GOES HERE %%

\end{document}
"""
    
    def compile_latex(self, tex_file: Path, cleanup: bool = True) -> Optional[Path]:
        """Compile LaTeX file to PDF."""
        try:
            # Run pdflatex twice for proper references
            for _ in range(2):
                result = subprocess.run(
                    ["pdflatex", "-interaction=nonstopmode", str(tex_file)],
                    cwd=tex_file.parent,
                    capture_output=True,
                    text=True
                )
                if result.returncode != 0:
                    print(f"LaTeX compilation error:\n{result.stdout}\n{result.stderr}")
                    return None
            
            # Cleanup auxiliary files if requested
            if cleanup:
                for ext in ['.aux', '.log', '.out']:
                    aux_file = tex_file.with_suffix(ext)
                    if aux_file.exists():
                        aux_file.unlink()
            
            pdf_file = tex_file.with_suffix('.pdf')
            return pdf_file if pdf_file.exists() else None
            
        except Exception as e:
            print(f"Error compiling LaTeX: {e}")
            return None
    
    def generate_cheat_sheet(self, content: str, filename: str) -> Optional[Path]:
        """Generate a cheat sheet PDF."""
        template = self.create_cheat_sheet_template()
        latex_content = template.replace("%% CONTENT GOES HERE %%", content)
        
        tex_file = self.output_dir / f"{filename}.tex"
        tex_file.write_text(latex_content)
        
        return self.compile_latex(tex_file)
    
    def generate_problem_set(self, content: str, filename: str) -> Optional[Path]:
        """Generate a problem set PDF."""
        template = self.create_problem_set_template()
        latex_content = template.replace("%% CONTENT GOES HERE %%", content)
        
        tex_file = self.output_dir / f"{filename}.tex"
        tex_file.write_text(latex_content)
        
        return self.compile_latex(tex_file)


def create_cheat_sheet(content: str, filename: str, output_dir: str = ".") -> str:
    """Create a cheat sheet PDF."""
    generator = LaTeXGenerator(output_dir)
    pdf_path = generator.generate_cheat_sheet(content, filename)
    if pdf_path:
        return f"Cheat sheet created: {pdf_path}"
    else:
        return "Failed to create cheat sheet"


def create_problem_set(content: str, filename: str, output_dir: str = ".") -> str:
    """Create a problem set PDF."""
    generator = LaTeXGenerator(output_dir)
    pdf_path = generator.generate_problem_set(content, filename)
    if pdf_path:
        return f"Problem set created: {pdf_path}"
    else:
        return "Failed to create problem set"


if __name__ == "__main__":
    # Example usage
    sample_content = r"""
\begin{multicols}{2}

\begin{conceptbox}{Derivatives}
Basic differentiation rules:
\begin{align*}
\frac{d}{dx}[x^n] &= nx^{n-1} \\
\frac{d}{dx}[e^x] &= e^x \\
\frac{d}{dx}[\ln x] &= \frac{1}{x}
\end{align*}
\end{conceptbox}

\begin{formulabox}
Chain rule: $(f \circ g)'(x) = f'(g(x)) \cdot g'(x)$
\end{formulabox}

\end{multicols}
"""
    generator = LaTeXGenerator()
    result = generator.generate_cheat_sheet(sample_content, "test_cheat_sheet")
    print(f"Generated: {result}")
