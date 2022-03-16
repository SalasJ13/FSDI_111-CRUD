from app.database import get_db


def get_users_and_vehicles_join():
    stm = """
        select 
        user.last_name,
        user.first_name,
        user.hobbies,
        user.active, 
        vehicle.license_plate,
        vehicle.color,
        vehicle.v_type as vehicle_type,
        vehicle_type.description 
        from user inner join vehicle on user.id=vehicle.user_id 
        inner join vehicle_type on vehicle.v_type = vehicle_type;"
    """
    cursor = get_db().execute(stm, ())
    results = cursor.fetchall()
    out = []
    for result in results:
        res_dict = {}
        res_dict = {
            "user_first_name": result[0],
            "user_last_name": result[1],
            "user_hobbies": result[2],
            "user_activate": "true" if result[3] == 1 else "false",
            "vehicle_license_plate": result[4],
            "vehicle_color": result[5],
            "vehicle_type": result[6]
        }
        out.append(res_dict)
    return out
