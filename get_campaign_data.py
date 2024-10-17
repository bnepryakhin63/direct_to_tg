from sqlalchemy import create_engine
import pandas as pd
from datetime import  datetime
import requests

def get_campaign_data(user, password, host, port, dbname):
    # Формируем строку подключения
    db_url = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{dbname}?auth_plugin=mysql_native_password"

    # Создаем подключение к базе данных
    engine = create_engine(db_url)

    # SQL-запрос для расчёта метрик за последнюю неделю без разбивки по кабинетам
    query = """
        SELECT 
        'Общие данные' AS CabinetName,  -- Название кабинета
        ROUND(SUM(tf.Cost)) AS TotalCost,  -- Затраты
        SUM(tf.Clicks) AS TotalClicks,  -- Количество кликов
        SUM(
            COALESCE(tf.goal_1, 0) + 
            COALESCE(tf.goal_2, 0) + 
            COALESCE(tf.goal_3, 0) + 
            COALESCE(tf.goal_4, 0) + 
            COALESCE(tf.goal_5, 0) + 
            COALESCE(tf.goal_6, 0)
        ) AS TotalConversions,  -- Число конверсий
        SUM(tf.Impressions) AS TotalImpressions,  -- Охваты рекламы (Impressions)
        ROUND(SUM(tf.Cost) / NULLIF(SUM(tf.Clicks), 0)) AS AverageCPC,  -- Средняя CPC
        ROUND(SUM(tf.Cost) / NULLIF(
            SUM(
                COALESCE(tf.goal_1, 0) + 
                COALESCE(tf.goal_2, 0) + 
                COALESCE(tf.goal_3, 0) + 
                COALESCE(tf.goal_4, 0) + 
                COALESCE(tf.goal_5, 0) + 
                COALESCE(tf.goal_6, 0)
            ), 0)) AS CPA  -- CPA (стоимость за конверсию)
    FROM `user_pr_bi`.`tf_direct` AS tf
    WHERE tf.Date >= DATE_SUB(CURDATE(), INTERVAL 7 DAY)  -- Фильтр за последнюю неделю
    """
    
    # Запрос за последние 30 дней
    query_last_30_days = query.replace("7 DAY", "30 DAY")

    # Запрос за последние 90 дней
    query_last_90_days = query.replace("7 DAY", "90 DAY")

    # Выполняем SQL-запросы и загружаем результаты в DataFrame
    last_7_days_data = pd.read_sql(query, con=engine)
    last_30_days_data = pd.read_sql(query_last_30_days, con=engine)
    last_90_days_data = pd.read_sql(query_last_90_days, con=engine)

    return last_7_days_data, last_30_days_data, last_90_days_data
