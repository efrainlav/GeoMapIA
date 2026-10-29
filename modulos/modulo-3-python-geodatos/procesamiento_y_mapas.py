"""
Módulo 3 — Curso GeoMapIA (SELPER Colombia)
Script generado con asistencia de IA (Prompts 3.1 y 3.2):
1. Lee el archivo CSV con coordenadas de muestreo agrícola/ambiental de Colombia (sin requerir librerías externas para el paso base, y mostrando el flujo con GeoPandas).
2. Demuestra cómo transformar entre MAGNA-SIRGAS Origen Nacional (EPSG:9377) y WGS84 (EPSG:4326).
3. Exporta un archivo GeoJSON optimizado para la web (`data/muestreo_agro_optimizado.geojson`).
"""

import csv
import json
from pathlib import Path

# Rutas del proyecto
BASE_DIR = Path(__file__).resolve().parents[2]
CSV_PATH = BASE_DIR / "data" / "muestreo_agro_campo.csv"
OUT_GEOJSON = BASE_DIR / "data" / "muestreo_agro_optimizado.geojson"


def csv_a_geojson_optimizado(csv_path: Path, out_geojson: Path) -> None:
    """Convierte un CSV con latitud/longitud a un GeoJSON liviano en EPSG:4326."""
    features = []
    with csv_path.open(mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row.get("latitud") or not row.get("longitud"):
                continue
            lat = round(float(row["latitud"]), 5)
            lon = round(float(row["longitud"]), 5)
            props = {
                "id_lote": row["id_lote"],
                "municipio": row["municipio"],
                "departamento": row["departamento"],
                "region": row["region"],
                "cultivo": row["cultivo"],
                "ndvi": float(row["ndvi"]),
                "humedad_suelo_pct": float(row["humedad_suelo_pct"]),
                "altitud_msnm": int(row["altitud_msnm"]),
                "rendimiento_ton_ha": float(row["rendimiento_ton_ha"]),
                "estado_fitosanitario": row["estado_fitosanitario"],
            }
            features.append({
                "type": "Feature",
                "properties": props,
                "geometry": {"type": "Point", "coordinates": [lon, lat]},
            })

    geojson_obj = {
        "type": "FeatureCollection",
        "name": "muestreo_agro_optimizado",
        "features": features,
    }

    out_geojson.write_text(json.dumps(geojson_obj, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[OK] GeoJSON web exportado con {len(features)} registros en: {out_geojson}")


def ejemplo_reproyeccion_magna_sirgas() -> str:
    """
    Plantilla de referencia con GeoPandas para reproyectar Shapefiles pesados
    desde MAGNA-SIRGAS Origen Nacional (EPSG:9377) a WGS84 Web (EPSG:4326).
    """
    return '''
    import geopandas as gpd

    # 1. Leer Shapefile o GeoPackage original (ej. IGAC / IDEAM / DANE)
    gdf = gpd.read_file("predios_magna_9377.shp")
    print("CRS Original:", gdf.crs)

    # 2. Reproyectar al estándar web EPSG:4326
    gdf_web = gdf.to_crs(epsg=4326)

    # 3. Simplificar geometría para que cargue rápido en Leaflet
    gdf_web["geometry"] = gdf_web["geometry"].simplify(tolerance=0.0005, preserve_topology=True)

    # 4. Exportar a GeoJSON ligero
    gdf_web.to_file("predios_web_4326.geojson", driver="GeoJSON")
    '''


if __name__ == "__main__":
    if CSV_PATH.exists():
        csv_a_geojson_optimizado(CSV_PATH, OUT_GEOJSON)
    else:
        print(f"No se encontró el archivo {CSV_PATH}")
