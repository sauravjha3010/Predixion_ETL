import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Data Extraction
def extract_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"Data extracted successfully. Shape: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None

# 2. Data Transformation
def transform_data(df):
    # Standardize email domains
    df['Email Address'] = df['Email Address'].str.replace(r'@.*', '@gmail.com', regex=True)
    
    # Standardize phone numbers
    df['Phone Number'] = df['Phone Number'].astype(str).str.replace(r'\D', '', regex=True).apply(lambda x: '+91' + x.zfill(10)[-10:])
    
    # Add Income Level and Financial Status
    np.random.seed(42)  # For reproducibility
    df['Income Level'] = np.random.choice(['low', 'medium', 'high'], size=len(df), p=[0.33, 0.33, 0.34])
    df['Financial Status'] = np.random.choice(['stable', 'semi-stable', 'unstable'], size=len(df), p=[0.33, 0.33, 0.34])
    
    # Convert necessary columns to numeric
    df['Loan Amount'] = pd.to_numeric(df['Loan Amount'], errors='coerce')
    df['Interest Rate'] = pd.to_numeric(df['Interest Rate'], errors='coerce')
    df['Days Left to Pay Current EMI'] = pd.to_numeric(df['Days Left to Pay Current EMI'], errors='coerce')
    
    # Convert 'Date of Birth' to datetime
    df['Date of Birth'] = pd.to_datetime(df['Date of Birth'], format='%d-%m-%Y', errors='coerce')
    
    print("Data transformed successfully")
    return df

# 3. Visualization
def visualize_data(df):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='Gender')
    plt.title('Borrowers by Gender')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='Marital Status')
    plt.title('Borrowers by Marital Status')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='Language Preference')
    plt.title('Borrowers by Language Preference')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='Loan Type')
    plt.title('Borrowers by Loan Type')
    plt.show()

    plt.figure(figsize=(12, 6))
    sns.histplot(data=df, x='Credit Score', bins=20)
    plt.title('Distribution of Credit Scores')
    plt.show()

# 4. Generate Collection Risk Score
def generate_collection_risk_score(df):
    # Calculate Payment History Score
    df['PH_Score'] = np.where(df['Delayed Payment'] == 'No', 30 * 0.30, 
                              np.where(df['Delayed Payment'] == 'Yes', 15 * 0.30, 0))

    # Calculate Outstanding Debt Amount Score
    df['TotalAmountToBePaid'] = df['Loan Amount'] / df['Loan Term']
    df['ODA_Score'] = (1 - (df['Loan Amount'] / df['TotalAmountToBePaid'])) * 20 * 0.20

    # Calculate Income Level Score
    df['IL_Score'] = np.where(df['Income Level'] == 'high', 20 * 0.20,
                              np.where(df['Income Level'] == 'medium', 10 * 0.20, 0))

    # Calculate Financial Status Score (as proxy for Employment Status)
    df['ES_Score'] = np.where(df['Financial Status'] == 'stable', 15 * 0.15,
                              np.where(df['Financial Status'] == 'semi-stable', 7.5 * 0.15, 0))

    # Calculate Credit Score
    df['CS_Score'] = (df['Credit Score'] / 850) * 15 * 0.15

    # Calculate total Collection Risk Score
    df['CollectionRiskScore'] = df['PH_Score'] + df['ODA_Score'] + df['IL_Score'] + df['ES_Score'] + df['CS_Score']

    # Rank borrowers based on collection risk score
    df['Rank'] = df['CollectionRiskScore'].rank(method='dense', ascending=False)
    return df

# Main execution
if __name__ == "__main__":
    file_path = "/content/10k_borrowers_data.csv"  # Replace with your actual file path
    
    # ETL Process
    df = extract_data(file_path)
    if df is not None:
        df_transformed = transform_data(df)
        
        # Visualization
        visualize_data(df_transformed)
        
        # Generate Collection Risk Score
        df_with_scores = generate_collection_risk_score(df_transformed)
        
        # Display top 5 borrowers with the highest collection risk score
        print(df_with_scores.nlargest(5, 'CollectionRiskScore'))
        
        print("Process complete. Collection risk scores generated.")
