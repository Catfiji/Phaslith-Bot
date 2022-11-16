
import Cogs.Functions.database as db

#;---------------------------------------------------------------------------

#;- Get the ID of the players location
def get_user_location_id(user_id):
    db.cursor.execute(f"SELECT LOCATION_ID from users where ID = {user_id}")
    rows = db.cursor.fetchall()
    for row in rows:
        user_location = int(row["LOCATION_ID"])
        return user_location

#;- Get Information of a location
def get_location_information(location_id):
    db.cursor.execute(f"SELECT * from locations where ID = {location_id}")
    rows = db.cursor.fetchall()
    for row in rows:
        location_id = int(row["ID"])
        location_name = str(row["NAME"])
        location_mchance = int(row["MONSTERCHANCE"])
        location_mingold = int(row["MINGOLD"])
        location_maxgold = int(row["MAXGOLD"])
        location_minxp = int(row["MINEXP"])
        location_maxxp = int(row["MAXEXP"])
        location_info = [location_id, location_name, location_mchance, location_mingold, location_maxgold, location_minxp, location_maxxp]
        return location_info

#;---------------------------------------------------------------------------
