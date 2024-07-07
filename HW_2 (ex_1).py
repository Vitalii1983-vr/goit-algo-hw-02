import queue  # модуль для використання черги
import random  # модуль для генерації випадкових чисел
import time  # модуль часу для імітації затримок

# Створюємо чергу для заявок
request_queue = queue.Queue()

def generate_request(request_queue, request_id):
    """
    Функція для генерації та додавання нових заявок до черги
    :param request_queue: черга, до якої буде додано заявку
    :param request_id: унікальний ідентифікатор заявки
    """
    print(f"Генеруємо нову заявку з ID: {request_id}")
    request_queue.put(request_id)  # Додаємо нову заявку до черги

def process_request(request_queue):
    """
    Функція для обробки заявок, видаляючи їх з черги
    :param request_queue: черга заявок для обробки
    """
    if not request_queue.empty():  # Перевірка, чи черга не пуста
        request_id = request_queue.get()  # Видалення заявки з черги для обробки
        print(f"Обробляємо заявку з ID: {request_id}")
    else:
        print("Черга пуста, немає заявок для обробки")

def main():
    """
    Головна функція для управління генерацією та обробкою заявок
    """
    request_id = 0  # Ініціалізація першого ID заявки
    
    # Безкінечний цикл для генерації та обробки заявок
    try:
        while True:
            generate_request(request_queue, request_id)
            time.sleep(random.randint(1, 3))  # Симуляція затримки до наступної заявки
            
            process_request(request_queue)
            time.sleep(random.randint(1, 2))  # Симуляція часу обробки заявки
            
            request_id += 1  # Інкрементація ID для наступної заявки
            
            # Обмеження для автоматичного виходу з циклу після 5 заявок
            if request_id > 5:
                break
    except KeyboardInterrupt:
        print("Програму зупинено користувачем")

if __name__ == "__main__":
    main()  # Запуск головної функції програми
