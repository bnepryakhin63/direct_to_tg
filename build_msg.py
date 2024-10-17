# Получаем текущую дату в формате "День, Месяц Число, Год"
current_date = datetime.now().strftime("%B %d, %Y")

def build_msg(data):
    # Извлекаем общие агрегированные данные
    total_row = data.iloc[0]

    SUM7 = total_row['AverageCost']
    SUMCLICKS7 = total_row['AverageClicks']
    SUMCONV7 = total_row['AverageConversions']

    # Отклонения
    DEVCOST30 = total_row['DeviationCost_30']
    DEVCLICKS30 = total_row['DeviationClicks_30']
    DEVCONV30 = total_row['DeviationConversions_30']

    DEVCOST90 = total_row['DeviationCost_90']
    DEVCLICKS90 = total_row['DeviationClicks_90']
    DEVCONV90 = total_row['DeviationConversions_90']

    # Основное сообщение с итогами
    message = f"""
    ===
    <b>Отчет на дату: {current_date} </b>

    Итоги за 7 дней:    
    Среднедневные показатели:

    Бюджет: {formatter(SUM7)} руб.
    Кол-во кликов: {formatter(SUMCLICKS7)}
    Кол-во конверсий: {formatter(SUMCONV7)}

    <b>Сравнение с 30 днями:</b>
    Бюджет: {get_trend_text(DEVCOST30)} на {formatter(DEVCOST30, 1)}
    Клики: {get_trend_text(DEVCLICKS30)} на {formatter(DEVCLICKS30, 1)}
    Конверсии: {get_trend_text(DEVCONV30)} на {formatter(DEVCONV30, 1)}

    <b>Сравнение с 90 днями:</b>
    Бюджет: {get_trend_text(DEVCOST90)} на {formatter(DEVCOST90, 1)}
    Клики: {get_trend_text(DEVCLICKS90)} на {formatter(DEVCLICKS90, 1)}
    Конверсии: {get_trend_text(DEVCONV90)} на {formatter(DEVCONV90, 1)}
    """

    return message

def formatter(text, type=0):
    if type == 0:
        return '{:,.0f}'.format(text).replace(',', ' ')
    elif type == 1:
        return '{:+.0f}%'.format(text)

def get_trend_text(value):
    """Определяет тренд на основе знака значения."""
    if value < 0:
        return "снижение"
    else:
        return "рост"