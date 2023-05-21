import json

# 读取 JSON 文件
with open('Labour_2021.json', "r") as f:
    json_data2 = json.load(f)

# Create the GeoJSON data structure
geojson2_data = {
    "type": "FeatureCollection",
    "features": [json_data2]
}

# Save the GeoJSON data to a file
with open("../../geo_json/output2.geojson", "w") as f:
    json.dump(geojson2_data, f)
