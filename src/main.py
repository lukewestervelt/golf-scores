import pandas as pd


def process_data(filename):
    # https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
    csv_input = pd.read_csv(filename, header='infer', encoding='utf8', delimiter=',')
    print(csv_input)


if __name__ == '__main__':
    process_data("data/sample-scores.csv")
