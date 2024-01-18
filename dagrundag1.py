from airflow import DAG
from airflow.operators.bash import  BashOperator 
from pendulum import DateTime
from datetime import datetime
from airflow.operators.trigger_dagrun import TriggerDagRunOperator


dag = DAG('dagrundag1', description= "Nossa Dag Run Dag 1", schedule_interval=None,
          start_date=datetime(2024,1,15),catchup=False)


task1 = BashOperator(task_id="tsk1",bash_command="sleep 5", dag=dag)
task2 = TriggerDagRunOperator(task_id="tsk2",trigger_dag_id="dagrundag2", dag=dag)


# Sequencia da execução utilizando TaskGroup

task1 >>  task2 