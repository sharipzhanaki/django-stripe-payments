# Django Stripe Payments

Django + Stripe API сервис для создания платёжных форм. Поддерживает оплату отдельных товаров и заказов со скидками и налогами.

## Демо

🌐 **Задеплоенное приложение:** https://django-stripe-payments-production.up.railway.app/

🔑 **Доступ к Django Admin:**
- URL: https://django-stripe-payments-production.up.railway.app/admin/
- Login: `admin`
- Password: `test1234!`

---

## Реализованный функционал

### Основное задание
- Модель `Item` (name, description, price, currency)
- `GET /item/{id}` — HTML страница с информацией о товаре и кнопкой Buy
- `GET /buy/{id}` — возвращает Stripe Session Id, на фронтенде происходит `redirectToCheckout`

### Бонусные задачи
- ✅ Запуск через Docker
- ✅ Использование environment variables (`.env`)
- ✅ Просмотр и управление моделями через Django Admin
- ✅ Запуск на удалённом сервере с доступом к админке
- ✅ Модель `Order` — объединяет несколько `Item`, оплата на общую сумму
- ✅ Модели `Discount` и `Tax` — прикрепляются к `Order`, учитываются при расчёте итоговой суммы
- ✅ Поле `Item.currency` (USD / EUR) — два набора Stripe ключей, валюта выбирается автоматически
- ✅ Stripe Payment Intent для `Order` — платёжная форма Stripe Elements встроена в страницу

---

## API

| Метод | URL | Описание |
|---|---|---|
| GET | `/item/<id>/` | HTML страница товара с кнопкой Buy |
| GET | `/buy/<id>/` | JSON с `id` Stripe Checkout Session для товара |
| GET | `/order/<id>/` | HTML страница заказа со встроенной формой оплаты |
| GET | `/buy/order/<id>/` | JSON с `client_secret` для Stripe Payment Intent заказа |

---

## Запуск локально

### Через Python

**1. Клонировать репозиторий:**
```bash
git clone https://github.com/sharipzhanaki/django-stripe-payments.git
cd django-stripe-payments
```

**2. Создать и активировать виртуальное окружение:**
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

**3. Установить зависимости:**
```bash
pip install -r requirements.txt
```

**4. Создать `.env` файл в корне проекта:**
```bash
cp .env.example .env
```
Заполнить реальными значениями:
```
SECRET_KEY=django-insecure-...
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

STRIPE_PUBLIC_KEY_USD=pk_test_...
STRIPE_SECRET_KEY_USD=sk_test_...
STRIPE_PUBLIC_KEY_EUR=pk_test_...
STRIPE_SECRET_KEY_EUR=sk_test_...
```

**5. Применить миграции и создать суперпользователя:**
```bash
cd stripe_payments
python manage.py migrate
python manage.py createsuperuser
```

**6. Запустить сервер:**
```bash
python manage.py runserver
```

Приложение доступно на http://localhost:8000

---

### Через Docker

**1. Создать `.env` файл в корне проекта (шаг 4 выше)**

**2. Собрать и запустить контейнер:**
```bash
docker compose up --build
```

Приложение доступно на http://localhost:8000

**Создать суперпользователя в контейнере:**
```bash
docker compose exec web python manage.py createsuperuser
```

---

## Тестовая оплата

Для тестирования используй карту Stripe:

| Поле | Значение |
|---|---|
| Номер карты | `4242 4242 4242 4242` |
| Дата | любая будущая, например `12/34` |
| CVC | любые 3 цифры |

---

## Структура проекта

```
django-stripe-payments/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── .env                          # не коммитится в git
└── stripe_payments/              # Django проект
    ├── manage.py
    ├── items/                    # Приложение товаров
    │   ├── models.py             # Модель Item
    │   ├── views.py
    │   ├── services.py           # Stripe Checkout Session для Item
    │   └── templates/
    ├── orders/                   # Приложение заказов
    │   ├── models.py             # Модели Order, Discount, Tax
    │   ├── views.py
    │   ├── services.py           # Stripe Payment Intent для Order
    │   └── templates/
    └── stripe_payments/          # Настройки Django
        ├── settings.py
        ├── urls.py
        └── services.py           # Общий get_stripe_keys
```

---

## Переменные окружения

| Переменная | Описание |
|---|---|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | Режим отладки (`True` / `False`) |
| `ALLOWED_HOSTS` | Разрешённые хосты через запятую |
| `CSRF_TRUSTED_ORIGINS` | Доверенные источники для CSRF (нужно для деплоя) |
| `STRIPE_PUBLIC_KEY_USD` | Stripe публичный ключ для USD |
| `STRIPE_SECRET_KEY_USD` | Stripe секретный ключ для USD |
| `STRIPE_PUBLIC_KEY_EUR` | Stripe публичный ключ для EUR |
| `STRIPE_SECRET_KEY_EUR` | Stripe секретный ключ для EUR |
