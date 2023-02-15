def get_feed(user_id, limit, db, config):
    with db.cursor() as cursor:
        cursor.execute(
            """
            SELECT * 
            FROM feed_action
            WHERE user_id = %(user_id)s
                AND time > %(start_date)s
            ORDER BY(time)
            LIMIT %(limit)s
            """,
            {"user_id": user_id, "limit": limit, "start_date": config["feed_start_date"]}
        )
        return cursor.fetchall()

def get_likes(user_id, limit, db, config):
    with db.cursor() as cursor:
        cursor.execute(
            """
            SELECT *
            FROM feed_action
            WHERE user_id = %(user_id)s 
                  AND action = 'like'
                  AND time > %(start_date)s
            ORDER BY(time)
            LIMIT %(limit)s
            """,
            {"user_id": user_id, "limit": limit, "start_date": config["feed_start_date"]}
        )
        return cursor.fetchall()