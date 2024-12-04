## File Structure

**Input file:** all_participants_raw_text.csv

The CSV file must include a column named text containing the text data for sentiment analysis.

**Output file**: vader_analysis.csv

The output file is saved in the same directory as the script and includes sentiment scores and labels for each text entry.

## Script Details

**Working Directory**: The script automatically sets the working directory to: /Users/claudiamoralesvaliente/Library/CloudStorage/OneDrive-TheUniversityofWesternOntario/PhD/Study 2/Python/VADER



## Main Steps:

- Load the dataset from all_participants_raw_text.csv.

- Check for the presence of the text column.

- Analyze sentiment for each text entry using VADER.

- Extract and save individual sentiment scores (neg, neu, pos, compound).

- Classify the overall sentiment into Positive, Negative, or Neutral.

- Save the results to vader_analysis.csv.
