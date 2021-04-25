import csv
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def prepare_data():
    dataloader = []

    with open('result.csv') as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            if row:
                orig1 = float(row[0][1:-1].split(',')[0])
                orig2 = float(row[0][1:-1].split(',')[1][1:])
                distance = []
                for item in row:
                    distance.append(float(item[1:-1].split(',')[2][1:]))
                dataloader.append([orig1,orig2,min(distance)])
    df = pd.DataFrame(dataloader)
    return df

def data_grid(data):
    print(data)
    grid = pd.crosstab(data[1], data[0], data[2], aggfunc=np.sum)
    print(grid)
    return grid

if __name__ == "__main__":
    df = prepare_data()
    grid = data_grid(df)

    fig = plt.figure()
    p1 = sns.heatmap(grid)
    plt.show()