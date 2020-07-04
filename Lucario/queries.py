
def count_function(schema):
    transact_sql = """
        BEGIN;

        CREATE OR REPLACE FUNCTION {}.audit_table_test()
		RETURNS void AS
		$$
		DECLARE
			rec   RECORD;
			crec  RECORD;
		BEGIN
			FOR rec IN SELECT relname FROM pg_stat_user_tables WHERE schemaname='{}' LIMIT 50 LOOP
				FOR crec IN EXECUTE format('SELECT count(*) as rows from staging.%I',rec.relname) LOOP
					-- nothing here, move along
				END LOOP;
				INSERT INTO {}.table_row_count values (rec.relname, crec.rows) ;
			END LOOP;
		RETURN;
		END;
		$$ LANGUAGE 'plpgsql';

        COMMIT;
		""".format(schema,schema,schema)
    return transact_sql


def run_function(schema):
    query = """
    BEGIN;

    SELECT * FROM {}.audit_table_test();
    
    COMMIT;
    """.format(schema)
    return query


def drop_table(schema):
    query = """
    BEGIN;

    DROP TABLE IF EXISTS {}.table_row_count;
    
    COMMIT;
    """.format(schema)
    return query

def create_audit_table(schema):
    query = """
    
    BEGIN;

    CREATE TABLE IF NOT EXISTS  {}.table_row_count(table_name TEXT,row_count INT);
    
    COMMIT;
    """.format(schema)
    return query

def get_audit_table(schema):
    query = """SELECT * FROM {}.table_row_count;""".format(schema)
    return query


