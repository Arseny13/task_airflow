# task_airflow

[Документация-туториал](https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html)

[Видео-туториал](https://www.youtube.com/watch?v=AHMm1wfGuHE&list=PLYizQ5FvN6pvIOcOd6dFZu3lQqc6zBGp2)

# Задача 
Необходимо создать даг, состоящий из двух тасков PythonOperator
даг работает каждый 15 минут
Один таск вычисляет текущее дату-время и передает это значение следующему таску
Второй таск берет значение от 1 таска и обрабатывает его следующим образом:
если значение минут < 30, то таск скипается
иначе выводит дату и завершается
регламент запуска дага задаем в формате cron
