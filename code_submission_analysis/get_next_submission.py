import psycopg2
import pickle
import os
import json

conn = psycopg2.connect(database="cmsdb", user="cmsuser",
                        password="cmspsw", host="192.168.33.115", port="5432")

cur = conn.cursor()

filename = 'last_sub_id'
with open(filename, 'a+b') as file:
    file.seek(0)
    if os.path.getsize("./" + filename) > 0:
        last_submission_id = pickle.load(file)
        # get next current submission based on the timestamp
        cur.execute(f"\
            SELECT * \
            FROM submissions \
            WHERE id != {last_submission_id} \
            AND timestamp > (SELECT timestamp FROM submissions WHERE id={last_submission_id}) \
            AND official = true \
            ORDER BY timestamp ASC LIMIT 1")
        current_submission = cur.fetchall()[0]
        # check the participant whom the curent submission belongs to if have submitted another submission for the same task before the current submission
        # if yes return filesystem address for both of them and some other extra info regarding the submissions
        # if not return only the current submission
        cur.execute(f"\
            WITH current_submission AS ( \
                SELECT * \
                FROM submissions \
                WHERE id = {current_submission[0]} \
            )  \
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
        print(fetched_data)
        if fetched_data:
            print("print both of them")
        else:
            print("print only the current submission")
    else:
        # Same for here except since it is the first ever submission being considered only return the current one.
        try:
            cur.execute("\
                SELECT * \
                FROM submissions \
                WHERE official = true \
                ORDER BY timestamp ASC \
                LIMIT 1\
                    ")
            submission = cur.fetchall()[0]
            pickle.dump(submission[0], file)
            json.dumps(
                {
                    'submission_id': submission[0],
                    'participation_id': submission[1],
                    'task_id': submission[2],
                    'timestamp': str(submission[3]),
                    'language': submission[4],
                    'file_path': '/var/ioi/cms/test',
                }
            )
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')
