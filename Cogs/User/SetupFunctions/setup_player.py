from Cogs.Functions import database as db

default_level = 1
default_xp = 0
default_wallet = 0
default_bank = 0
default_steps = 0
# skills
default_strength = 5
default_agility = 5
default_defense = 5

default_mining_lvl = 1
default_mining_xp = 0
default_fishing_lvl = 1
default_fishing_xp = 0
default_farming_lvl = 1
default_farming_xp = 0
default_cooking_lvl = 1
default_cooking_xp = 0
default_blacksmith_lvl = 1
default_blacksmith_xp = 0
default_enchant_lvl = 1
default_enchant_xp = 0
default_wood_lvl = 1
default_wood_xp = 0

defualt_location_id = 1

def setup_player(user_id):
    users_data_a = """INSERT INTO users (ID, LEVEL, EXP, WALLET, BANK, LOCATION_ID) VALUES (%s, %s, %s, %s, %s, %s)"""
    users_data_a_val = (
        user_id,
        default_level,
        default_xp,
        default_wallet,
        default_bank,
        defualt_location_id
    )

    users_data_b = "INSERT INTO usersskills (ID, STRENGTH, AGILITY, DEFENSE, MINING_LEVEL, MINING_XP, FISHING_LEVEL, FISHING_XP, FARMING_LEVEL, FARMING_XP, COOKING_LEVEL, COOKING_XP, BLACKSMITHING_LEVEL, BLACKSMITHING_XP, ENCHANTING_LEVEL, ENCHANTING_XP, WOODCUTTING_LEVEL, WOODCUTTING_XP) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    users_data_b_val = (
        user_id,
        default_strength,
        default_agility,
        default_defense,
        default_mining_lvl,
        default_mining_xp,
        default_fishing_lvl,
        default_fishing_xp,
        default_farming_lvl,
        default_farming_xp,
        default_cooking_lvl,
        default_cooking_xp,
        default_blacksmith_lvl,
        default_blacksmith_xp,
        default_enchant_lvl,
        default_enchant_xp,
        default_wood_lvl,
        default_wood_xp
    )

    users_data_c = "INSERT INTO usersinfo (ID, STEPS_TAKEN) VALUES (%s, %s)"
    users_data_c_val = (
        user_id,
        default_steps
    )
    try:
        db.cursor.execute(users_data_a, users_data_a_val)
        db.data.commit()
        db.cursor.reset()
        db.cursor.execute(users_data_b, users_data_b_val)
        db.data.commit()
        db.cursor.reset()
        db.cursor.execute(users_data_c, users_data_c_val)
        db.data.commit()
        db.cursor.reset()
    except Exception as e:
        print(e)

    print(f"created new user {user_id} in 3 databases")
    return True
