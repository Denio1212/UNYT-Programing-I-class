"""
Exports the .txt file called expenses.txt, which houses all expense data, into JSON and CSV formats
"""
import pandas as pd
import json

def convert_to_csv(input_path, output_path, delimiter=" "):
    """
    Converts a .txt file to a .csv file
    :param input_path: the path of "expenses.txt" file
    :param output_path: The path of the output "expenses.csv" file
    :param delimeter: The seperator
    """
    df = pd.read_csv(input_path) # Turns .txt file into a Pandas Data Frame
    df.to_csv(output_path, index=False) # Using Pandas Library, we can then save it in a CSV format

def convert_to_json(input_path, output_path):
    """
    Converts a .txt file to a .json file
    :param input_path: the path of "expenses.txt" file
    :param output_path: the path of the output "expenses.json" file
    :param delimiter: The seperator
    """
    df = pd.read_csv(input_path) # Turns .txt file into a Pandas Data Frame
    df.to_json(output_path, orient="records", indent=4) # Using Pandas Library, we can then save it in a JSON format