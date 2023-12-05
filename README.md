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

# Зависимости
Install venv
```
python3.10 -m venv venv
source venv/bin/activate
```

Установить распложение airflow в текущей папке + установить airflow
```
export AIRFLOW_HOME="$(pwd)"
AIRFLOW_VERSION=2.7.3

# Extract the version of Python you have installed. If you're currently using a Python version that is not supported by Airflow, you may want to set this manually.
# See above for supported versions.
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"

CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
# For example this would install 2.7.3 with python 3.8: https://raw.githubusercontent.com/apache/airflow/constraints-2.7.3/constraints-3.8.txt

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```

Запустить airflow

`airflow standalone`

Тесты:

airflow tasks test task_1 push_current_date_time current_date