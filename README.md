# Data ETL Project

## Overview
This project performs Extract, Transform, and Load (ETL) operations on borrower data. It includes data extraction from a CSV file, transformation of data, visualization, and the generation of a collection risk score for each borrower.

## Features
- **Data Extraction:** Reads data from a CSV file.
- **Data Transformation:** Standardizes email addresses, phone numbers, and adds new columns like Income Level and Financial Status.
- **Visualization:** Generates visualizations to understand the distribution of borrowers based on various attributes.
- **Collection Risk Score:** Calculates and ranks borrowers based on a collection risk score.

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/data-etl-project.git
Navigate to the project directory:
bash
Copy code
cd data-etl-project
Update the file_path variable in etl.py to point to your CSV file.
Run the script:
bash
Copy code
python etl.py
Requirements
pandas
numpy
matplotlib
seaborn
You can install the required packages using pip:

bash
Copy code
pip install pandas numpy matplotlib seaborn

Commit and Push:

Stage and commit your changes:
bash
Copy code
git add etl.py README.md
git commit -m "Add ETL script and README"
Push your changes to GitHub:
bash
Copy code
git push origin main
## Instructions
1. Ensure you have Python and the required libraries installed.
2. Place the `10k_borrowers_data.csv` file in the same directory as `etl_script.py`.
3. Run the `etl_script.py` script:


## Contact
For any questions or issues, please contact [sauravjha62@gmail.com].
