from airflow.models.dag import DAG
import pendulum
import datetime

with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
  
  # [START howto_operator_bash]
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    )

    bash_t2= BashOperator(
    task_id="bash_t2",
    bash_command="echo $HOSTNAME",
    )

    # [END howto_operator_bash]

    # [END howto_operator_bash_template]
    bash_t1 >> bash_t2