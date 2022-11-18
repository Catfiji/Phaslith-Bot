import json
from Cogs.Functions.database import *

#;- Get user inventory
def get_user_inventory(user_id):
    cursor.execute(f"SELECT INVENTORY from userinventory where ID = {user_id}")
    rows = cursor.fetchall()
    for row in rows:
        user_inv = row["INVENTORY"]
        return user_inv

    cursor.reset()

#;- Get Readable data
def get_json_inventory(unloaded_data):
    output = json.loads(unloaded_data)
    return output

#;- Check item
def check_item(dictonary, item):
    for key, value in dictonary.items():
        if item == key:
            return True
        else:
            return False

#;- Add a item
def add_item(user_id, item, amount):
    user_inv = get_json_inventory(get_user_inventory(user_id))

    if check_item(user_inv, item):
        user_inv[item] += amount
    else:
        user_inv[item] = amount

    sql = f'UPDATE `userinventory` SET `INVENTORY` = (%s) WHERE `ID` = (%s)'
    val = (json.dumps(user_inv), user_id)
    cursor.execute(sql,val)
    data.commit()

#;- Remove a item
def remove_item(user_id, item, amount):
    user_inv = get_json_inventory(get_user_inventory(user_id))

    if check_item(user_inv, item):
        user_inv[item] -= amount

    sql = f'UPDATE `userinventory` SET `INVENTORY` = (%s) WHERE `ID` = (%s)'
    val = (json.dumps(user_inv), user_id)
    cursor.execute(sql, val)
    data.commit()

#;- Delete a item
def delete_item(user_id, item):
    user_inv = get_json_inventory(get_user_inventory(user_id))

    if check_item(user_inv, item):
        del user_inv[item]

    sql = f'UPDATE `userinventory` SET `INVENTORY` = (%s) WHERE `ID` = (%s)'
    val = (json.dumps(user_inv), user_id)
    cursor.execute(sql, val)
    data.commit()