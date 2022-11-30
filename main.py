import tkinter
from tkinter import filedialog
import pandas as pd
import pathlib2 as pl2
import os


# asking for the file
def search_for_file_path():
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        print("You chose: %s" % tempdir)
    return tempdir


if __name__ == '__main__':
    # creating window
    root = tkinter.Tk()
    root.withdraw()  # use to hide tkinter window

    # pathes
    ask_path = search_for_file_path()
    #path_test = pl2.Path("/Users/riad_rustum/Desktop/test")
    path_combine = pl2.Path(ask_path)

    # combining the data
    dfs = [pd.read_csv(p, encoding='UTF-8', sep=';') for p in path_combine.glob('*.csv')]
    names = ["A", "B", "C"]

    new_data = pd.concat(dfs, keys=names)
    new_data = new_data.reset_index(level=1, drop=True).rename_axis('File').reset_index()


    # exporting the data
    new_data.to_csv(r'/Users/riad_rustum/Desktop/end_ergebnisse.csv',
                    encoding='UTF-8',
                    sep=";",
                    decimal=',',
                    index=False)
