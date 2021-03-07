CMS Database Schema
===================

- [Getting started with Markdown](#getting-started-with-markdown)
- [Titles](#titles)
- [Paragraph](#paragraph)
- [CMS Setup Tables]
	- [Fs Objects Table](#fs-objects-table)
	- [Tokens Table](#tokens-table)

- [People Tables]
	- [Users Table](#users-table)
	- [Admins Table](#admins-table)
	- [Teams Table](#teams-table)
	- [Managers Table](#managers-table)
	    - [User Test Managers Table](#user-test-managers-table)

- [Contest Setup Tables]
    - [Contests Table](#contests-table)
    - [Communication Tables]
        - [Announcements Table](#announcements-table)
        - [Attachements Table](#attachements-table)
        - [Messages Table](#messages-table)
        - [Print Jobs Table](#print-jobs-table)
        - [Files Table](#messages-table)
            - [User Test Files Table](#user-test-files-table)
        - [Participations Table](#participations-table)
    - [Questions Tables]
        - [Datasets Table](#datasets-table)
        - [Questions Table](#questions-table)
        - [Statements Table](#messages-table)
        - [Tasks Table](#tasks-table)
        - [Testcases Table](#testcases-table)
    - [Submission Tables]
        - [Executables Table](#executables-table)
            - [User Test Executables Table](#user-test-executables-table)
        - [Submissions Table](#submissions-table)
        - [Files Table](#messages-table)
    - [Results Tables]
        - [Evaluations Table](#evaluations-table)
        - [Submission Results Table](#submission-results-table)
        - [User Test Results Table](#user-test-results-table)


#Users Table
+---------------------------------------------------------------------------------------------------+
|                                              Table Users                                          |
+---------------------------------------------------------------------------------------------------+
|      Column                   |            Type                          | Nullable               |
|-------------------------------+-------------------------------------------+-----------------------+
| id(auto)                      | integer                                  | not null               |
| first_name                    | character varying                        | not null               |
| last_name                     | character varying                        | not null               |
| username                      | character varying                        | not null               |
| password                      | character varying                        | not null               |
| email                         | character varying                        |                        |
| timezone                      | character varying                        |                        |
| preferred_languages           | character varying[]                      | not null               |
+---------------------------------------------------------------------------------------------------+
+-----------------------+-----------------------------+-----------------------+---------------------+
|    PRIMARY KEY        |        FOREIGN KEY          |    REFERENCES         |     CONSTRAINT      |
+-----------------------|-----------------------------|---------------------------------------------+
| id                    |                             |                       |                     |
+-----------------------|-----------------------------|---------------------------------------------+
|                       |                             |                       |  UNIQUE(username)   |
+---------------------------------------------------------------------------------------------------+
    


#Admins Table
+---------------------------------------------------------------------------------------------------+
|                                              Table Admins                                         |
+---------------------------------------------------------------------------------------------------+
|      Column                   |            Type                          | Nullable               |
|-------------------------------+-------------------------------------------+-----------------------+
| id(auto)                      | integer                                  | not null               |
| name                          | character varying                        | not null               |
| username                      | character varying                        | not null               |
| authentication                | character varying                        | not null               |
| enabled                       | boolean                                  | not null               |
| permission_all                | boolean                                  | not null               |
| permission_messaging          | boolean                                  | not null               |
+-----------------------------------------------------------------------------+---------------------+
+-----------------------+-----------------------------+---------------------------------------------+
|    PRIMARY KEY        |        FOREIGN KEY          |    REFERENCES         |     CONSTRAINT      |
+-----------------------|-----------------------------|---------------------------------------------+
| id                    |                             |                       |                     |
+---------------------------------------------------------------------------------------------------+


#Announcements Table
+---------------------------------------------------------------------------------------------------+
|                                         Table Announcements                                       |
+---------------------------------------------------------------------------------------------------+
|      Column                   |            Type                          | Nullable               |
|-------------------------------+-------------------------------------------+-----------------------+
| id(auto)                      | integer                                  | not null               |
| timestamp                     | timestamp without time zone              | not null               |
| subject                       | character varying                        | not null               |
| text                          | character varying                        | not null               |
| contest_id                    | integer                                  | not null               |
| admin_id                      | integer                                  | not null               |
+---------------------------------------------------------------------------------------------------+
+-----------------------+-----------------------------+-----------------------+---------------------+
|    PRIMARY KEY        |        FOREIGN KEY          |    REFERENCES         |     CONSTRAINT      |
+-----------------------|-----------------------------|---------------------------------------------+
| id                    |                             |                       |                     |
+-----------------------|-----------------------------|---------------------------------------------+
|                       | admin_id                    | admins(id)            | ON UPDATE CASCADE   |
|                       |                             |                       | ON DELETE CASCADE   |
+-----------------------|-----------------------------|---------------------------------------------+
|                       | contest_id                  | contests(id)          | ON UPDATE CASCADE   |
|                       |                             |                       | ON DELETE CASCADE   |
+---------------------------------------------------------------------------------------------------+


#Attachements Table
+----------------------------------------------------------------------------------------------------+
|                                           Table Attachments                                        |
+----------------------------------------------------------------------------------------------------+
|      Column                   |            Type                          | Nullable                |
|-------------------------------+-------------------------------------------+------------------------+
| id(auto)                      | integer                                  | not null                |
| task_id                       | integer                                  | not null                |
| filename                      | character varying                        | not null                |
| digest                        | character varying                        | not null                |
+----------------------------------------------------------------------------------------------------+
+-----------------------+-----------------------------+-------------------+--------------------------+
| PRIMARY KEY           | FOREIGN KEY                 | REFERENCES        | CONSTRAINT               |
+-----------------------|-----------------------------|----------------------------------------------+
| id                    |                             |                   |                          |
+-----------------------|-----------------------------|----------------------------------------------+
|                       |                             |                   | UNIQUE(task_id,filename) |
+-----------------------|-----------------------------|----------------------------------------------+
|                       | task_id                     | tasks(id)         | ON UPDATE CASCADE        |
|                       |                             |                   | ON DELETE CASCADE        |
+----------------------------------------------------------------------------------------------------+


#Contests Table
+----------------------------------------------------------------------------------------------------+
|                                              Table Contests                                        |
+----------------------------------------------------------------------------------------------------+
|      Column                   |            Type                           | Nullable               |
|-------------------------------+-------------------------------------------+------------------------+
| id(auto)                      | integer                                   | not null               |
| name                          | character varying                         | not null               |
| description                   | character varying                         | not null               |
| allowed_localizations         | character varying[]                       | not null               |
| languages                     | character varying[]                       | not null               |
| submissions_download_allowed  | boolean                                   | not null               |
| allow_questions               | boolean                                   | not null               |
| allow_user_tests              | boolean                                   | not null               |
| block_hidden_participations   | boolean                                   | not null               |
| allow_password_authentication | boolean                                   | not null               |
| ip_restriction                | boolean                                   | not null               |
| ip_autologin                  | boolean                                   | not null               |
| token_mode                    | token_mode                                | not null               |
| token_max_number              | integer                                   |                        |
| token_min_interval            | interval                                  | not null               |
| token_gen_initial             | integer                                   | not null               |
| token_gen_number              | integer                                   | not null               |
| token_gen_interval            | interval                                  | not null               |
| token_gen_max                 | integer                                   |                        |
| start                         | timestamp without time zone               | not null               |
| stop                          | timestamp without time zone               | not null               |
| analysis_enabled              | boolean                                   | not null               |
| analysis_start                | timestamp without time zone               | not null               |
| analysis_stop                 | timestamp without time zone               | not null               |
| start                         | timestamp without time zone               | not null               |
| timezone                      | character varying                         |                        |
| per_user_time                 | interval                                  |                        |
| max_submission_number         | integer                                   |                        |
| max_user_test_number          | integer                                   |                        |
| min_submission_interval       | interval                                  |                        |
| min_user_test_interval        | interval                                  |                        |
| score_precision               | integer                                   | not null               |
+----------------------------------------------------------------------------------------------------+
+----------------+---------------------+----------------+--------------------------------------------+
| PRIMARY KEY | FOREIGN KEY | REFERENCES |     CONSTRAINT                                            |
+-------------|-------------|------------------------------------------------------------------------+
| id          |             |            |                                                           |
+-------------|-------------|------------------------------------------------------------------------+
|             |             |            | UNIQUE(name)                                              |
+-------------|-------------|------------------------------------------------------------------------+
|             |             |            | CHECK (start <= stop)                                     |
+-------------|-------------|------------------------------------------------------------------------+
|             |             |            | CHECK (stop <= analysis_start)                            |
+-------------|-------------|------------------------------------------------------------------------+
|             |             |            | CHECK (analysis_start <= analysis_stop)                   |
+-------------|-------------|------------------------------------------------------------------------+
|             |             |            | CHECK (token_gen_initial <= token_gen_max)                |
+-------------|-------------|------------------------------------------------------------------------+
|             |             |            | CHECK (max_submission_number > 0)                         |
+-------------|-------------|------------------------------------------------------------------------+
|             |             |            | CHECK (max_user_test_number > 0)                          | 
+-------------|-------------|------------------------------------------------------------------------+
|             |             |            | CHECK (min_submission_interval > '00:00:00'::interval)    |
+-------------|-------------|------------------------------------------------------------------------+
|             |             |            | CHECK (min_user_test_interval > '00:00:00'::interval)     |
+-------------|-------------|------------------------------------------------------------------------+
|             |             |            | CHECK (per_user_time >= '00:00:00'::interval)             |
+-------------|-------------|------------------------------------------------------------------------+
|             |             |            | CHECK (score_precision >= 0)                              |
+-------------|-------------|------------------------------------------------------------------------+
|             |             |            | CHECK (token_gen_initial >= 0)                            |
+-------------|-------------|------------------------------------------------------------------------+
|             |             |            | CHECK (token_gen_interval > '00:00:00'::interval)         |
+-------------|-------------|------------------------------------------------------------------------+
|             |             |            | CHECK (token_gen_max > 0)                                 |
+-------------|-------------|------------------------------------------------------------------------+
|             |             |            | CHECK (token_gen_number >= 0)                             |
+-------------|-------------|------------------------------------------------------------------------+
|             |             |            | CHECK (token_max_number > 0)                              |
+-------------|-------------|------------------------------------------------------------------------+
|             |             |            | CHECK (token_min_interval >= '00:00:00'::interval)        |
+----------------------------------------------------------------------------------------------------+


#Datasets Table
+----------------------------------------------------------------------------------------------------+
|                                           Table Datasets                                           |
+----------------------------------------------------------------------------------------------------+
|      Column                   |            Type                          | Nullable                |
|-------------------------------+-------------------------------------------+------------------------+
| id(auto)                      | integer                                  | not null                |
| task_id                       | integer                                  | not null                |
| description                   | character varying                        | not null                |
| autojudge                     | boolean                                  | not null                |
| time_limit                    | double precision                         |                         |
| memory_limit                  | bigint                                   |                         |
| task_type                     | character varying                        | not null                |
| task_type_parameters          | jsonb                                    | not null                |
| score_type                    | character varying                        | not null                |
| score_type_parameters         | jsonb                                    | not null                |
+----------------------------------------------------------------------------------------------------+
+------------------ +---------------------+---------------+------------------------------------------+
|    PRIMARY KEY    |     FOREIGN KEY     |   REFERENCES  |     CONSTRAINT                           |
+-------------------|---------------------|---------------|------------------------------------------+
| id                |                     |               |                                          |
+-------------------|---------------------|---------------|------------------------------------------+
|                   |                     |               | UNIQUE(id, task_id)                      |
+-------------------|---------------------|---------------|------------------------------------------+
|                   |                     |               | UNIQUE(task_id, description)             |
+-------------------|---------------------|---------------|------------------------------------------+
|                   |                     |               | CHECK (memory_limit > 0)                 |
+-------------------|---------------------|---------------|------------------------------------------+
|                   |                     |               | CHECK (time_limit > 0::double precision) |
+-------------------|---------------------|---------------|------------------------------------------+
|                   | task_id             | tasks(id)     | ON UPDATE CASCADE                        |
|                   |                     |               | ON DELETE CASCADE                        |
+----------------------------------------------------------------------------------------------------+


#Evaluations Table
+----------------------------------------------------------------------------------------------------+
|                                           Table Evaluations                                        |
+----------------------------------------------------------------------------------------------------+
|      Column                   |            Type                          | Nullable                |
|-------------------------------+-------------------------------------------+------------------------+
| id(auto)                      | integer                                  | not null                |
| submission_id                 | integer                                  | not null                |
| dataset_id                    | integer                                  | not null                |
| testcase_id                   | integer                                  | not null                |
| outcome                       | character varying                        |                         |
| text                          | character varying[]                      | not null                |
| autojudge                     | boolean                                  | not null                |
| execution_time                | double precision                         |                         |
| execution_wall_clock_time     | double precision                         |                         |
| execution_memory              | bigint                                   |                         |
| evaluation_shard              | integer                                  |                         |
| evaluation_sandbox            | character varying                        |                         |
+----------------------------------------------------------------------------------------------------+
+------------+-----------------+---------------------+-----------------------------------------------+
| PRIMARY KEY|   FOREIGN KEY   |    REFERENCES       |     CONSTRAINT                                |
+------------|-----------------|---------------------------------------------------------------------+
| id         |                 |                     |                                               |
+------------|-----------------|---------------------------------------------------------------------+
|            |                 |                     | UNIQUE(submission_id, dataset_id, testcase_id)|
+------------|-----------------|---------------------------------------------------------------------+
|            |                 |                     | UNIQUE(task_id, description)                  |
+------------|-----------------|---------------------------------------------------------------------+
|            |                 |                     | CHECK (memory_limit > 0)                      |
+------------|-----------------|---------------------------------------------------------------------+
|            |                 |                     | CHECK (time_limit > 0::double precision)      |
+------------|-----------------|---------------------------------------------------------------------+
|            | dataset_id      | datasets(id)        | ON UPDATE CASCADE                             |
|            |                 |                     | ON DELETE CASCADE                             |
+------------|-----------------|---------------------------------------------------------------------+
|            | (submission_id, | submission_results( | ON UPDATE CASCADE                             |
|            |  dataset_id)    |    submission_id,   | ON DELETE CASCADE                             |
|            |                 |    dataset_id       |                                               |
|            |                 | )                   |                                               |
+------------|-----------------|---------------------------------------------------------------------+
|            | submission_id   | submissions(id)     | ON UPDATE CASCADE                             |
|            |                 |                     | ON DELETE CASCADE                             |
+------------|-----------------|---------------------------------------------------------------------+
|            | testcase_id     | testcases(id)       | ON UPDATE CASCADE                             |
|            |                 |                     | ON DELETE CASCADE                             |
+----------------------------------------------------------------------------------------------------+



#Executables Table
+----------------------------------------------------------------------------------------------------+
|                                           Table Executables                                        |
+----------------------------------------------------------------------------------------------------+
|      Column                   |            Type                          | Nullable                |
|-------------------------------+-------------------------------------------+------------------------+
| id(auto)                      | integer                                  | not null                |
| submission_id                 | integer                                  | not null                |
| dataset_id                    | integer                                  | not null                |
| filename                      | character varying                        | not null                |
| digest                        | character varying                        | not null                |
+----------------------------------------------------------------------------------------------------+
+-------------+-----------------------------+-----------------------+--------------------------------+
| PRIMARY KEY | FOREIGN KEY       | REFERENCES          | CONSTRAINT                                 |
+-------------|-------------------|------------------------------------------------------------------+
| id          |                   |                     |                                            |
+-------------|-------------------|------------------------------------------------------------------+
|             |                   |                     | UNIQUE(submission_id, dataset_id, filename)|
+-------------|-------------------|------------------------------------------------------------------+
|             | dataset_id        | datasets(id)        | ON UPDATE CASCADE                          |
|             |                   |                     | ON DELETE CASCADE                          |
+-------------|-------------------|------------------------------------------------------------------+
|             | (submission_id,   | submission_results( | ON UPDATE CASCADE                          |
|             |  dataset_id)      |    submission_id,   | ON DELETE CASCADE                          |
|             |                   |    dataset_id)      |                                            |
|             |  dataset_id)      | )                   |                                            |
+-------------|-------------------|------------------------------------------------------------------+
|             | submission_id     | submissions(id)     | ON UPDATE CASCADE                          |
|             |                   |                     | ON DELETE CASCADE                          |
+----------------------------------------------------------------------------------------------------+


#Files Table
+----------------------------------------------------------------------------------------------------+
|                                           Table Files                                              |
+----------------------------------------------------------------------------------------------------+
|      Column                   |            Type                          | Nullable                |
|-------------------------------+-------------------------------------------+------------------------+
| id(auto)                      | integer                                  | not null                |
| submission_id                 | integer                                  | not null                |
| filename                      | character varying                        | not null                |
| digest                        | character varying                        | not null                |
+----------------------------------------------------------------------------------------------------+
+--------------------+------------------------+--------------------+---------------------------------+
| PRIMARY KEY        | FOREIGN KEY            | REFERENCES         | CONSTRAINT                      |
+--------------------|------------------------|------------------------------------------------------+
| id                 |                        |                    |                                 |
+--------------------|------------------------|------------------------------------------------------+
|                    |                        |                    | UNIQUE(submission_id, filename) |
+--------------------|------------------------|------------------------------------------------------+
|                    | submission_id          | submissions(id)    | ON UPDATE CASCADE               |
|                    |                        |                    | ON DELETE CASCADE               |
+----------------------------------------------------------------------------------------------------+


#Fs Objects
+----------------------------------------------------------------------------------------------------+
|                                           Table Fsobjects                                          |
+----------------------------------------------------------------------------------------------------+
|      Column                   |            Type                          | Nullable                |
|-------------------------------+------------------------------------------+-------------------------+
| digest                        | character varying                        | not null                |
| loid                          | loid                                     | not null                |
| description                   | character varying                        | not null                |
+----------------------------------------------------------------------------------------------------+
+-----------------------+-----------------------------+-----------------------+----------------------+
| PRIMARY KEY           | FOREIGN KEY                 | REFERENCES            | CONSTRAINT           |
+-----------------------|-----------------------------|----------------------------------------------+
| digest                |                             |                       |                      |
+----------------------------------------------------------------------------------------------------+


#Managers Table
+----------------------------------------------------------------------------------------------------+
|                                           Table Managers                                           |
+----------------------------------------------------------------------------------------------------+
|      Column                   |            Type                          | Nullable                |
|-------------------------------+-------------------------------------------+------------------------+
| id(auto)                      | integer                                  | not null                |
| dataset_id                    | integer                                  | not null                |
| filename                      | character varying                        | not null                |
| digest                        | character varying                        | not null                |
+----------------------------------------------------------------------------------------------------+
+---------------------+------------------------+-----------------------+-----------------------------+
| PRIMARY KEY         | FOREIGN KEY            | REFERENCES            | CONSTRAINT                  |
+---------------------|------------------------|-----------------------------------------------------+
| id                  |                        |                       |                             |
+---------------------|------------------------|-----------------------------------------------------+
|                     |                        |                       | UNIQUE(dataset_id, filename)|
+---------------------|------------------------|-----------------------------------------------------+
|                     | dataset_id             | datasets(id)          | ON UPDATE CASCADE           |
|                     |                        |                       | ON DELETE CASCADE           |
+----------------------------------------------------------------------------------------------------+



#Messages Table
+----------------------------------------------------------------------------------------------------+
|                                           Table Messages                                           |
+----------------------------------------------------------------------------------------------------+
|      Column                   |            Type                          | Nullable                |
|-------------------------------+-------------------------------------------+------------------------+
| id(auto)                      | integer                                  | not null                |
| timestamp                     | timestamp without time zone              | not null                |
| subject                       | character varying                        | not null                |
| text                          | character varying                        | not null                |
| participation_id              | integer                                  | not null                |
| admin_id                      | integer                                  |                         |
+----------------------------------------------------------------------------------------------------+
+-----------------------+-----------------------------+-----------------------+----------------------+
| PRIMARY KEY           | FOREIGN KEY                 | REFERENCES            | CONSTRAINT           |
+-----------------------|-----------------------------|----------------------------------------------+
| id                    |                             |                       |                      |
+-----------------------|-----------------------------|----------------------------------------------+
|                       | admin_id                    | admins(id)            | ON UPDATE CASCADE    |
|                       |                             |                       | ON DELETE CASCADE    |
+-----------------------|-----------------------------|----------------------------------------------+
|                       | participation_id            | participations(id)    | ON UPDATE CASCADE    |
|                       |                             |                       | ON DELETE CASCADE    |
+----------------------------------------------------------------------------------------------------+




#Participations Table
+-----------------------------------------------------------------------------------------------------+
|                                           Table Participations                                      |
+-----------------------------------------------------------------------------------------------------+
|      Column                   |            Type                          | Nullable                 |
|-------------------------------+-------------------------------------------+-------------------------+
| id(auto)                      | integer                                  | not null                 |
| ip                            | cidr[]                                   |                          |
| starting_time                 | timestamp without time zone              |                          |
| delay_time                    | interval                                 | not null                 |
| extra_time                    | interval                                 | not null                 |
| password                      | character varying                        |                          |
| hidden                        | boolean                                  | not null                 |
| unrestricted                  | boolean                                  | not null                 |
| contest_id                    | integer                                  | not null                 |
| user_id                       | integer                                  | not null                 |
| team_id                       | integer                                  |                          |
+-----------------------------------------------------------------------------------------------------+
+--------------+-------------------+---------------------+--------------------------------------------+
| PRIMARY KEY  | FOREIGN KEY       | REFERENCES          | CONSTRAINT                                 |
+--------------|-------------------|------------------------------------------------------------------+
| id           |                   |                     |                                            |
+--------------|-------------------|------------------------------------------------------------------+
|              |                   |                     | UNIQUE(contest_id, user_id)                |
+--------------|-------------------|------------------------------------------------------------------+
|              |                   |                     | CHECK (delay_time >= '00:00:00'::interval) |
+--------------|-------------------|------------------------------------------------------------------+
|              |                   |                     | CHECK (extra_time >= '00:00:00'::interval) |
+--------------|-------------------|------------------------------------------------------------------+
|              | contest_id        | contest(id)         | ON UPDATE CASCADE                          |
|              |                   |                     | ON DELETE CASCADE                          |
+--------------|-------------------|------------------------------------------------------------------+
|              | team_id           | teams(id)           | ON UPDATE CASCADE                          |
|              |                   |                     | ON DELETE CASCADE                          |
+--------------|-------------------|------------------------------------------------------------------+
|              | user_id           | users(id)           | ON UPDATE CASCADE                          |
|              |                   |                     | ON DELETE CASCADE                          |
+-----------------------------------------------------------------------------------------------------+


#Print Jobs Table
+-----------------------------------------------------------------------------------------------------+
|                                           Table Printjobs                                           |
+-----------------------------------------------------------------------------------------------------+
|      Column                   |            Type                          | Nullable                 |
|-------------------------------+-------------------------------------------+-------------------------+
| id(auto)                      | integer                                  | not null                 |
| participation_id              | integer                                  | not null                 |
| timestamp                     | timestamp without time zone              | not null                 |
| filename                      | character varying                        | not null                 |
| digest                        | character varying                        | not null                 |
| done                          | boolean                                  | not null                 |
| status                        | character varying[]                      | not null                 |
+-----------------------------------------------------------------------------------------------------+
+-----------------------+-------------------------+---------------------+-----------------------------+
| PRIMARY KEY           | FOREIGN KEY             | REFERENCES          | CONSTRAINT                  |
+-----------------------|-------------------------|---------------------------------------------------+
| id                    |                         |                     |                             |
+-----------------------|-------------------------|---------------------------------------------------+
|                       |                         |                     | UNIQUE(task_id, filename)   |
+-----------------------|-------------------------|---------------------------------------------------+
|                       | participation_id        | participations(id)  | ON UPDATE CASCADE           |
|                       |                         |                     | ON DELETE CASCADE           |
+-----------------------------------------------------------------------------------------------------+




#Questions Table
+-----------------------------------------------------------------------------------------------------+
|                                           Table Questions                                           |
+-----------------------------------------------------------------------------------------------------+
|      Column                   |            Type                          | Nullable                 |
|-------------------------------+-------------------------------------------+-------------------------+
| id(auto)                      | integer                                  | not null                 |
| question_timestamp            | timestamp without time zone              | not null                 |
| subject                       | character varying                        | not null                 |
| text                          | character varying                        | not null                 |
| reply_timestamp               | timestamp without time zone              |                          |
| ignored                       | boolean                                  | not null                 |
| reply_subject                 | character varying                        |                          |
| reply_text                    | character varying                        |                          |
| participation_id              | integer                                  | not null                 |
| admin_id                      | integer                                  |                          |
+-----------------------------------------------------------------------------------------------------+
+-----------------------+-----------------------+-----------------------+-----------------------------+
| PRIMARY KEY           | FOREIGN KEY           | REFERENCES            | CONSTRAINT                  |
+-----------------------|-----------------------|-----------------------------------------------------+
| id                    |                       |                       |                             |
+-----------------------|-----------------------|-----------------------------------------------------+
|                       |                       |                       | UNIQUE(task_id, filename)   |
+-----------------------|-----------------------|-----------------------------------------------------+
|                       | admin_id              | admins(id)            | ON UPDATE CASCADE           |
|                       |                       |                       | ON DELETE CASCADE           |
+-----------------------|-----------------------|-----------------------------------------------------+
|                       | participation_id      | participations(id)    | ON UPDATE CASCADE           |
|                       |                       |                       | ON DELETE CASCADE           |
+-----------------------------------------------------------------------------------------------------+




#Statements Table
+-----------------------------------------------------------------------------------------------------+
|                                           Table Statements                                          |
+-----------------------------------------------------------------------------------------------------+
|      Column                   |            Type                          | Nullable                 |
|-------------------------------+-------------------------------------------+-------------------------+
| id(auto)                      | integer                                  | not null                 |
| task_id                       | integer                                  | not null                 |
| language                      | character varying                        | not null                 |
| digest                        | character varying                        | not null                 |
+-----------------------------------------------------------------------------------------------------+
+-----------------------+-----------------------------+------------------+----------------------------+
| PRIMARY KEY           | FOREIGN KEY                 | REFERENCES       | CONSTRAINT                 |
+-----------------------|-----------------------------|-----------------------------------------------+
| id                    |                             |                  |                            |
+-----------------------|-----------------------------|-----------------------------------------------+
|                       |                             |                  | UNIQUE(task_id, language)  |
+-----------------------|-----------------------------|-----------------------------------------------+
|                       | task_id                     | tasks(id)        | ON UPDATE CASCADE          |
|                       |                             |                  | ON DELETE CASCADE          |
+-----------------------------------------------------------------------------------------------------+

#Submission Results Table
+-----------------------------------------------------------------------------------------------------+
|                                           Table Submission Results                                  |
+-----------------------------------------------------------------------------------------------------+
|      Column                   |            Type                          | Nullable                 |
|-------------------------------+-------------------------------------------+-------------------------+
| submission_id                 | integer                                  | not null                 |
| dataset_id                    | integer                                  | not null                 |
| compilation_outcome           | compilation_outcome                      |                          |
| compilation_text              | character varying[]                      | not null                 |
| compilation_tries             | integer                                  | not null                 |
| compilation_stdout            | character varying                        |                          |
| compilation_stderr            | character varying                        |                          |
| compilation_time              | double precision                         |                          |
| compilation_wall_clock_time   | double precision                         |                          |
| compilation_memory            | bigint                                   |                          |
| compilation_shard             | integer                                  |                          |
| compilation_sandbox           | character varying                        |                          |
| evaluation_outcome            | evaluation_outcome                       |                          |
| evaluation_tries              | integer                                  | not null                 |
| score                         | double precision                         |                          |
| score_details                 | jsonb                                    |                          |
| public_score                  | double precision                         |                          |
| public_score_details          | jsonb                                    |                          |
| ranking_score_details         | character varying[]                      |                          |
+-----------------------------------------------------------------------------------------------------+
+-----------------------------+-----------------------------+--------------------+--------------------+
| PRIMARY KEY                 | FOREIGN KEY                    | REFERENCES         | CONSTRAINT      |
+-----------------------------|-----------------------------|-----------------------------------------+
| (submission_id, dataset_id) |                             |                    |                    |
+-----------------------------|-----------------------------|-----------------------------------------+
|                             | dataset_id                  | datasets(id)       | ON UPDATE CASCADE  |
|                             |                             |                    | ON DELETE CASCADE  |
+-----------------------------|-----------------------------|-----------------------------------------+
|                             | submission_id               | submissions(id)    | ON UPDATE CASCADE  |
|                             |                             |                    | ON DELETE CASCADE  |
+-----------------------------------------------------------------------------------------------------+


#Submissions Table
+-----------------------------------------------------------------------------------------------------+
|                                           Table Submissions                                         |
+-----------------------------------------------------------------------------------------------------+
|      Column                   |            Type                          | Nullable                 |
|-------------------------------+-------------------------------------------+-------------------------+
| id(auto)                      | integer                                  | not null                 |
| task_id                       | integer                                  | not null                 |
| participation_id              | integer                                  | not null                 |
| timestamp                     | timestamp without time zone              | not null                 |
| language                      | character varying                        |                          |
| comment                       | character varying                        | not null                 |
| official                      | boolean                                  | not null                 |
+-----------------------------------------------------------------------------------------------------+
+-----------------------+-----------------------+-----------------------+-----------------------------+
| PRIMARY KEY           | FOREIGN KEY           | REFERENCES            | CONSTRAINT                  |
+-----------------------|-----------------------|-----------------------------------------------------+
| id                    |                       |                       |                             |
+-----------------------|-----------------------|-----------------------------------------------------+
|                       |                       |                       | UNIQUE(task_id, filename)   |
+-----------------------|-----------------------|-----------------------------------------------------+
|                       | task_id               | tasks(id)             | ON UPDATE CASCADE           |
|                       |                       |                       | ON DELETE CASCADE           |
+-----------------------|-----------------------|-----------------------------------------------------+
|                       | participation_id      | participations(id)    | ON UPDATE CASCADE           |
|                       |                       |                       | ON DELETE CASCADE           |
+-----------------------------------------------------------------------------------------------------+


#Tasks Table
+-----------------------------------------------------------------------------------------------------+
|                                              Table Tasks                                            |
+-----------------------------------------------------------------------------------------------------+
|      Column                   |            Type                           | Nullable                |
|-------------------------------+-------------------------------------------+-------------------------+
| id(auto)                      | integer                                   | not null                |
| num                           | integer                                   |                         |
| contest_id                    | integer                                   |                         |
| name                          | character varying                         | not null                |
| title                         | character varying                         | not null                |
| submission_format             | character varying[]                       | not null                |
| primary_statements            | character varying[]                       | not null                |
| token_mode                    | token_mode                                | not null                |
| token_max_number              | integer                                   |                         |
| token_min_interval            | interval                                  | not null                |
| token_gen_initial             | integer                                   | not null                |
| token_gen_number              | integer                                   | not null                |
| token_gen_interval            | interval                                  | not null                |
| token_gen_max                 | integer                                   |                         |
| max_submission_number         | integer                                   |                         |
| max_user_test_number          | integer                                   |                         |
| min_submission_interval       | interval                                  |                         |
| min_user_test_interval        | interval                                  |                         |
| feedback_level                | feedback_level                            | not null                |
| score_precision               | integer                                   | not null                |
| score_mode                    | score_mode                                | not null                |
| active_dataset_id             | integer                                   |                         |
+-----------------------------------------------------------------------------------------------------+
+-----------------------+----------------------+--------------+---------------------------------------+
| PRIMARY KEY  | FOREIGN KEY          | REFERENCES   | CONSTRAINT                                     |
+--------------|----------------------|---------------------------------------------------------------+
| id           |                      |              |                                                |
+--------------|----------------------|---------------------------------------------------------------+
|              |                      |              | UNIQUE(name)                                   |
+--------------|----------------------|---------------------------------------------------------------+
|              |                      |              | UNIQUE(contest_id, num)                        |
+--------------|----------------------|---------------------------------------------------------------+
|              |                      |              | UNIQUE(contest_id, name)                       |
+--------------|----------------------|---------------------------------------------------------------+
|              |                      |              | CHECK (token_gen_initial <= token_gen_max)     |
+--------------|----------------------|---------------------------------------------------------------+
|              |                      |              | CHECK (max_submission_number > 0)              |
+--------------|----------------------|---------------------------------------------------------------+
|              |                      |              | CHECK (max_user_test_number > 0)               | 
+--------------|----------------------|---------------------------------------------------------------+
|              |                      |              | CHECK (min_submission_interval > '00:00:00')   |
+--------------|----------------------|---------------------------------------------------------------+
|              |                      |              | CHECK (min_user_test_interval > '00:00:00')    |
+--------------|----------------------|---------------------------------------------------------------+
|              |                      |              | CHECK (per_user_time >= '00:00:00')            |
+--------------|----------------------|---------------------------------------------------------------+
|              |                      |              | CHECK (score_precision >= 0)                   |
+--------------|----------------------|---------------------------------------------------------------+
|              |                      |              | CHECK (token_gen_initial >= 0)                 |
+--------------|----------------------|---------------------------------------------------------------+
|              |                      |              | CHECK (token_gen_interval > '00:00:00')        |
+--------------|----------------------|---------------------------------------------------------------+
|              |                      |              | CHECK (token_gen_max > 0)                      |
+--------------|----------------------|---------------------------------------------------------------+
|              |                      |              | CHECK (token_gen_number >= 0)                  |
+--------------|----------------------|---------------------------------------------------------------+
|              |                      |              | CHECK (token_max_number > 0)                   |
+--------------|----------------------|---------------------------------------------------------------+
|              | (id,                 | datasets(    | ON UPDATE CASCADE                              |
|              |  active_dataset_id)  |    task_id,  | ON DELETE CASCADE                              |
|              |                      |    id        |                                                |
|              |                      | )            |                                                |
+--------------|----------------------|---------------------------------------------------------------+
|              | contest_id           | contests(id) | ON UPDATE CASCADE                              |
|              |                      |              | ON DELETE CASCADE                              |
+-----------------------------------------------------------------------------------------------------+


#Teams Table
+-----------------------------------------------------------------------------------------------------+
|                                           Table Teams                                               |
+-----------------------------------------------------------------------------------------------------+
|      Column                   |            Type                          | Nullable                 |
|-------------------------------+-------------------------------------------+-------------------------+
| id(auto)                      | integer                                  | not null                 |
| code                          | character varying                        | not null                 |
| name                          | character varying                        | not null                 |
+-----------------------------------------------------------------------------------------------------+
+-----------------------+-----------------------------+-----------------------+-----------------------+
| PRIMARY KEY           | FOREIGN KEY                 | REFERENCES            | CONSTRAINT            |
+-----------------------|-----------------------------|-----------------------------------------------+
| id                    |                             |                       |                       |
+-----------------------|-----------------------------|-----------------------------------------------+
|                       |                             |                       | UNIQUE(code)          |
+-----------------------------------------------------------------------------------------------------+


#Testcases Table
+-----------------------------------------------------------------------------------------------------+
|                                           Table Testcases                                           |
+-----------------------------------------------------------------------------------------------------+
|      Column                   |            Type                          | Nullable                 |
|-------------------------------+-------------------------------------------+-------------------------+
| id(auto)                      | integer                                  | not null                 |
| dataset_id                    | integer                                  | not null                 |
| codename                      | character varying                        | not null                 |
| public                        | boolean                                  | not null                 |
| input                         | character varying                        | not null                 |
| onput                         | character varying                        | not null                 |
+-----------------------------------------------------------------------------------------------------+
+-----------------------+-----------------------+-----------------------+-----------------------------+
| PRIMARY KEY           | FOREIGN KEY           | REFERENCES            | CONSTRAINT                  |
+-----------------------|-----------------------|-----------------------------------------------------+
| id                    |                       |                       |                             |
+-----------------------|-----------------------|-----------------------------------------------------+
|                       |                       |                       | UNIQUE(dataset_id, codename)|
+-----------------------|-----------------------|-----------------------------------------------------+
|                       | dataset_id            | datasets(id)          | ON UPDATE CASCADE           |
|                       |                       |                       | ON DELETE CASCADE           |
+-----------------------------------------------------------------------------------------------------+


#Tokens Table
+-----------------------------------------------------------------------------------------------------+
|                                           Table Tokens                                              |
+-----------------------------------------------------------------------------------------------------+
|      Column                   |            Type                          | Nullable                 |
|-------------------------------+-------------------------------------------+-------------------------+
| id(auto)                      | integer                                  | not null                 |
| submission_id                 | integer                                  | not null                 |
| timestamp                     | timestamp without time zone              | not null                 |
+-----------------------------------------------------------------------------------------------------+
+-----------------------+-----------------------------+-----------------------+-----------------------+
| PRIMARY KEY           | FOREIGN KEY                 | REFERENCES            | CONSTRAINT            |
+-----------------------|-----------------------------|-----------------------------------------------+
| id                    |                             |                       |                       |
+-----------------------|-----------------------------|-----------------------------------------------+
|                       |                             |                       | UNIQUE(submission_id) |
+-----------------------|-----------------------------|-----------------------------------------------+
|                       | submission_id               | submissions(id)       | ON UPDATE CASCADE     |
|                       |                             |                       | ON DELETE CASCADE     |
+-----------------------------------------------------------------------------------------------------+



#Executable Table
+-----------------------------------------------------------------------------------------------------+
|                                           Table User Test Executables                               |
+-----------------------------------------------------------------------------------------------------+
|      Column                   |            Type                          | Nullable                 |
|-------------------------------+-------------------------------------------+-------------------------+
| id(auto)                      | integer                                  | not null                 |
| user_test_id                  | integer                                  | not null                 |
| dataset_id                    | integer                                  | not null                 |
| filename                      | character varying                        | not null                 |
| digest                        | character varying                        | not null                 |
+-----------------------------------------------------------------------------------------------------+
+---------------+-----------------+--------------------+----------------------------------------------+
| PRIMARY KEY   | FOREIGN KEY     | REFERENCES         | CONSTRAINT                                   |
+---------------|-----------------|-------------------------------------------------------------------+
| id            |                 |                    |                                              |
+---------------|-----------------|-------------------------------------------------------------------+
|               |                 |                    | UNIQUE(user_test_id, dataset_id, filename)   |
+---------------|-----------------|-------------------------------------------------------------------+
|               | dataset_id      | datasets(id)       | ON UPDATE CASCADE                            |
|               |                 |                    | ON DELETE CASCADE                            |
+---------------|-----------------|-------------------------------------------------------------------+
|               | (user_test_id,  | user_test_results( | ON UPDATE CASCADE                            |
|               |  dataset_id)    |    user_test_id,   | ON DELETE CASCADE                            |
|               |                 |     dataset_id     |                                              |
|               |                 | )                  |                                              |
+---------------|-----------------|-------------------------------------------------------------------+
|               | user_test_id    | user_tests(id)     | ON UPDATE CASCADE                            |
|               |                 |                    | ON DELETE CASCADE                            |
+-----------------------------------------------------------------------------------------------------+



#User Test Files Table
+-----------------------------------------------------------------------------------------------------+
|                                           Table User Test Files                                     |
+-----------------------------------------------------------------------------------------------------+
|      Column                   |            Type                          | Nullable                 |
|-------------------------------+-------------------------------------------+-------------------------+
| id(auto)                      | integer                                  | not null                 |
| user_test_id                  | integer                                  | not null                 |
| filename                      | character varying                        | not null                 |
| digest                        | character varying                        | not null                 |
+-----------------------------------------------------------------------------------------------------+
+-----------------+-----------------------------+---------------------+-------------------------------+
| PRIMARY KEY     | FOREIGN KEY                 | REFERENCES          | CONSTRAINT                    |
+-----------------|-----------------------------|-----------------------------------------------------+
| id              |                             |                     |                               |
+-----------------|-----------------------------|-----------------------------------------------------+
|                 |                             |                     | UNIQUE(user_test_id, filename)|
+-----------------|-----------------------------|-----------------------------------------------------+
|                 | user_test_id                | user_tests(id)      | ON UPDATE CASCADE             |
|                 |                             |                     | ON DELETE CASCADE             |
+-----------------------------------------------------------------------------------------------------+



#User Test Managers Table
+-----------------------------------------------------------------------------------------------------+
|                                           Table User Test Managers                                  |
+-----------------------------------------------------------------------------------------------------+
|      Column                   |            Type                          | Nullable                 |
|-------------------------------+-------------------------------------------+-------------------------+
| id(auto)                      | integer                                  | not null                 |
| user_test_id                  | integer                                  | not null                 |
| filename                      | character varying                        | not null                 |
| digest                        | character varying                        | not null                 |
+-----------------------------------------------------------------------------------------------------+
+-----------------------+--------------------+-----------------------+--------------------------------+
| PRIMARY KEY           | FOREIGN KEY        | REFERENCES            | CONSTRAINT                     |
+-----------------------|--------------------|--------------------------------------------------------+
| id                    |                    |                       |                                |
+-----------------------|--------------------|--------------------------------------------------------+
|                       |                    |                       | UNIQUE(user_test_id, filename) |
+-----------------------|--------------------|--------------------------------------------------------+
|                       | user_test_id       | user_tests(id)        | ON UPDATE CASCADE              |
|                       |                    |                       | ON DELETE CASCADE              |
+-----------------------------------------------------------------------------------------------------+



#User Test Results Table
+-----------------------------------------------------------------------------------------------------+
|                                           Table User Test Results                                   |
+-----------------------------------------------------------------------------------------------------+
|      Column                   |            Type                          | Nullable                 |
|-------------------------------+-------------------------------------------+-------------------------+
| user_test_id                  | integer                                  | not null                 |
| dataset_id                    | integer                                  | not null                 |
| output                        | character varying                        |                          |
| compilation_outcome           | character varying                        |                          |
| compilation_text              | character varying[]                      | not null                 |
| compilation_tries             | integer                                  | not null                 |
| compilation_stdout            | character varying                        |                          |
| compilation_stderr            | character varying                        |                          |
| compilation_time              | double precision                         |                          |
| compilation_wall_clock_time   | double precision                         |                          |
| compilation_memory            | bigint                                   |                          |
| compilation_shard             | integer                                  |                          |
| compilation_sandbox           | character varying                        |                          |
| evaluation_outcome            | character varying                        |                          |
| evaluation_text               | character varying                        | not null                 |
| evaluation_tries              | integer                                  | not null                 |
| execution_time                | double precision                         |                          |
| execution_wall_clock_time     | double precision                         |                          |
| execution_memory              | bigint                                   |                          |
| execution_shard               | integer                                  |                          |
| execution_sandbox             | character varying                        |                          |
+-----------------------------------------------------------------------------------------------------+
+-----------------------------+--------------------------+--------------------+-----------------------+
| PRIMARY KEY                 | FOREIGN KEY              | REFERENCES         | CONSTRAINT            |
+-----------------------------|--------------------------|--------------------------------------------+
| (user_test_id, dataset_id)  |                          |                    |                       |
+-----------------------------|--------------------------|--------------------------------------------+
|                             | dataset_id               | datasets(id)       | ON UPDATE CASCADE     |
|                             |                          |                    | ON DELETE CASCADE     |
+-----------------------------|--------------------------|--------------------------------------------+
|                             | user_test_id             | user_tests(id)     | ON UPDATE CASCADE     |
|                             |                          |                    | ON DELETE CASCADE     |
+-----------------------------------------------------------------------------------------------------+




#User Tests Table
+-----------------------------------------------------------------------------------------------------+
|                                           Table User Tests                                          |
+-----------------------------------------------------------------------------------------------------+
|      Column                   |            Type                          | Nullable                 |
|-------------------------------+-------------------------------------------+-------------------------+
| id(auto)                      | integer                                  | not null                 |
| task_id                       | integer                                  | not null                 |
| participation_id              | integer                                  | not null                 |
| timestamp                     | timestamp without time zone              | not null                 |
| language                      | character varying                        |                          |
| input                         | character varying                        | not null                 |
+-----------------------------------------------------------------------------------------------------+
+-----------------------+-----------------------------+-----------------------+-----------------------+
| PRIMARY KEY           | FOREIGN KEY                 | REFERENCES            | CONSTRAINT            |
+-----------------------|-----------------------------|-----------------------------------------------+
| id                    |                             |                       |                       |
+-----------------------|-----------------------------|-----------------------------------------------+
|                       | task_id                     | tasks(id)             | ON UPDATE CASCADE     |
|                       |                             |                       | ON DELETE CASCADE     |
+-----------------------|-----------------------------|-----------------------------------------------+
|                       | participation_id            | participations(id)    | ON UPDATE CASCADE     |
|                       |                             |                       | ON DELETE CASCADE     |
+-----------------------------------------------------------------------------------------------------+