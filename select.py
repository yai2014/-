import psycopg2

try:
    # Устанавливаем соединение (с параметрами из вашего docker-compose.yml)
    connection = psycopg2.connect(
        host="localhost",              # База в контейнере, доступна через localhost
        port="5430",                   # Ваш порт (из docker ps и DBeaver)
        user="postgres_user",          # POSTGRES_USER из docker-compose.yml
        password="postgres_password",  # POSTGRES_PASSWORD из docker-compose.yml
        database="postgres_db"         # POSTGRES_DB из docker-compose.yml
    )
    
    cursor = connection.cursor()
    
    # Проверка подключения - получаем версию PostgreSQL
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print(f"✅ Подключение успешно!")
    print(f"Версия PostgreSQL: {version[0][:60]}...")
    
    # 1. Выполняем запрос

    cursor.execute("SELECT first_name, last_name FROM students;")



    # 2. Извлекаем все строки

    students = cursor.fetchall()



    for student in students:

        print(f"Студент: {student[0]} {student[1]}")



    # Не забываем закрыть курсор

    cursor.close()



except Exception as error:

    print(f"Ошибка при подключении: {error}")