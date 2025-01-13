import sqlite3

def random_Restaurant(username):
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()

    cursor.execute('SELECT u_id FROM Users WHERE Name = ?', (username,))
    user_id = cursor.fetchone()[0]

    cursor.execute('''
        SELECT Restaurant.r_id, r_name, a_name, t_name
        FROM Restaurant
        JOIN Area ON Restaurant.a_id = Area.a_id
        JOIN Restaurant_Types ON Restaurant.r_id = Restaurant_Types.r_id
        JOIN Type ON Restaurant_Types.t_id = Type.t_id
        WHERE Restaurant.r_id NOT IN (
            SELECT h_id
            FROM Blacklist
            WHERE u_id = ?
        )
        ORDER BY RANDOM()
        LIMIT 1
    ''', (user_id,))
    
    result = cursor.fetchone()
    conn.close()

    if result:
        return {
            'restaurant_id': result[0],
            'restaurant_name': result[1],
            'area_name': result[2],
            'type_name': result[3]
        }
    else:
        return {
            'restaurant_id': None,
            'restaurant_name': "No restaurant found",
            'area_name': "挖哩勒",
            'type_name': "哭出來"
        }


print(random_Restaurant('billy'))