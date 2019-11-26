from csv import DictReader
from modules.app import app


@app.route('/dummy_csv', methods=['GET'])
def dummy_csv():

    data_list = []

    with open("data/hdb-carpark-information.csv") as file:
        csv_reader = DictReader(file)

        for row in csv_reader:
            data_list.append(row)

    return str(data_list)
