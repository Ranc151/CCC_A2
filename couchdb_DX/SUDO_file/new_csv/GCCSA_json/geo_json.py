import json

json_file = 'Labour_2021.json'  # 输入的CSV文件路径

# 读取 JSON 文件
with open('Labour_2021.json', "r") as f:
    json_data = json.load(f)


# Create the GeoJSON data structure
geojson_data = {
  "type": "FeatureCollection",
  "features": [json_data]
}

# Save the GeoJSON data to a file
with open("output.geojson", "w") as f:
    json.dump(geojson_data, f)
