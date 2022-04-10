# import pandas as pd
# from matplotlib import pyplot as plt
from airflow import DAG
from airflow.providers.papermill.operators.papermill import PapermillOperator
# from airflow.operators.python_operator import PythonOperator

# def print_firstdag():
#     return 'My First DAG from HevoData!'
#
# dag = DAG('first_dag', description='HevoData Dag',
#           schedule_interval='0 8 * * *',
#           start_date=datetime(2022, 2, 24), catchup=False)
#
# print_operator = PythonOperator(task_id='first_task', python_callable=print_firstdag, dag=dag)
#
# print_operator
dag = DAG('Game_Sales', description='Read video game csv', schedule_interval='None')

notebook_task = PapermillOperator(
        task_id="run_notebook",
        input_nb="/Users/joe/dev/AirflowWeekend/airflow-proj-files/PS4_Game_Sales.ipynb",
        output_nb="/Users/joe/dev/AirflowWeekend/airflow-proj-files/out-{Top_10_PS4_Games_Sold}.ipynb",
    )
# def read_csv():
#     data = pd.read_csv('/Users/joe/dev/AirflowWeekend/airflow-proj-files/dags/PS4_GamesSales.csv')
#     return data
#
# def transform_data():
#     data2 = read_csv().dropna()
#     data2.drop(['North America', 'Europe', 'Japan', 'Rest of World'], axis=1, inplace=True)
#     data2 = data2.astype({'Year': 'int64'})
#     data2 = data2[data2 != 0].dropna()
#     data2.reset_index(drop=True, inplace=True)
#     return data2
#
# def top_10_games():
#     return transform_data().head(10)
#
# # def graph_top_games():
# #     plt.xticks(rotation=90)
# #     plt.ylabel('Sales (in millions)')
# #     plt.xlabel('Games')
# #     plt.title('Top 10 Games Sold for PS4')
# #     plt.bar(top_10_games().Game, top_10_games().Global)
# #     plt.show()
# #     plt.savefig('./Top 10 PS4 Games Sold.png')
#
# def save_top_10_data():
#     top_10_games().to_csv('Top 10 PS4 Games Sold', sep='\t')
#
# t1 = PythonOperator(task_id='read_csv', python_callable=read_csv(), dag=dag)
# t2 = PythonOperator(task_id='transform_data', python_callable=transform_data(), dag=dag)
# t2.setupstream(t1)
# t3 = PythonOperator(task_id='top_10_games', python_callable=top_10_games(), dag=dag)
# t3.setupstream(t2)
# # t4 = PythonOperator(task_id='graph_top_games', python_callable=graph_top_games(), dag=dag)
# t5 = PythonOperator(task_id='save_top_10_data', python_callable=save_top_10_data(), dag=dag)
# # t4.setupstream(t3)
# t5.setupstream(t3)
