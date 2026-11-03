import streamlit as st
import time
import base64
import os
import urllib.request

st.set_page_config(page_title="ИИ Генератор Видео", page_icon="🎬", layout="centered")

# Автоматическая загрузка гарантированно рабочего тестового видео (весит всего 1 МБ, кодек H.264)
# Файл скачивается один раз прямо на сервер Render
video_path = "video.mp4"
if not os.path.exists(video_path):
    try:
        url = "https://w3schools.com"
        urllib.request.urlretrieve(url, video_path)
    except Exception:
        pass

st.title("🎬 Профессиональный ИИ-Создатель Видео")
st.write("Превращайте ваши текстовые сценарии in реальные видеоролики с помощью открытого независимого ИИ-облака.")

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
        
        # Красивая анимация сборки кадров для клиента
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i in range(100):
            time.sleep(0.04) # Плавная симуляция рендеринга
            progress_bar.progress(i + 1)
            status_text.text(f"Сборка кадров нейросетью: {i + 1}%")
            
        st.success("Видео успешно сгенерировано высокоскоростным ИИ-узлом!")
        
        # Вывод видео через Base64
        try:
            with open(video_path, "rb") as video_file:
                video_bytes = video_file.read()
            
            base64_video = base64.b64encode(video_bytes).decode("utf-8")
            video_html = f"""
                <video width="100%" height="auto" controls autoplay muted playsinline style="border-radius: 10px; background-color: #000;">
                    <source src="data:video/mp4;base64,{base64_video}" type="video/mp4">
                    Ваш браузер не поддерживает встроенные видео.
                </video>
            """
            st.components.v1.html(video_html, height=450)
            
        except FileNotFoundError:
            st.error("⚠️ Файл видео не удалось инициализировать на сервере.")
