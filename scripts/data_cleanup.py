from typing import TypedDict, List
import os
import glob
from pathlib import Path

import pandas as pd


def load_spreadsheet_data(sheet_name: str, period: str, start_row: int, end_row: int, header_row: int) -> pd.DataFrame:
    start_col: str = "B"
    if period.upper() == "MONTH":
        end_col: str = "ABW"
    elif period.upper() == "SEASON":
        end_col: str = "IR"
    else:
        raise ValueError(f"Unrecognized period: {period}. Valid options are MONTH, SEASON.")

    header_df: pd.DataFrame = pd.read_excel(io="../data/Original_ACI_Dataset.xlsx",
                                            sheet_name=sheet_name,
                                            usecols=f"{start_col}:{end_col}",
                                            skiprows=(header_row - 1),
                                            nrows=2,
                                            header=None)

    data_df: pd.DataFrame = pd.read_excel(io="../data/Original_ACI_Dataset.xlsx",
                                          sheet_name=sheet_name,
                                          usecols=f"{start_col}:{end_col}",
                                          skiprows=(start_row - 1),
                                          nrows=(end_row - start_row + 1),
                                          header=None)

    return pd.concat([header_df, data_df])


class TableSpec(TypedDict):
    file_name: str
    sheet_name: str
    period: str
    start_row: int
    end_row: int
    header_row: int


