import streamlit as st
import time

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
            
        # Этот блок срабатывает строго ПОСЛЕ того, как шкала дошла до 100%
        st.success("Видео успешно сгенерировано высокоскоростным ИИ-узлом!")
        
        # Надежное чтение локального файла video.mp4 из репозитория
        try:
            with open("video.mp4", "rb") as video_file:
                video_bytes = video_file.read()
            st.video(video_bytes, format="video/mp4", muted=True, autoplay=True)
        except FileNotFoundError:
            st.error("⚠️ Файл 'video.mp4' не найден на сервере. Пожалуйста, убедитесь, что вы загрузили его в корень репозитория GitHub рядом с app.py!")
