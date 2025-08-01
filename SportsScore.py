import pandas as pd

# Sample player data: Name, Age, Runs
def create_score_dataframe():
    data = {
        "Player": ["Kohli", "Rohit", "Gill", "Dhoni", "Hardik"],
        "Age": [35, 36, 24, 42, 30],
        "Runs": [1200, 980, 750, 1600, 890]
    }
    return pd.DataFrame(data)

# 1️⃣ Function to calculate average score
def get_average_score(df):
    return df["Runs"].mean()

# 2️⃣ Function to count players above age 30
def count_players_above_age(df, age=30):
    return df[df["Age"] > age].shape[0]

# 🧪 Sample usage
if __name__ == "__main__":
    df = create_score_dataframe()
    print("Player Data:")
    print(df)

    avg_score = get_average_score(df)
    print(f"\nAverage Score of Players: {avg_score:.2f}")

    senior_count = count_players_above_age(df)
    print(f"Number of Players Aged Above 30: {senior_count}")
