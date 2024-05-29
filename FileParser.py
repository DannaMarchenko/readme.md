import os

import numpy as np
import pandas as pd


class FileParser:
    def __init__(self):
        self.fileNamePrefix = 'new'
        self.files = [f for f in os.listdir('.') if os.path.isfile(f) and f.__contains__(".xlsx")]
        self.files.sort()

    def parse(self):
        indexCounter = 0
        for file in self.files:
            try:
                dataFrame = pd.read_excel(file)  # прочитать DF
                if indexCounter == 0:
                    indexCounter += (dataFrame.values.__len__())
                    dataFrame.to_excel("{}_{}".format('new', file))
                else:
                    dataFrame.index = np.arange(indexCounter, len(dataFrame)+indexCounter)
                    indexCounter += (dataFrame.values.__len__())
                    dataFrame.to_excel("{}_{}".format('new', file))
                # df = dataFrame.replace(to_replace=self.regex, value=self.replaceTo, regex=True)
                # df.astype("string").to_excel("{}_{}".format('new', file))
                print("Файл {} был успешно сохранен".format("{}_{}".format('new', file)))
            except Exception as e:
                print(e)
