import Cogs.Functions.database as db
#;---------------------------------------------------------------------------
    # GETTERS AND SETTERS

# Get User Balance
def get_user_wallet(user_id):
    db.cursor.execute(f"SELECT WALLET from users where ID = {user_id}")
    rows = db.cursor.fetchall()
    for row in rows:
        user_balance = int(row["WALLET"])
        return user_balance

# Get user bank balance
def get_user_bank(user_id):
    db.cursor.execute(f"SELECT BANK from users where ID = {user_id}")
    rows = db.cursor.fetchall()
    for row in rows:
        user_bank_current = int(row["BANK"])
        return user_bank_current

# add money to player wallet
def add_wallet_bal(user_id, amount):
    user_balance = get_user_wallet(user_id)
    sql = f"UPDATE users SET WALLET = {user_balance + amount} WHERE ID = {user_id}"
    db.cursor.execute(sql)
    db.data.commit()

# remove money from player wallet
def remove_wallet_bal(user_id, amount):
    user_balance = get_user_wallet(user_id)
    sql = f"UPDATE users SET WALLET = {user_balance - amount} WHERE ID = {user_id}"
    db.cursor.execute(sql)
    db.data.commit()

# add money to player bank
def add_bank_bal(user_id, amount):
    user_bank = get_user_bank(user_id)
    sql = f"UPDATE users SET BANK = {user_bank + amount} WHERE ID = {user_id}"
    db.cursor.execute(sql)
    db.data.commit()

# add money to player bank
def remove_bank_bal(user_id, amount):
    user_bank = get_user_bank(user_id)
    sql = f"UPDATE users SET BANK = {user_bank - amount} WHERE ID = {user_id}"
    db.cursor.execute(sql)
    db.data.commit()

    # TRANSFERRING

# deposit from wallet into bank
def deposit(user_id, amount):
    if get_user_wallet(user_id) - amount >= 0:
        remove_wallet_bal(user_id, amount)
        add_bank_bal(user_id,amount)
        return True
    else:
        return False

# withdrawl from bank into wallet
def withdrawl(user_id, amount):
    if get_user_bank(user_id) - amount >= 0:
        add_wallet_bal(user_id, amount)
        remove_bank_bal(user_id, amount)
        return True
    else:
        return False

#;---------------------------------------------------------------------------