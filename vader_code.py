#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:55:45 2024

@author: claudiamoralesvaliente
"""

import os
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Set your working directory (the path you cannot change in Spyder)
working_dir = '/Users/claudiamoralesvaliente/Library/CloudStorage/OneDrive-TheUniversityofWesternOntario/PhD/Study 2/Python/VADER'
os.chdir(working_dir)  # Change the current working directory
print(f"Working directory set to: {os.getcwd()}")

# Specify your dataset file name
file_name = 'all_participants_raw_text.csv'

# Load the dataset
df = pd.read_csv(file_name)

# Display the first few rows to confirm data loading
print(df.head())

# Ensure you have a column named 'text' containing the data for sentiment analysis
if 'text' not in df.columns:
    raise ValueError("The dataset must contain a column named 'text' for analysis.")

# Initialize the VADER Sentiment Intensity Analyzer
analyzer = SentimentIntensityAnalyzer()

# Apply VADER sentiment analysis to the 'text' column
df['Sentiment_Scores'] = df['text'].apply(lambda x: analyzer.polarity_scores(str(x)))

# Extract individual scores (neg, neu, pos, compound) into separate columns
df['Negative'] = df['Sentiment_Scores'].apply(lambda x: x['neg'])
df['Neutral'] = df['Sentiment_Scores'].apply(lambda x: x['neu'])
df['Positive'] = df['Sentiment_Scores'].apply(lambda x: x['pos'])
df['Compound'] = df['Sentiment_Scores'].apply(lambda x: x['compound'])

# Label the overall sentiment based on the compound score
df['Sentiment_Label'] = df['Compound'].apply(
    lambda x: "Positive" if x > 0.05 else ("Negative" if x < -0.05 else "Neutral")
)

# Save the results to a new CSV file
output_path = '/Users/claudiamoralesvaliente/Library/CloudStorage/OneDrive-TheUniversityofWesternOntario/PhD/Study 2/Python/VADER/vader_analysis.csv'
df.to_csv(output_path, index=False)

# Display the first few rows of the updated DataFrame
print(df.head())

# Print the path of the output file
print(f"vader analysis saved to: {output_path}")
