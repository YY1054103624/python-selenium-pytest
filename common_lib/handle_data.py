import csv


def handle_csv_data(path):
    file = open(path, "r", encoding="utf-8")
    return list(map(tuple, csv.reader(file)))[1:]
