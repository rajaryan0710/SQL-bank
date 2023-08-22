import sqlite3

conn = sqlite3.connect('bankData.db')
cur = conn.cursor()

def create_account(name, phoneNo, age):
    balance = 0
    query = "INSERT INTO accounts (name, balance, phoneNo, age) VALUES (?,?,?,?);"
    values = (name, balance, phoneNo, age) 
    cur.execute(query, values)  
    conn.commit()
    print(f"Account successfully created with {name}, {phoneNo}, and {age}")

def delete_account(accountNo):
    values = (accountNo,)
    query = "DELETE FROM accounts WHERE accountNo = (?);"
    cur.execute(query, values)
    conn.commit()
    print(f"Account deleted with {accountNo}")

def add_balance(accountNo, amount):
    query = "UPDATE accounts SET balance = balance + ? WHERE accountNo = ?;"
    values = (amount, accountNo)
    cur.execute(query, values)
    conn.commit()
    print(f"Added {amount} in the account {accountNo}")

def withdraw(accountNo, amount):
    balance_query = "SELECT balance from accounts WHERE accountNo = ?;"
    cur.execute(balance_query, (accountNo,))
    balance = cur.fetchone()[0]  # Fetch the balance value from the result

    if balance < amount:
        print("Deposit some money first, mon cheri")
    else:
        query = "UPDATE accounts SET balance = balance - ? WHERE accountNo = ?;"
        values = (amount, accountNo)
        cur.execute(query, values)
        conn.commit()
        print(f"Withdrew {amount} from account {accountNo}")


