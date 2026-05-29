"""Homework module for data subsets in pandas."""

import os
import pandas as pd


def create_specific_columns_csv():
    """Extract specific columns from input CSV and save to output."""
    # Define input and output paths
    input_file = "files/input/truck_event_text_partition.csv"
    output_dir = "files/output"
    output_file = os.path.join(output_dir, "specific-columns.csv")
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Read the input CSV
    df = pd.read_csv(input_file)
    
    # Extract specific columns (meaningful subset for analysis)
    specific_columns = [
        'driverId',
        'truckId', 
        'eventType',
        'longitude',
        'latitude',
        'driverName',
        'routeName',
        'eventDate'
    ]
    
    # Select only columns that exist in the dataframe
    available_columns = [col for col in specific_columns if col in df.columns]
    df_specific = df[available_columns]
    
    # Save to output
    df_specific.to_csv(output_file, index=False)


# Create the output file when module is imported
create_specific_columns_csv()
