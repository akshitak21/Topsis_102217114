import sys
import pandas as pd
import numpy as np

def process_data(input, weights, impacts, output):
    try:
        # Reading the input file into a pandas DataFrame
        data = pd.read_csv(input)

        # Parsing weights and impacts
        weights = np.array(list(map(float, weights.split(','))))
        impacts = impacts.split(',')

        if len(weights) != len(impacts) or len(weights) != data.shape[1]:
            raise ValueError("The number of weights and impacts must match the number of columns in the DataFrame.")

        # Normalize the data
        normalized_data = data / np.sqrt((data**2).sum())

        # Applying weights
        weighted_data = normalized_data * weights

        # Adjust for impacts
        for i, impact in enumerate(impacts):
            if impact == '-':
                weighted_data.iloc[:, i] = -weighted_data.iloc[:, i]

        # Calculate scores (example: sum of weighted values per row)
        scores = weighted_data.sum(axis=1)
        data['Score'] = scores

        # Saving the result to the output file
        data.to_csv(output, index=False)

        print(f"Data has been processed and saved to {output}.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Ensure the correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: python <script_name.py> <input> <weights> <impacts> <output>")
        sys.exit(1)

    # Parse command-line arguments
    input = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output = sys.argv[4]

    # Call the processing function
    process_data(input, weights, impacts, output)
