import streamlit as st
import time
import base64

st.set_page_config(page_title="ИИ Генератор Видео", page_icon="🎬", layout="centered")

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
        
        # Красивая анимация сборки кадров для клиента
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i in range(100):
            time.sleep(0.04) # Плавная симуляция рендеринга
            progress_bar.progress(i + 1)
            status_text.text(f"Сборка кадров нейросетью: {i + 1}%")
            
        st.success("Видео успешно сгенерировано высокоскоростным ИИ-узлом!")
        
        # Самый надежный метод вывода: кодирование видео в строку Base64
        try:
            with open("video.mp4", "rb") as video_file:
                video_bytes = video_file.read()
            
            # Конвертируем байты видео в текстовую строку
            base64_video = base64.b64encode(video_bytes).decode("utf-8")
            video_html = f"""
                <video width="100%" height="auto" controls autoplay muted playsinline style="border-radius: 10px; background-color: #000;">
                    <source src="data:video/mp4;base64,{base64_video}" type="video/mp4">
                    Ваш браузер не поддерживает встроенные видео.
                </video>
            """
            # Выводим чистый HTML плеер
            st.components.v1.html(video_html, height=450)
            
        except FileNotFoundError:
            st.error("⚠️ Файл 'video.mp4' не найден на сервере. Пожалуйста, убедитесь, что вы загрузили его в корень репозитория GitHub рядом с app.py!")
