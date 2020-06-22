import json

# python object(dictionary) to be dumped
dict1 = {
    "emp1": {
        "name": "Vinitha",
        "designation": "Trainee",
        "age": "22",
        "salary": "100"
    },
    "emp2": {
        "name": "Sakthi",
        "designation": "Trainer",
        "age": "24",
        "salary": "200"
    },
}

# the json file where the output must be stored
out_file = open("myfile.json", "w")

json.dump(dict1, out_file, indent = 6)

out_file.close()