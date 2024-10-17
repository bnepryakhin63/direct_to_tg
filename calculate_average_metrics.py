def calculate_average_metrics(data, days):
    """Вычисляем средние значения по данным за указанный период (days)"""
    # Суммируем все значения по всем данным
    total_cost = data['TotalCost'].sum()
    total_clicks = data['TotalClicks'].sum()
    total_conversions = data['TotalConversions'].sum()
    
    # Рассчитываем средние значения
    avg_data = {
        'TotalCost': total_cost,
        'TotalClicks': total_clicks,
        'TotalConversions': total_conversions,
        'AverageCost': total_cost / days,
        'AverageClicks': total_clicks / days,
        'AverageConversions': total_conversions / days
    }

    # Преобразуем в DataFrame для удобства
    return pd.DataFrame([avg_data])

def calculate_deviations(data_7_days, data_30_days, data_90_days):
    """Вычисляем отклонения средних значений за 30 и 90 дней относительно данных за 7 дней"""
    # Вычисляем средние значения за 7, 30 и 90 дней
    avg_7_days = calculate_average_metrics(data_7_days, 7)
    avg_30_days = calculate_average_metrics(data_30_days, 30)
    avg_90_days = calculate_average_metrics(data_90_days, 90)

    # Рассчитываем отклонения для 30 дней
    deviation_data = {
        'AverageCost': avg_7_days['AverageCost'][0],
        'AverageClicks': avg_7_days['AverageClicks'][0],
        'AverageConversions': avg_7_days['AverageConversions'][0],
        'DeviationCost_30': ((avg_7_days['AverageCost'][0] - avg_30_days['AverageCost'][0]) / avg_30_days['AverageCost'][0]) * 100,
        'DeviationClicks_30': ((avg_7_days['AverageClicks'][0] - avg_30_days['AverageClicks'][0]) / avg_30_days['AverageClicks'][0]) * 100,
        'DeviationConversions_30': ((avg_7_days['AverageConversions'][0] - avg_30_days['AverageConversions'][0]) / avg_30_days['AverageConversions'][0]) * 100,
        'DeviationCost_90': ((avg_7_days['AverageCost'][0] - avg_90_days['AverageCost'][0]) / avg_90_days['AverageCost'][0]) * 100,
        'DeviationClicks_90': ((avg_7_days['AverageClicks'][0] - avg_90_days['AverageClicks'][0]) / avg_90_days['AverageClicks'][0]) * 100,
        'DeviationConversions_90': ((avg_7_days['AverageConversions'][0] - avg_90_days['AverageConversions'][0]) / avg_90_days['AverageConversions'][0]) * 100
    }

    # Преобразуем в DataFrame для удобства
    return pd.DataFrame([deviation_data])

# Итоговые данные
merged_data = calculate_deviations(last_7_days, last_30_days, last_90_days)
merged_data