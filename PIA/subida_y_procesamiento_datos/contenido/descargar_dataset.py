import os
import zipfile

# Dataset de Kaggle
dataset = "adrianjuliusaluoch/hourly-crypto-stocks-market-data"

# Carpeta destino (donde está este script)
target_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta del ZIP
zip_path = os.path.join(target_dir, "hourly-crypto-stocks-market-data.zip")

# Descargar el ZIP directamente en contenido/
print(f"📥 Descargando dataset: {dataset}")
os.system(f"kaggle datasets download -d {dataset} -p {target_dir}")

# Verificar que se descargó correctamente
if not os.path.exists(zip_path):
    raise FileNotFoundError("❌ No se encontró archive.zip en la carpeta destino.")

# Descomprimir el ZIP en contenido/
print(f"📂 Descomprimiendo: {zip_path}")
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(target_dir)
    print(f"✅ Archivos extraídos: {zip_ref.namelist()}")

# Eliminar el ZIP
os.remove(zip_path)
print("🧹 archive.zip eliminado")

print("🎉 Descarga y extracción completadas. Archivos disponibles en:", target_dir)
