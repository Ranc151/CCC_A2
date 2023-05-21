import json

file_address = "C:\\Users\\13593\PycharmProjects\\CCC_A2\\couchdb_DX\\SUDO_file\\new_csv\\GCCSA_json\\Labour_2021.json"
gcc = []
with open(file_address, 'r', encoding='utf-8') as file:
    newline = file.readline()
    newline = file.readline()
    cityStr = ""
    while True:
        newline = file.readline()
        if newline != "        }\n" and newline != "        },\n":
            cityStr += newline
        if newline == "        },\n":
            cityStr += newline.split(",")[0]
            dic = json.loads(cityStr)
            city = dic.get("gccsa_code_2016")
            if city not in gcc:
                gcc.append(city)

            cityStr = ""
        if newline == "        }\n":
            cityStr += newline[:-1]
            dic = json.loads(cityStr)
            city = dic.get("gccsa_code_2016")
            if city not in gcc:
                gcc.append(city)
            print(gcc)

            exit()
