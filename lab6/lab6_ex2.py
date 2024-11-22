import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Завантаження даних
data = pd.read_csv('renfe_small.csv')

# Попередня обробка даних
data['start_date'] = pd.to_datetime(data['start_date'])
data['День'] = data['start_date'].dt.day
data['Місяць'] = data['start_date'].dt.month
data['Рік'] = data['start_date'].dt.year

# Видалення непотрібних колонок
data = data.drop(columns=['start_date', 'insert_date', 'end_date'])

# Заповнення відсутніх значень
data = data.dropna(subset=['price'])
data = data.dropna()

# Перетворення цільової змінної на категоричну
bins = [0, 50, 100, np.inf]  # Визначення категорій
labels = ['cheap', 'moderate', 'expensive']  # Відповідні мітки
data['price'] = pd.cut(data['price'], bins=bins, labels=labels)

# Розділення даних на навчальний та тестовий набори
X = data.drop('price', axis=1)
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Кодування текстових даних за допомогою OneHotEncoder та перетворення на густий формат
categorical_features = ['origin', 'destination', 'train_type', 'train_class', 'fare']
categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', categorical_transformer, categorical_features)
    ],
    remainder='passthrough'
)

# Створення та навчання моделі з використанням Pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', GaussianNB())
])

model.fit(X_train, y_train)

# Прогнозування та оцінка моделі
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Приклад прогнозування цінової категорії з ймовірностями
new_data = pd.DataFrame({
    'День': [15],
    'Місяць': [6],
    'Рік': [2024],
    'origin': ['Madrid'],
    'destination': ['Barcelona'],
    'train_type': ['AVE'],
    'train_class': ['Preferente'],
    'fare': ['Promo']
})
predicted_price_category = model.predict(new_data)
predicted_probabilities = model.predict_proba(new_data)

print(f"Predicted price category: {predicted_price_category[0]}")
print("Predicted probabilities:")
for category, probability in zip(model.classes_, predicted_probabilities[0]):
    print(f" {category}: {probability:.6f}")