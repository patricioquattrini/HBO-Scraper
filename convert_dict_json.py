import json
def convert_dict_json(input_list, output_list, type):
    if type == "serie":
        for m in input_list:
            n = m.__dict__
            output_list[type].append(n)
    with open('Result.json', 'w') as file:
        json.dump(output_list, file)