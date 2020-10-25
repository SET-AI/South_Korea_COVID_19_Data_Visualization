from pandas import read_csv
import numpy as np
import pandas as pd

from datetime import datetime
from datetime import timedelta
import math
import winsound
import glob, os

ko_dict = {
    '서울': 'Seoul',
    '경기': 'Gyeonggi-do',
    '인천': 'Incheon',
    '대전': 'Daejeon',
    '대구': 'Daegu',
    '광주': 'Gwangju',
    '강원': 'Gangwon-do',
    '울산': 'Ulsan',
    '세종': 'Sejong',
    '충북': 'Chungcheongbuk-do',
    '충남': 'Chungcheongnam-do',
    '전북': 'Jeollabuk-do',
    '전남': 'Jeollanam-do',
    '경북': 'Gyeongsangbuk-do',
    '경남': 'Gyeongsangnam-do',
    '부산': 'Busan',
    '제주': 'Jeju-do',
}

class TCSDataConverter():
    def __init__(self):
        self.time = datetime.now().strftime("%m_%d_%Y-%H_%M_%S")

    def date_convertor(self, date):
        # 20190105 -> 2019-01-05
        date = str(date)
        new_date = ''
        i = 0
        for d in date:
            if i == 4 or i == 6:
                new_date += '-'
            new_date += d
            i += 1

        return new_date


    def run(self):
        path = "../../data/korea/covid/TCS"
        os.chdir(path)

        df_list = []
        for file in glob.glob("*.xlsx"):
            print(file)

            # 1. Loads data from xlsx
            self.excel_data = pd.read_excel(file, 'Sheet')

            # Changes value names
            self.excel_data = self.excel_data.replace(ko_dict)

            # Combines two columns
            cols = ['출발시도', '도착시도']
            self.excel_data['route'] = self.excel_data[cols].apply(lambda row: '>'.join(row.values.astype(str)), axis=1)

            # Drops unnecessary columns
            self.excel_data = self.excel_data.drop(columns=cols)

            # Pivots this table
            pivoted = self.excel_data.pivot(index='집계일', columns='route', values='차량댓수')

            # Takes a experiment list
            # experiments = self.excel_data['Experiment'].unique()

            # For each experiment
            # for ex in experiments:
            #     # Takes an experiment data
            #     self.df_cur_ex = self.excel_data[(self.excel_data['Experiment'] == ex)]
            df_list.append(pivoted)

        # Stacks all results
        df_vertical_stack = pd.concat(df_list, axis=0)

        # convert index to column pandas dataframe
        df_vertical_stack.reset_index(inplace=True)
        df_vertical_stack = df_vertical_stack.rename(columns={'집계일': 'date'})

        # 20190105 -> 2019-01-05
        df_vertical_stack['date'] = df_vertical_stack['date'].apply(lambda row: self.date_convertor(row))

        # Saves all results as one file
        df_vertical_stack.to_csv(f"output/total_{self.time}.csv")


TCSDataConverter().run()

winsound.Beep(1000, 440)
