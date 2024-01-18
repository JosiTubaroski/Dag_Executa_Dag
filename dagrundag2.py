from airflow import DAG
from airflow.operators.bash import  BashOperator 
from pendulum import DateTime
from datetime import datetime


dag = DAG('dagrundag2', description= "Nossa Dag Run Dag 2", schedule_interval=None,
          start_date=datetime(2024,1,15),catchup=False)


task1 = BashOperator(task_id="tsk1",bash_command="sleep 5", dag=dag)
task2 = BashOperator(task_id="tsk2",bash_command="sleep 5", dag=dag)


# Sequencia da execução utilizando TaskGroup

task1 >>  task2 
