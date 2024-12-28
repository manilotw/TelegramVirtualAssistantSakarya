import openai 
from environs import Env
# Укажите ваш API-ключ 

env = Env()
env.read_env()
openai.api_key = env.str('CHATGPT_TOKEN')

# Список статей с ключевыми словами (вы можете добавить больше категорий или ссылок) 
articles = { 
    "сайт": "https://example.com/about-site", 
    "регистрация": "https://example.com/registration-guide", 
    "тарифы": "https://example.com/pricing", 
} 
 
# Функция для отправки запроса в ChatGPT и получения ответа 
def get_chatgpt_response(user_query): 
    # Отправляем запрос в модель OpenAI 
    response = openai.ChatCompletion.create( 
        model="gpt-4",  # Используйте gpt-3.5 или gpt-4 в зависимости от вашей подписки 
        messages=[ 
            {"role": "system", "content": "Ты виртуальный помощник, который помогает пользователю."}, 
            {"role": "user", "content": user_query} 
        ] 
    ) 
     
    # Извлекаем ответ от ChatGPT 
    response_text = response["choices"][0]["message"]["content"].strip() 
    return response_text 
 
# Функция для поиска статьи или получения общего ответа 
def get_article_or_info(user_query): 
    # Получаем ответ от ChatGPT 
    response_text = get_chatgpt_response(user_query) 
 
    # Ищем совпадение намерения с ключевыми словами 
    for keyword, link in articles.items(): 
        if keyword in user_query.lower():  # Проверяем наличие ключевого слова в запросе 
            return f"Вот подходящая статья: {link}" 
 
    # Если ключевые слова не найдены, возвращаем ответ от ChatGPT 
    return response_text 
 
# Пример использования 
