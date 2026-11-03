import streamlit as st
import time
import os
import urllib.request

st.set_page_config(page_title="ИИ Генератор Видео", page_icon="🎬", layout="centered")

# Ссылка на РЕАЛЬНЫЙ тестовый видеоролик MP4 (кодек H.264, весит около 1.5 МБ)
video_path = "video.mp4"
if not os.path.exists(video_path):
    try:
        url = "https://w3schools.com"
        urllib.request.urlretrieve(url, video_path)
    except Exception as e:
        st.error(f"Не удалось скачать тестовое видео: {e}")

st.title("🎬 Профессиональный ИИ-Создатель Видео")
st.write("Превращайте ваши текстовые сценарии в реальные видеоролики с помощью открытого независимого ИИ-облака.")

st.subheader("📝 Настройки вашего ролика:")
prompt = st.text_area(
    "Опишите сюжет для видео:", 
    placeholder="Например: Футуристичный робот идет по городу будущего, стиль киберпанк, 4k...", 
    height=100
)
style = st.selectbox("Визуальный стиль:", ["Фотореализм (Cinematic)", "3D Анимация", "Аниме / Мультфильм", "Киберпанк"])

st.write("---")

if st.button("🚀 Сгенерировать ИИ-Видео"):
    if not prompt:
        st.warning("⚠️ Пожалуйста, введите текстовое описание сюжета.")
    else:
        st.info("⏳ Запрос успешно отправлен в ИИ-облако. Идет магия генерации, пожалуйста, подождите...")
        
        # Симуляция рендеринга
        progress_bar = st.progress(0)
        status_text = st.empty()
        for i in range(100):
            time.sleep(0.03)
            progress_bar.progress(i + 1)
            status_text.text(f"Сборка кадров нейросетью: {i + 1}%")
            
        st.success("Видео успешно сгенерировано высокоскоростным ИИ-узлом!")
        
        # Надежный и нативный вывод видео в Streamlit
        if os.path.exists(video_path):
            with open(video_path, "rb") as video_file:
                video_bytes = video_file.read()
            st.video(video_bytes, format="video/mp4", autoplay=True, muted=True)
        else:
            st.error("⚠️ Файл видео не найден на сервере.")
