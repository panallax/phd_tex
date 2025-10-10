import os
import re
import subprocess

# Ruta raíz del proyecto (puedes cambiarla si lo ejecutas desde otro sitio)
ROOT = os.getcwd()

# Recorre todas las carpetas en busca de SVGs
for root, dirs, files in os.walk(ROOT):
    for file in files:
        if file.lower().endswith(".svg"):
            svg_path = os.path.join(root, file)
            pdf_path = svg_path[:-4] + ".pdf"

            print(f"Convirtiendo: {svg_path} → {pdf_path}")
            try:
                subprocess.run(
                    [r"C:\Program Files\Inkscape\bin\inkscape.com", svg_path, "--export-type=pdf", "--export-filename", pdf_path],
                    check=True,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
            except Exception as e:
                print(f"⚠️ Error al convertir {svg_path}: {e}")

print("\n✅ Conversión de SVG a PDF completada.\n")

# Recorre todos los .tex y reemplaza \includesvg por \includegraphics
for root, dirs, files in os.walk(ROOT):
    for file in files:
        if file.lower().endswith(".tex"):
            tex_path = os.path.join(root, file)
            with open(tex_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Reemplaza los comandos \includesvg[opciones]{nombre}
            new_content = re.sub(
                r"\\includesvg(\[[^\]]*\])?\{([^}]+)\}",
                lambda m: f"\\\\includegraphics{m.group(1) or ''}{{{m.group(2)}.pdf}}",
                content
            )

            if new_content != content:
                with open(tex_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Actualizado: {tex_path}")

print("\n🎉 Todo listo: SVGs convertidos y comandos reemplazados.")
