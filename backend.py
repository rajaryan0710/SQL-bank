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

def change_accountNo(old_accountNo, new_accountNo):
    query= "select accountNo from accounts;"
    cur.execute(query)
    accountNos= cur.fetchall()
    accountNos = [acc[0] for acc in accountNos]
    print("The taken account nos are: ", accountNos)

    if new_accountNo not in accountNos:
        values = (new_accountNo, old_accountNo)
        query1 = "UPDATE accounts SET accountNo = ? WHERE accountNo = ?;"
        cur.execute(query1, values)
        conn.commit()
        print(f"update accountNo from {old_accountNo} to {new_accountNo}")
    else:
        print("Check, account No already taken.")




