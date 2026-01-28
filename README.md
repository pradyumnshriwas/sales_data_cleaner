# Sales Data Cleaner

## Project Title & Goal
A Python script that cleans messy sales CSV data, removes duplicates, converts prices, and outputs a structured JSON report.

## Setup Instructions
```bash
python main.py```

## The Logic (How you thought)

### Why did you choose this approach?
I chose a simple Python-based approach using built-in csv and json libraries to ensure the solution is lightweight, easy to understand, and runs locally without external dependencies.

### What was the hardest bug you faced, and how did you fix it?
The hardest part was handling inconsistent price formats containing dollar signs and quotes. I fixed this by cleaning the price strings before converting them into float values.

## Output Screenshots
Screenshot of the generated clean_sales.json file opened in a text editor showing the cleaned and converted data.

## Future Improvements
If I had two more days, I would add proper logging, validation for incorrect data entries, and unit tests to make the script more robust and production-ready.


