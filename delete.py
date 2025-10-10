import os

# Ruta base de tu proyecto (ajústala si lo ejecutas desde otro sitio)
base_path = os.path.abspath(".")

for root, dirs, files in os.walk(base_path):
    for file in files:
        if file.lower().endswith(".svg"):
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
            except Exception as e:
                print(f"⚠️  No se pudo eliminar {file_path}: {e}")

