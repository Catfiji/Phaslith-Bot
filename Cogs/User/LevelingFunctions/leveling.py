import Cogs.Functions.database as db
from math import *
#;---------------------------------------------------------------------------
    # GETTERS AND SETTERS

# Get user level
def get_user_level(user_id):
    db.cursor.execute(f"SELECT LEVEL from users where ID = {user_id}")
    rows = db.cursor.fetchall()
    for row in rows:
        user_level_current = int(row["LEVEL"])
        return user_level_current

# ADD USER LEVEL ## Just used for leveling up
def add_user_level(user_id, amount):
    amount = int(amount)
    sql = f"UPDATE users SET LEVEL = {get_user_level(user_id) + amount} WHERE ID = {user_id}"
    db.cursor.execute(sql)
    db.data.commit()

# Get user EXP
def get_user_exp(user_id):
    db.cursor.execute(f"SELECT EXP from users where ID = {user_id}")
    rows = db.cursor.fetchall()
    for row in rows:
        user_level_current = int(row["EXP"])
        return user_level_current

# Add user XP
def add_exp(user_id, amount):
    amount = int(amount)
    sql = f"UPDATE users SET EXP = {get_user_exp(user_id) + amount} WHERE ID = {user_id}"
    db.cursor.execute(sql)
    db.data.commit()

# Remove user XP
def remove_exp(user_id, amount):
    amount = int(amount)
    sql = f"UPDATE users SET EXP = {get_user_exp(user_id) - amount} WHERE ID = {user_id}"
    db.cursor.execute(sql)
    db.data.commit()

# get exp required to level up
def get_exp_required(user_id):
    users_current_level = get_user_level(user_id)

    xp_required = 0
    for i in range(1, users_current_level+1, 1):
        xp_required += floor(users_current_level + 300.0 * pow(2.0, users_current_level / 7.0))
    output = int(floor((xp_required / 4)))
    return output

# level up player
def level_up(user_id):
    req = get_exp_required(user_id)
    if get_user_exp(user_id) >= req:
        remove_exp(user_id, req)
        add_user_level(user_id, 1)
        return True
    else:
        return False

#;---------------------------------------------------------------------------
