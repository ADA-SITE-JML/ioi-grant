import psycopg2
import pickle
import os
import json
import sys


# def test():
#     print "test"


# if __name__ == "__main__":
#     test()

conn = psycopg2.connect(database="cmsdb", user="cmsuser",
                        password="cmspsw", host="192.168.33.115", port="5432")

cur = conn.cursor()

filename = 'last_sub_id'
with open(filename, 'a+b') as file:
    try:
        file.seek(0)
        if os.path.getsize("./" + filename) > 0:
            last_submission_id = pickle.load(file)
            # get next current submission based on the timestamp
            cur.execute(f"\
                SELECT *, (SELECT username FROM users where id = (SELECT user_id FROM participations where id = submissions.participation_id)) username\
                FROM submissions \
                WHERE id != {last_submission_id} \
                AND timestamp > (SELECT timestamp FROM submissions WHERE id={last_submission_id}) \
                AND official = true \
                ORDER BY timestamp ASC LIMIT 1")
            current_submission = cur.fetchall()[0]
            username = current_submission[7]
            data_dir = f"/var/local/lib/cms/submissions/{username}"
            # check the participant whom the curent submission belongs to if have submitted another submission for the same task before the current submission
            # if yes return filesystem address for both of them and some other extra info regarding the submissions
            # if not return only the current submission
            cur.execute(f"\
                WITH current_submission AS ( \
                    SELECT * \
                    FROM submissions \
                    WHERE id = {current_submission[0]} \
                ) \
                SELECT submissions.* \
                FROM submissions \
                INNER JOIN current_submission ON submissions.participation_id = current_submission.participation_id \
                WHERE submissions.task_id = current_submission.task_id \
                AND submissions.timestamp < current_submission.timestamp \
                AND submissions.official = true \
                ORDER BY submissions.timestamp DESC \
                LIMIT 1 \
                ")
            fetched_data = cur.fetchall()
            if fetched_data:
                prev_submission = fetched_data[0]
                json.dump(
                    {
                        'current_submission': {
                            'id': current_submission[0],
                            'participation_id': current_submission[1],
                            'task_id': current_submission[2],
                            'timestamp': str(current_submission[3]),
                            'language': current_submission[4],
                            'file_path': os.path.join(data_dir, f"'{current_submission[3]}'")
                        },
                        'previous_submission': {
                            'id': prev_submission[0],
                            'participation_id': prev_submission[1],
                            'task_id': prev_submission[2],
                            'timestamp': str(prev_submission[3]),
                            'language': prev_submission[4],
                            'file_path': os.path.join(data_dir, f"'{prev_submission[3]}'")
                        }
                    },
                    sys.stdout
                )
            else:
                json.dump(
                    {
                        'current_submission': {
                            'id': current_submission[0],
                            'participation_id': current_submission[1],
                            'task_id': current_submission[2],
                            'timestamp': str(current_submission[3]),
                            'language': current_submission[4],
                            'file_path': os.path.join(data_dir, f"'{current_submission[3]}'")
                        }
                    },
                    sys.stdout
                )
        else:
            # Same for here except since it is the first ever submission being considered only return the current one.
            cur.execute("\
                    SELECT *, (SELECT username FROM users where id = (SELECT user_id FROM participations where id = submissions.participation_id)) username \
                    FROM submissions \
                    WHERE official = true \
                    ORDER BY timestamp ASC \
                    LIMIT 1\
                        ")
            current_submission = cur.fetchall()[0]
            username = current_submission[7]
            data_dir = f"/var/local/lib/cms/submissions/{username}"
            json.dump(
                {
                    'current_submission': {
                        'id': current_submission[0],
                        'participation_id': current_submission[1],
                        'task_id': current_submission[2],
                        'timestamp': str(current_submission[3]),
                        'language': current_submission[4],
                        'file_path': os.path.join(data_dir, f"'{current_submission[3]}'")
                    }
                },
                sys.stdout
            )
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
        with open(filename, 'wb') as outfile:
            pickle.dump(current_submission[0], outfile)
