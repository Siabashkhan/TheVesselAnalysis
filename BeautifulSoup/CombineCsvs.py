import os
import pandas as pd

# Set the directory path where your CSV files are located
directory_path = "/workspaces/beautiful-reddit-soup/CsvFiles"

# Get a list of all CSV files in the directory
csv_files = [file for file in os.listdir(directory_path) if file.endswith(".csv")]

# Check if there are any CSV files in the directory
if not csv_files:
    print("No CSV files found in the specified directory.")
else:
    # Initialize an empty list to store DataFrames
    dfs = []

    # Loop through each CSV file and append it to the list
    for csv_file in csv_files:
        file_path = os.path.join(directory_path, csv_file)
        df = pd.read_csv(file_path, header=None, names=['Column1'])  # Assume the column is named 'Column1'
        dfs.append(df)

    # Concatenate all DataFrames in the list into one DataFrame
    merged_data = pd.concat(dfs, ignore_index=True)

    # Save the merged DataFrame to a new CSV file
    output_file_path = "/workspaces/beautiful-reddit-soup/merged_data.csv"
    merged_data.to_csv(output_file_path, index=False)

    print(f"Merged data saved to {output_file_path}")
