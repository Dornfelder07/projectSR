import pandas as pd
import numpy as np
import datetime


class PartnerDataReader:
    def __init__(self, partner_id, today):
        self.partner_id = partner_id
        self.today = today

    def next_day(self):
        df = pd.read_csv('C:/Users/Alicja/Downloads/sorted-20201123T092929Z-003/sorted/sorted_'+self.partner_id+'_dataset.csv')

        date_time = self.today.strftime("%d/%m/%Y")

        new_df = df.loc[(df['click_timestamp'].astype(str).str.contains(date_time))]
        return new_df
