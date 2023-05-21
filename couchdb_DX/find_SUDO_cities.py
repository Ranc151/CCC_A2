import json

file_address = "C:\\Users\\13593\\PycharmProjects\\CCC_A2\\couchdb_DX\\SUDO_file\\new_csv\\SA4_json\\Labour_2021.json"
cityList = []
stateList = []
locationDict = {}
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
            city = dic.get("sa4_name_2016")
            state = dic.get("state_name_abbr")
            if city not in cityList:
                cityList.append(city)
            if state not in stateList:
                stateList.append(state)
            if state not in locationDict.keys():
                locationDict[state] = [city]
            if state in locationDict.keys():
                if city not in locationDict[state]:
                    locationDict[state].append(city)

            cityStr = ""
        if newline == "        }\n":
            cityStr += newline[:-1]
            dic = json.loads(cityStr)
            city = dic.get("sa4_name_2016")
            state = dic.get("state_name_abbr")
            if city not in cityList:
                cityList.append(city)
            if state not in stateList:
                stateList.append(state)
            if state not in locationDict.keys():
                locationDict[state] = [city]
            if state in locationDict.keys():
                if city not in locationDict[state]:
                    locationDict[state].append(city)
            print(cityList)
            print(stateList)
            print(locationDict)
            exit()
