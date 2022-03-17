from app.database import get_db


def get_users_and_vehicles_join():
    stmt = """
        select 
        user.last_name,
        user.first_name,
        user.hobbies,
        user.active, 
        vehicle.color,
        vehicle.license_plate,
        vehicle_type.description  
        from user 
        inner join vehicle on user.id = vehicle.user_id 
        inner join vehicle_type on vehicle.v_type = vehicle_type.id
        
    """
    cursor = get_db().execute(stmt, ())
    results = cursor.fetchall()
    cursor.close()
    out = []
    for result in results:
        res_dict = {}
        res_dict = {
            "user_first_name": result[0],
            "user_last_name": result[1],
            "user_hobbies": result[2],
            "user_activate": True if result[3] == 1 else False,
            # "vehicle_license_plate": result[4],
            "vehicle_color": result[4],
            "vehicle_type": result[5]
        }
        out.append(res_dict)
    return out
