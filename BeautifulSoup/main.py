import csv
from bs4 import BeautifulSoup
import os

def process_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r") as f:
                doc = BeautifulSoup(f, "html.parser")

                tags = doc.find_all("p")

                csvfile_path = os.path.join("/workspaces/beautiful-reddit-soup/CsvFiles", os.path.splitext(filename)[0] + ".csv")
                with open(csvfile_path, "w") as csvfile:
                    csvwriter = csv.writer(csvfile)
                    for tag in tags:
                        csvwriter.writerow([tag.string])

if __name__ == "__main__":
    directory = "/workspaces/beautiful-reddit-soup/WebPages"
    process_files(directory)
