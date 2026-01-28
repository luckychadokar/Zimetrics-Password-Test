# Password Strength Regex Tester

## Project Goal
This project validates the strength of passwords using Python and regular expressions based on defined security rules.

## Setup Instructions
1. Install Python on your system
2. Open terminal in the project folder
3. Run the script using:
   python main.py

## Logic
The program checks each password against the following conditions:
- Minimum length of 8 characters
- Contains at least one numeric digit
- Contains at least one special character

Python's `re` (regular expression) module is used to perform these validations efficiently.

## Challenges Faced
The main challenge was designing accurate regex patterns to correctly validate numbers and special characters. This was resolved by testing multiple cases and refining the patterns.

## Output Screenshot
<img width="1919" height="1015" alt="image" src="https://github.com/user-attachments/assets/2455b85e-2369-4de9-a5e4-d2ca9119bc1b" />


## Future Improvements
- Add uppercase and lowercase character validation
- Allow user input instead of a hardcoded password list
- Export validation results to a file

