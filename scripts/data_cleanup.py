import glob
import os
from pathlib import Path
from typing import TypedDict, List, Optional

import pandas
import pandas as pd


def main():
    for table in tables:
        load_spreadsheet_data(table["sheet_name"], table["period"], table["start_row"], table["end_row"],
                              table["header_row"]).to_csv(f"../data/{table["file_name"]}.csv", index=False,
                                                          header=False)

    monthly_files: List[str] = get_data_files("*_Monthly_*.csv")
    seasonal_files: List[str] = get_data_files("*_Seasonal_*.csv")

    combine_file_data(monthly_files, "Month").to_csv(f"../data/Cleaned_Data_Monthly.csv", index=False, header=True)
    combine_file_data(seasonal_files, "Season").to_csv(f"../data/Cleaned_Data_Seasonal.csv", index=False, header=True)


def get_data_files(pattern: str) -> List[str]:
    """Returns a list of file paths for files in the data directory whose file name matches the provided pattern.

    :param pattern: the regex that returned file names should match
    :return: a list of file paths for matching files
    """
    script_path: str = os.path.abspath(__file__)
    parent_directory: str = os.path.dirname(os.path.dirname(script_path))
    data_folder_path: str = os.path.join(parent_directory, 'data')
    pattern: str = os.path.join(data_folder_path, pattern)
    return glob.glob(pattern)


def combine_file_data(file_paths: List[str], period_header: str) -> pandas.DataFrame:
    """Combines the provided data files into a single DataFrame, pivoting Year and Period into columns.

    :param file_paths: a list of paths to the data files that should be combined
    :param period_header: the title that should be given to the column representing a portion of the year ("Month", "Season")
    :return: a DataFrame containing columns for Region, Month, Period, and each provided file
    """
    combined_df: Optional[pandas.DataFrame] = None
    for file_path in file_paths:
        df: pandas.DataFrame = pd.read_csv(file_path, header=[0, 1], index_col=0)
        df_melted: pandas.DataFrame = df.melt(var_name=["Year", period_header], value_name="Value", ignore_index=False)
        df_melted.reset_index(inplace=True)
        df_melted.columns.values[0] = "Region"
        df_melted.columns.values[3] = Path(file_path).stem

        if combined_df is None:
            combined_df = df_melted
        else:
            combined_df = pd.merge(combined_df, df_melted, on=["Region", "Year", period_header], how="outer")

    # Have to convert to float before casting to int to avoid type casting error
    combined_df["Year"] = combined_df["Year"].astype(float).astype(int)
    combined_df[period_header] = combined_df[period_header].astype(float).astype(int)
    return combined_df


def load_spreadsheet_data(sheet_name: str, period: str, start_row: int, end_row: int, header_row: int) -> pd.DataFrame:
    """Loads a table from the Original_ACI_Dataset.xlsx file into a DataFrame.

    :param sheet_name: the name of the Excel sheet the data should be sourced from
    :param period: whether the data is monthly or seasonal. Valid options: "MONTH", "SEASON"
    :param start_row: the row in the sheet that the table's data starts on
    :param end_row: the row in the sheet that the table's data ends on
    :param header_row: the row in the sheet that the table's header starts on
    :return: a DataFrame containing the data from the described table
    """
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

if __name__ == "__main__":
    main()
