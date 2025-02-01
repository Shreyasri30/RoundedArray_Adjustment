# Rounding Adjustment Logic

## Overview
This Python script processes a nested list of numbers, rounds them to the nearest lakh (100,000), adjusts rounding inconsistencies, and reconstructs the original nested structure.

## Features
✔ Flattens nested lists of numbers  
✔ Rounds numbers to the nearest lakh  
✔ Ensures total sum consistency after rounding  
✔ Reconstructs the original nested structure  
✔ Accepts JSON input from user or file  
✔ Outputs results in formatted JSON  
✔ Provides debugging logs for verification  

## How It Works

### 1. **Flattening Nested Lists**
- Extracts all numbers from the input JSON.
- Converts nested lists into a flat list.

### 2. **Computing Sum and Rounding**
- Calculates the total sum of all numbers before rounding.
- Rounds each number to the nearest lakh.

### 3. **Adjusting for Rounding Errors**
- Ensures that the sum of rounded numbers matches the rounded total.
- Spreads adjustments evenly across multiple numbers.

### 4. **Reconstructing the Nested Structure**
- Places the adjusted rounded numbers back into their original nested structure.

### 5. **Displaying and Saving Output**
- Shows formatted JSON output.
- Saves output to a file if requested.

## Installation

### Prerequisites
- Python 3.x installed
- JSON file containing numbers (optional)

