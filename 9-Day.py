travel_log = {"India" : ["BBI", "MUM", "DEL", "CCU", "BLR"],
              "US" : ["NY", "DC", "LA", "SA"]
              }

for key in travel_log:
    if(key == "India"):
        print(travel_log[key][2])
        for item in travel_log[key]:
            print(item)

nested_list = ["A","N", ["I","L"]]
for item in nested_list:
    print(item)
print(nested_list[2][1])
print(nested_list[2][0])