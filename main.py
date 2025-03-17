import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import requests
import io
import zipfile
import os

# URL of the data file
url = "https://techsummer.ringieraxelspringer.com/2025/data.zip"


# Create a function to download and extract the data
def download_and_extract(url):
    print(f"Downloading data from {url}...")
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(
            f"Failed to download the file. Status code: {response.status_code}"
        )

    print("Download complete. Extracting ZIP archive...")

    # Create a zip file object from the downloaded content
    zip_file = zipfile.ZipFile(io.BytesIO(response.content))

    # List the contents of the ZIP file
    file_list = zip_file.namelist()
    print(f"Files in the archive: {file_list}")

    # Extract the content (assuming there's only one text file)
    txt_file = None
    for file_name in file_list:
        if file_name.endswith(".txt"):
            txt_file = file_name
            break

    if not txt_file:
        txt_file = file_list[0]  # If no .txt found, take the first file

    print(f"Extracting file: {txt_file}")
    zip_file.extract(txt_file)

    return txt_file


# Process the data file and count frequencies
def analyze_data(file_path):
    print(f"Analyzing data from {file_path}...")
    frequencies = {}

    with open(file_path, "r") as file:
        count = 0
        for line in file:
            try:
                value = float(line.strip())
                if value in frequencies:
                    frequencies[value] += 1
                else:
                    frequencies[value] = 1

                count += 1
                if count % 1000000 == 0:
                    print(f"Processed {count} lines...")
            except ValueError:
                print(f"Skipping invalid line: {line.strip()}")

    print(f"Total lines processed: {count}")
    return frequencies


# Create visualization for the data
def visualize_and_get_solution(frequencies):
    # Find the most frequent values
    sorted_freq = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    top_values = sorted_freq[:10]  # Get top 10 for display

    print("\nTop 10 most frequent values:")
    for value, count in top_values:
        print(f"{value}: {count} occurrences")

    # The two most common values are the solution
    solution = f"{sorted_freq[0][0]},{sorted_freq[1][0]}"
    print(f"\nSolution: {solution}")

    # Create a DataFrame for visualization
    top_n = 20  # Show top 20 in histogram
    plot_data = pd.DataFrame(sorted_freq[:top_n], columns=["Value", "Count"])

    # Generate the histogram using seaborn
    plt.figure(figsize=(14, 8))
    sns.barplot(x="Value", y="Count", data=plot_data)
    plt.title("Top 20 Most Frequent Values")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("frequency_histogram.png")

    # Optionally, export to CSV for further analysis
    plot_data.to_csv("top_frequencies.csv", index=False)

    return solution


# Main execution
def main():
    try:
        # Download and extract the data
        file_path = download_and_extract(url)

        # Analyze the data
        frequencies = analyze_data(file_path)

        # Visualize and get the solution
        solution = visualize_and_get_solution(frequencies)

        # Clean up - remove the extracted file after processing
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Removed temporary file: {file_path}")

        print(f"Final solution: {solution}")
        return solution

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    main()
