# Lucario

###### Lucario is an ETL checker that:

  - Checks for diffs between databases
  - Send an alert email

### Testing 

- Test in an ipython notebook
- Set the below environment variables

```sh
  Database credentials:
  db_production:PROD_POSTGRES_DATABASE,
  db_analytics:STG_POSTGRES_DATABASE
  prod_user:PROD_POSTGRES_USER
  analytics_user:STG_POSTGRES_USER
  prod_pass:PROD_POSTGRES_PASSWORD
  analytics_pass:STG_POSTGRES_PASSWORD
  prod_host:PROD_POSTGRES_HOST
  analytics_host:STG_POSTGRES_HOST
  prod_schema:PROD_POSTGRES_SCHEMA
  analytics_schema:STG_POSTGRES_SCHEMA
  prod_port: PROD_POSTGRES_PORT
  analytics_port: STG_POSTGRES_PORT

  lucario_email:
  sender:LUCARIO_EMAIL
  receiver:RECEIVER_EMAIL
  password:LUCARIO_PASS

```
- Run ipython notebook in same folder as python files

```sh
from etlchecker import CheckOperator
from main import EtlCheck
```
- To print out the comparison tables
```sh
dataframe = CheckOperator(credentials)
df = datadrame.compare_df()
df.head()
```
- sample output

|    | table_name                |   x_rows |   y_rows | RowMatch   |   Missing Rows |
|---:|:--------------------------|---------:|---------:|:-----------|---------------:|
|  0 | stg_signups               |    45130 |    45130 | UPDATED    |              0 |
|  1 | src_ke_wards              |    20812 |    20812 | UPDATED    |              0 |
|  2 | stg_agg_farmer_repayments |    67150 |    67150 | UPDATED    |              0 |
|  3 | stg_farmer_loan_details   |    19710 |    19710 | UPDATED    |              0 |
|  4 | stg_sales_call            |   152861 |   152861 | UPDATED    |              0 |

- Running the checker and sending an alert email
```sh
test = EtlCheck(credentials)
test.run()
```

- Results
```sh
Audit table created and dropped...
Audit table created and dropped...
Success,Email sent
```

### Todos

 - Add a threshhold for alerts
 - Add a formatter for stitch created tables
 - Add requirements.txt
 - Add gitlab-ci
 - Create docker image
 - Create python package