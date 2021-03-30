import pandas as pd




def create_db():
    df = pd.read_csv('Data/data.csv')

    print(df.head())
    print('hello world')


if __name__ == '__main__':
    create_db()