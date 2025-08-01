import numpy as np

# Dataset: [Customer ID, Name, Loan Amount, Interest Rate %, Tenure in Years]
loan_data = np.array([
    [101, 'Alice', 5000, 5, 2],
    [102, 'Bob', 10000, 4.5, 5],
    [103, 'Charlie', 3000, 6, 1],
    [104, 'Diana', 8000, 3.5, 4],
    [105, 'Ethan', 4500, 5.2, 3]
], dtype=object)

# 1️⃣ Total loan amount taken by all customers
def calculate_total_loan(data):
    return sum([float(row[2]) for row in data])
# 3️2 Find the customer with the least repayment years
def find_least_tenure(data):
    return min(data, key=lambda row: int(row[4]))


def main():
    total_loan = calculate_total_loan(loan_data)
    print(f"Total Loan Amount Taken by All Customers: ${total_loan}")


    fastest = find_least_tenure(loan_data)
    print(f"Customer with Shortest Repayment Period: {fastest[1]} ({fastest[4]} years)")

if __name__ == "__main__":
    main()
