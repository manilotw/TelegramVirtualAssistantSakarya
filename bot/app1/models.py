from django.db import models

class User(models.Model):
    """Модель для хранения информации о пользователях из Телеграма."""
    telegram_username = models.CharField(max_length=150, unique=True, verbose_name="Ник в Телеграме")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")

    def __str__(self):
        return self.telegram_username


class Query(models.Model):
    """Модель для хранения общих запросов."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="queries", verbose_name="Пользователь")
    description = models.TextField(verbose_name="Описание запроса")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата поступления")
    chatgpt_response = models.TextField(blank=True, null=True, verbose_name="Ответ от ChatGPT")

    def __str__(self):
        return f"Запрос от {self.user.telegram_username} ({self.created_at})"


class Question(models.Model):
    """Модель для хранения вопросов."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions", verbose_name="Пользователь")
    description = models.TextField(verbose_name="Описание вопроса")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата поступления")
    chatgpt_response = models.TextField(blank=True, null=True, verbose_name="Ответ от ChatGPT")

    def __str__(self):
        return f"Вопрос от {self.user.telegram_username} ({self.created_at})"


class Complaint(models.Model):
    """Модель для хранения жалоб."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="complaints", verbose_name="Пользователь")
    message = models.TextField(verbose_name="Сообщение жалобы")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата поступления")
    is_resolved = models.BooleanField(default=False, verbose_name="Решено")

    def __str__(self):
        return f"Жалоба от {self.user.telegram_username} ({'Решено' if self.is_resolved else 'Не решено'})"
