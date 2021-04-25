import os
import pandas as pd


class Reader:
    @staticmethod
    def current_path():
        print("Current working directory:"+os.getcwd())

    @staticmethod
    def get_from_data(filename):
        os.chdir('../')
        dir_file = os.getcwd()+'/Data/'+filename
        df = pd.read_csv(dir_file)
        return df
