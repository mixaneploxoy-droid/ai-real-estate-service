import streamlit as st
import torch
import torch.nn as nn
import joblib
import numpy as np
import os

# 1. Точно копируем архитектуру нашей нейросети
class RealEstatePredictor(nn.Module):
    def __init__(self):
        super(RealEstatePredictor, self).__init__()
        self.fc1 = nn.Linear(5, 64)
        self.relu1 = nn.ReLU()
        self.fc2 = nn.Linear(64, 32)
        self.relu2 = nn.ReLU()
        self.fc3 = nn.Linear(32, 16)
        self.relu3 = nn.ReLU()
        self.output = nn.Linear(16, 1)
        
    def forward(self, x):
        x = self.relu1(self.fc1(x))
        x = self.relu2(self.fc2(x))
        x = self.relu3(self.fc3(x))
        x = self.output(x)
        return x

st.title("🤖 ИИ-Оценщик Недвижимости")

# Проверим, видит ли скрипт файлы в текущей папке
st.write("Текущая рабочая папка сервера:", os.getcwd())
st.write("Файлы в папке:", os.listdir('.'))

# Прямая загрузка без скрытия ошибок
st.write("🔄 Загрузка ИИ-компонентов...")
scaler = joblib.load('scaler.pkl')
model = RealEstatePredictor()
model.load_state_dict(torch.load('housing_model.pth'))
model.eval()
st.success("✅ Все компоненты успешно загружены!")

# Создаем удобные поля ввода и слайдеры для пользователей сайта
med_inc = st.number_input("Медианный доход семьи в районе (в тыс. $):", min_value=0.5, max_value=15.0, value=3.5, step=0.1)
house_age = st.slider("Средний возраст домов в районе (лет):", min_value=1, max_value=52, value=25)
ave_rooms = st.number_input("Среднее количество комнат в доме:", min_value=1.0, max_value=10.0, value=5.0, step=0.1)
ave_bedrms = st.number_input("Среднее количество спален в доме:", min_value=1.0, max_value=5.0, value=1.0, step=0.1)
population = st.number_input("Количество жителей в районе (человек):", min_value=10, max_value=50000, value=1500)

# Главная кнопка на сайте
if st.button("📊 Рассчитать стоимость"):
    user_data = np.array([[med_inc, house_age, ave_rooms, ave_bedrms, population]])
    user_data_scaled = scaler.transform(user_data)
    user_data_tensor = torch.tensor(user_data_scaled, dtype=torch.float32)
    
    with torch.no_grad():
        prediction = model(user_data_tensor).item()
    
    final_price = prediction * 100000
    st.success(f"🎯 Прогноз нейросети: Средняя стоимость жилья в этом районе составляет **${final_price:,.2f}**")
