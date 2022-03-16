from app.database import get_db

# Clase4


def output_formatter(results):
    out = []
    for result in results:
        res_dict = {
            "id": result[0],
            "color": result[1],
            "license_plate": result[2],
            "v_type": result[3],
            "user_id": result[4],
            "activate": result[5]
        }
        out.append(res_dict)
    return out


def select_by_user_id(uid):
    cursor = get_db().execute(
        "SELECT * FROM vehicle WHERE user_id=?", (uid,))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)
#


def insert(vehicle_dict):
    value_tuple = (
        vehicle_dict["color"],
        vehicle_dict["license_type"],
        vehicle_dict["v_type"],
        vehicle_dict["id"],
        vehicle_dict["user_id"],
        vehicle_dict["active"],
    )

    stmt = """
        INSERT INTO vehicle (
        color,
        license_type,
        v_type,
        user_id
        ) VALUES (?, ?, ?)
    """
    cursor = get_db()
    last_row_id = cursor.execute(stmt, value_tuple)
    cursor.commit()
    cursor.close()


def scan():
    cursor = get_db().execute(
        "SELECT * FROM vehicle WHERE active=1", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def select_by_id(pk):
    cursor = get_db().execute(
        "SELECT * FROM vehicle WHERE id=?", (pk, ))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def update(pk, vehicle_data):
    value_tuple = (
        vehicle_data["color":],
        vehicle_data["license_type"],
        vehicle_data["v_type"],
        vehicle_data["user_id"],
        pk
    )
    stmt = """
        UPDATE user
        SET 
        color=?,
        license_type=?,
        v_type=?,
        user_id=?
        WHERE id=?
    """
    cursor = get_db()
    cursor.execute(stmt, value_tuple)
    cursor.commit()


def deactivate(pk):
    stmt = """
        UPDATE vehicle
        SET active=0
        WHERE id=?
    """
    cursor = get_db()
    cursor.execute(stmt, (pk, ))
    cursor.commit()
    cursor.close()
