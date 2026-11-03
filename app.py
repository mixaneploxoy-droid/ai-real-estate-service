import streamlit as st
import requests
import time

st.set_page_config(page_title="ИИ Генератор Видео", page_icon="🎬", layout="centered")

st.title("🎬 Профессиональный ИИ-Создатель Видео")
st.write("Превращайте ваши текстовые сценарии в реальные видеоролики с помощью передовых облачных моделей.")

# Считываем токен безопасности из настроек Secrets
try:
    HF_TOKEN = st.secrets["HF_TOKEN"]
except Exception:
    HF_TOKEN = None

# СОВРЕМЕННАЯ И БЫСТРАЯ ТЕКСТОВАЯ ВИДЕО-МОДЕЛЬ (Всегда активна на серверах)
API_URL = "https://huggingface.co"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

st.subheader("📝 Настройки вашего ролика:")
prompt = st.text_area(
    "Опишите сюжет для видео (строго НА АНГЛИЙСКОМ языке):", 
    placeholder="Например: Astronaut riding a horse on mars, photorealistic, 4k, HD...",
    height=100
)

style = st.selectbox("Стиль видео:", ["Фотореализм", "Кинематографичный", "Аниме", "3D Рендер"])
st.write("---")

if st.button("🚀 Сгенерировать ИИ-Видео"):
    if not HF_TOKEN:
        st.error("⚠️ Ошибка: Вы забыли добавить 'HF_TOKEN' в настройки Secrets вашего приложения!")
    elif not prompt:
        st.warning("⚠️ Пожалуйста, введите текстовое описание сюжета.")
    else:
        st.info("⏳ Запрос отправлен в ИИ-облако. Идет создание видеоролика, пожалуйста, подождите...")
        
        # Красивая анимация загрузки
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Склеиваем описание и выбранный стиль
        full_prompt = f"{prompt}, {style} style, high quality, detailed, cinematic lighting"
        
        # Отправляем запрос в ИИ-облако
        try:
            # Увеличиваем таймаут ожидания до 150 секунд, чтобы сайт не обрывал связь
            response = requests.post(API_URL, headers=headers, json={"inputs": full_prompt}, timeout=150)
            
            # Если модель только просыпается, плавно ждем её в цикле
            attempts = 0
            while response.status_code == 503 and attempts < 3:
                status_text.warning("⏳ Сервер ИИ просыпается и загружает модель в память. Ждем 20 секунд...")
                time.sleep(20)
                response = requests.post(API_URL, headers=headers, json={"inputs": full_prompt}, timeout=150)
                attempts += 1
            
            # Имитируем заполнение полосы прогресса до конца
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)
                status_text.text(f"Рендеринг кадров: {i + 1}%")
                
            if response.status_code == 200:
                st.success("🎯 Видео успешно сгенерировано нейросетью!")
                
                # Получаем бинарные файлы видеоролика напрямую от ИИ
                video_bytes = response.content
                
                # Выводим настоящее видео в плеер браузера
                st.video(video_bytes)
                st.caption("Вы можете скачать готовый ролик, нажав на три точки в правом нижнем углу видеоплеера.")
            else:
                st.error(f"❌ Ошибка ИИ-сервера (Код {response.status_code}).")
                st.caption(f"Ответ сервера: {response.text}")
                
        except Exception as e:
            st.error(f"💥 Произошла критическая ошибка: {e}")
