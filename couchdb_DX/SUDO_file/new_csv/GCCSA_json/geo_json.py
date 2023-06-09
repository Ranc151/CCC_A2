import json

# 读取 JSON 文件
with open('Labour_2020.json', "r") as f:
    json_data = json.load(f)

# Create the GeoJSON data structure
geojson_data = {
    "type": "FeatureCollection",
    "features": [json_data]
}

# Save the GeoJSON data to a file
with open("../../geo_json/output.geojson", "w") as f:
    json.dump(geojson_data, f)