tables: List[TableSpec] = [
    {"file_name": "Sea_Level_Monthly_Unsmoothed", "sheet_name": "Sea Level Monthly", "period": "MONTH", "start_row": 11,
     "end_row": 25, "header_row": 7},
    {"file_name": "Sea_Level_Monthly_Smoothed", "sheet_name": "Sea Level Monthly", "period": "MONTH", "start_row": 28,
     "end_row": 42, "header_row": 7},
    {"file_name": "Sea_Level_Seasonal_Unsmoothed", "sheet_name": "Sea Level Seasonal", "period": "SEASON",
     "start_row": 28, "end_row": 42, "header_row": 7},
    {"file_name": "Sea_Level_Seasonal_Smoothed", "sheet_name": "Sea Level Seasonal", "period": "SEASON",
     "start_row": 28, "end_row": 42, "header_row": 7},
    {"file_name": "Sea_Level_Monthly_Unsmoothed_Unstandardized", "sheet_name": "Sea Level Unstandardized",
     "period": "MONTH", "start_row": 11, "end_row": 25, "header_row": 7},
    {"file_name": "Sea_Level_Seasonal_Unsmoothed_Unstandardized", "sheet_name": "Sea Level Unstandardized",
     "period": "SEASON", "start_row": 32, "end_row": 46, "header_row": 28},
    {"file_name": "CDD_Monthly_Unsmoothed", "sheet_name": "CDD Monthly", "period": "MONTH", "start_row": 11,
     "end_row": 25, "header_row": 7},
    {"file_name": "CDD_Monthly_Smoothed", "sheet_name": "CDD Monthly", "period": "MONTH", "start_row": 28,
     "end_row": 42, "header_row": 7},
    {"file_name": "CDD_Seasonal_Unsmoothed", "sheet_name": "CDD Seasonal", "period": "SEASON", "start_row": 11,
     "end_row": 25, "header_row": 7},
    {"file_name": "CDD_Seasonal_Smoothed", "sheet_name": "CDD Seasonal", "period": "SEASON", "start_row": 28,
     "end_row": 42, "header_row": 7},
    {"file_name": "CDD_Monthly_Unsmoothed_Unstandardized", "sheet_name": "CDD Unstandardized", "period": "MONTH",
     "start_row": 11, "end_row": 25, "header_row": 7},
    {"file_name": "CDD_Seasonal_Unsmoothed_Unstandardized", "sheet_name": "CDD Unstandardized", "period": "SEASON",
     "start_row": 32, "end_row": 46, "header_row": 28},
    {"file_name": "Rx5Day_Monthly_Unsmoothed", "sheet_name": "Rx5Day Monthly", "period": "MONTH", "start_row": 11,
     "end_row": 25, "header_row": 7},
    {"file_name": "Rx5Day_Monthly_Smoothed", "sheet_name": "Rx5Day Monthly", "period": "MONTH", "start_row": 28,
     "end_row": 42, "header_row": 7},
    {"file_name": "Rx5Day_Seasonal_Unsmoothed", "sheet_name": "Rx5Day Seasonal", "period": "SEASON", "start_row": 11,
     "end_row": 25, "header_row": 7},
    {"file_name": "Rx5Day_Seasonal_Smoothed", "sheet_name": "Rx5Day Seasonal", "period": "SEASON", "start_row": 28,
     "end_row": 42, "header_row": 7},
    {"file_name": "Rx5Day_Monthly_Unsmoothed_Unstandardized", "sheet_name": "Rx5day Unstandardized", "period": "MONTH",
     "start_row": 11, "end_row": 25, "header_row": 7},
    {"file_name": "Rx5Day_Seasonal_Unsmoothed_Unstandardized", "sheet_name": "Rx5day Unstandardized",
     "period": "SEASON", "start_row": 32, "end_row": 46, "header_row": 28},
    {"file_name": "T10_Monthly_Unsmoothed", "sheet_name": "T10 Monthly", "period": "MONTH", "start_row": 11,
     "end_row": 25, "header_row": 7},
    {"file_name": "T10_Monthly_Smoothed", "sheet_name": "T10 Monthly", "period": "MONTH", "start_row": 28,
     "end_row": 42, "header_row": 7},
    {"file_name": "T10_Seasonal_Unsmoothed", "sheet_name": "T10 Seasonal", "period": "SEASON", "start_row": 11,
     "end_row": 25, "header_row": 7},
    {"file_name": "T10_Seasonal_Smoothed", "sheet_name": "T10 Seasonal", "period": "SEASON", "start_row": 28,
     "end_row": 42, "header_row": 7},
    {"file_name": "T10_Monthly_Unsmoothed_Unstandardized", "sheet_name": "T10 Unstandardized", "period": "MONTH",
     "start_row": 11, "end_row": 25, "header_row": 7},
    {"file_name": "T10_Seasonal_Unsmoothed_Unstandardized", "sheet_name": "T10 Unstandardized", "period": "SEASON",
     "start_row": 32, "end_row": 46, "header_row": 28},
    {"file_name": "T90_Monthly_Unsmoothed", "sheet_name": "T90 Monthly", "period": "MONTH", "start_row": 11,
     "end_row": 25, "header_row": 7},
    {"file_name": "T90_Monthly_Smoothed", "sheet_name": "T90 Monthly", "period": "MONTH", "start_row": 28,
     "end_row": 42, "header_row": 7},
    {"file_name": "T90_Seasonal_Unsmoothed", "sheet_name": "T90 Seasonal", "period": "SEASON", "start_row": 11,
     "end_row": 25, "header_row": 7},
    {"file_name": "T90_Seasonal_Smoothed", "sheet_name": "T90 Seasonal", "period": "SEASON", "start_row": 28,
     "end_row": 42, "header_row": 7},
    {"file_name": "T90_Monthly_Unsmoothed_Unstandardized", "sheet_name": "T90 Unstandardized", "period": "MONTH",
     "start_row": 11, "end_row": 25, "header_row": 7},
    {"file_name": "T90_Seasonal_Unsmoothed_Unstandardized", "sheet_name": "T90 Unstandardized", "period": "SEASON",
     "start_row": 32, "end_row": 46, "header_row": 28},
    {"file_name": "WP90_Monthly_Unsmoothed", "sheet_name": "WP90 Monthly", "period": "MONTH", "start_row": 11,
     "end_row": 25, "header_row": 7},
    {"file_name": "WP90_Monthly_Smoothed", "sheet_name": "WP90 Monthly", "period": "MONTH", "start_row": 28,
     "end_row": 42, "header_row": 7},
    {"file_name": "WP90_Seasonal_Unsmoothed", "sheet_name": "WP90 Seasonal", "period": "SEASON", "start_row": 11,
     "end_row": 25, "header_row": 7},
    {"file_name": "WP90_Seasonal_Smoothed", "sheet_name": "WP90 Seasonal", "period": "SEASON", "start_row": 28,
     "end_row": 42, "header_row": 7},
    {"file_name": "WP90_Monthly_Unsmoothed_Unstandardized", "sheet_name": "WP90 Unstandardized", "period": "MONTH",
     "start_row": 11, "end_row": 25, "header_row": 7},
    {"file_name": "WP90_Seasonal_Unsmoothed_Unstandardized", "sheet_name": "WP90 Unstandardized", "period": "SEASON",
     "start_row": 32, "end_row": 46, "header_row": 28},
    {"file_name": "ACI_Combined_Monthly_Unsmoothed", "sheet_name": "ACI Combined Monthly", "period": "MONTH",
     "start_row": 11,
     "end_row": 25, "header_row": 7},
    {"file_name": "ACI_Combined_Monthly_Smoothed", "sheet_name": "ACI Combined Monthly", "period": "MONTH",
     "start_row": 28,
     "end_row": 42, "header_row": 7},
    {"file_name": "ACI_Combined_Seasonal_Unsmoothed", "sheet_name": "ACI Combined Seasonal", "period": "SEASON",
     "start_row": 11,
     "end_row": 25, "header_row": 7},
    {"file_name": "ACI_Combined_Seasonal_Smoothed", "sheet_name": "ACI Combined Seasonal", "period": "SEASON",
     "start_row": 28,
     "end_row": 42, "header_row": 7}
]

for table in tables:
    load_spreadsheet_data(table["sheet_name"], table["period"], table["start_row"], table["end_row"],
                          table["header_row"]).to_csv(f"../data/{table["file_name"]}.csv", index=False, header=False)


script_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(os.path.dirname(script_path))
data_folder_path = os.path.join(parent_directory, 'data')
pattern = os.path.join(data_folder_path, '*Monthly*.csv')
matching_files = glob.glob(pattern)

running_df = None
for file in matching_files:
    df = pd.read_csv(file, header=[0, 1], index_col=0)
    df_melted = df.melt(var_name=["Year", "Month"], value_name="Value", ignore_index=False)
    df_melted.reset_index(inplace=True)
    df_melted.columns.values[0] = "Region"
    df_melted.columns.values[3] = Path(file).stem

    if running_df is None:
        running_df = df_melted
    else:
        running_df = pd.merge(running_df, df_melted, on=["Region", "Year", "Month"], how="outer")

running_df.to_csv(f"../data/Cleaned_Monthly_Data.csv", index=False, header=True)
