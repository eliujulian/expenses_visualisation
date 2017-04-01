import csv
import json


def missing_as_double_quotes():
    jsonfile = open('data.json', 'w')

    with open('data.csv') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    for r in rows:
        for k, v in r.items():
            if k == "Level":
                r[k] = str(v)
            elif v.isdigit():
                r[k] = int(v)
            elif k == "":
                r[k] = ""
            elif len(v) > 3:
                pass
            elif len(v) == 0:
                pass
            elif v in ["TVs"]:
                pass
            else:
                r[k] = float(v)

    for r in rows:
        json.dump(r, jsonfile)
        jsonfile.write(',\n')


def missing_as_zeros():
    jsonfile = open('data_w_zeros.json', 'w')

    with open('data.csv') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    for r in rows:
        for k, v in r.items():
            if k == "Level":
                r[k] = str(v)
            elif v.isdigit():
                r[k] = int(v)
            elif k == "":
                r[k] = 0
            elif len(v) > 3:
                pass
            elif len(v) == 0:
                r[k] = 0
            elif v in ["TVs"]:
                pass
            else:
                r[k] = float(v)

    for r in rows:
        json.dump(r, jsonfile)
        jsonfile.write(',\n')


def per_person_missing_as_double_quotes():
    jsonfile = open('data_pp.json', 'w')

    with open('data.csv') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    for r in rows:
        for k, v in r.items():
            if k == "Level":
                r[k] = str(v)
            elif v.isdigit():
                r[k] = int(v)
            elif k == "":
                r[k] = ""
            elif len(v) > 3:
                pass
            elif len(v) == 0:
                pass
            elif v in ["TVs"]:
                pass
            else:
                r[k] = float(v)

    for r in rows[1:]:
        for k, v in r.items():
            if k == "Group":
                pass
            elif isinstance(v, int):
                print(k, v, rows[0][k])
                r[k] = int(v / rows[0][k])

    for r in rows:
        json.dump(r, jsonfile)
        jsonfile.write(',\n')


def missing_as_zeros_per_person():
    jsonfile = open('data_w_zeros_pp.json', 'w')

    with open('data.csv') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    for r in rows:
        for k, v in r.items():
            if k == "Level":
                r[k] = str(v)
            elif v.isdigit():
                r[k] = int(v)
            elif k == "":
                r[k] = 0
            elif len(v) > 3:
                pass
            elif len(v) == 0:
                r[k] = 0
            elif v in ["TVs"]:
                pass
            else:
                r[k] = float(v)

    for r in rows[1:]:
        for k, v in r.items():
            if k == "Group":
                pass
            elif isinstance(v, int):
                # print(k, v, rows[0][k])
                r[k] = int(v / rows[0][k])

    for r in rows:
        json.dump(r, jsonfile)
        jsonfile.write(',\n')

missing_as_double_quotes()
missing_as_zeros()
per_person_missing_as_double_quotes()
missing_as_zeros_per_person()
