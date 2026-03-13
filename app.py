import streamlit as st

# Configuración de la página (Diseño minimalista)
st.set_page_config(
    page_title="Dashboard Educativo: IA en Salud Mental",
    page_icon="🧠",
    layout="centered"
)

# Estilo personalizado (CSS) para bordes redondeados y diseño limpio
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #4A90E2;
        color: white;
        border: none;
    }
    .stExpander {
        border-radius: 15px;
        background-color: white;
        border: 1px solid #e1e4e8;
        margin-bottom: 10px;
    }
    .ref-card {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #4A90E2;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. SECCIÓN DEL TÍTULO [cite: 3, 4, 6]
st.markdown("<h1 style='text-align: center; color: #2c3e50;'>El terapeuta en tu bolsillo: ¿Puede un algoritmo sanar la mente?</h1>", unsafe_allow_html=True)

# 2. SECCIÓN DEL RESUMEN [cite: 7, 8, 9]
st.markdown("### Resumen")
st.info("""
Imagina que son las tres de la mañana. Una crisis de ansiedad o un pensamientorecurrente no te deja dormir. En lugar de esperar semanas por una cita clínica, sacas
tu teléfono y entablas una conversación con una inteligencia que no solo te escucha, sino que aplica décadas de ciencia psicológica para ayudarte a respirar. Lo que antes parecía ciencia ficción,
hoy es el campo de batalla de la salud mental moderna. ¿Es la Inteligencia Artificial (IA) un simple "plan B" o estamos ante la evolución definitiva del diván?
""")

st.divider()

# 3. SECCIÓN DE SUBTÍTULOS E INTERACTIVIDAD (Estructura de tarjetas/juego) [cite: 11, 12, 13, 15]
st.subheader("Explora las secciones del artículo")

# Tarjeta 1: Evolución
with st.expander("🔵 De las videollamadas al algoritmo inteligente"):
    st.write("""
  Durante años, la "telemedicina" fue poco más que una videollamada glorificada; un intento de eliminar la distancia física manteniendo el formato
  tradicional (Krzyżaniak et al., 2021). Sin embargo, el concepto ha mutado. Hemos pasado de leer guías en formato PDF a
  interactuar con sistemas que aprenden de nosotros.
  
La ciencia actual sugiere que lo digital ya no es el hermano menor de la terapia presencial. Investigadores como Hedman-Lagerlöf et al. (2023) han demostrado
que el formato digital es una alternativa real y efectiva para problemas psiquiátricos, logrando resultados prácticamente idénticos a los del cara a cara.
Incluso, en ciertos casos de depresión, la terapia electrónica ha mostrado ser ligeramente más efectiva en indicadores de severidad que las
sesiones tradicionales (Luo et al., 2020).
 """)

# Tarjeta 2: Metodología
with st.expander("🟢 El código detrás de la empatía"):
    st.write("""
   ¿Cómo puede una máquina "entender" nuestro sufrimiento? La respuesta no está en la magia, sino en la Teoría Cognitivo-Conductual (TCC). Al ser una
   metodología basada en pasos lógicos, tareas estructuradas y objetivos claros, la TCC es el lenguaje perfecto para ser traducido
   a algoritmos (Kambeitz-Ilankovic et al., 2022).
   
Sin embargo, no todo es tan sencillo como programar un bot. La psicología nos enseña que para que alguien sane, debe confiar en el proceso. Aquí entra 
la aceptabilidad: estudios recientes indican que los pacientes ya aceptan la terapia digital con el mismo rigor que la tradicional (Pauley et al., 2023).
El reto ahora es la personalización. Erasmus et al. (2025) advierten que la IA no puede ser una "talla única"; debe adaptarse a la complejidad de
cada caso, especialmente en terapias sistémicas donde las relaciones humanas son el eje central.

    """)

# Tarjeta 3: Desafíos
with st.expander("🟡 El gran desafío: ¿Por qué abandonamos el tratamiento?"):
    st.write("""
    Uno de los mayores obstáculos de la salud digital es la adherencia. Es mucho más fácil "dejar en visto" a una aplicación que faltar 
    a una cita con un terapeuta de carne y hueso. Las cifras lo confirman: mientras que en persona la tasa de permanencia es del 82.4%, en el 
    mundo digital baja al 72.9% (Kambeitz-Ilankovic et al., 2022).
    
Para cerrar esta brecha, la ciencia propone las intervenciones guiadas. No se trata de dejar al paciente solo con la máquina, sino
de usar la tecnología con el respaldo de un profesional humano. Este modelo híbrido parece ser la llave maestra para asegurar que el 
tratamiento realmente funcione (Hedman-Lagerlöf et al., 2023).
.
    """)

# Tarjeta 4: Futuro
with st.expander("🟣 El futuro: ¿Un mundo sin listas de espera?"):
    st.write("""
   La justificación para integrar la IA en la psicología es sólida: si ya sabemos que lo digital funciona (Luo et al., 2020), el siguiente paso
   es usar la IA para democratizar el acceso a la salud mental. El objetivo no es reemplazar al psicólogo, sino potenciar su alcance, eliminando
   barreras geográficas y económicas.
   
Estamos construyendo un andamiaje donde el rigor de la ciencia y la velocidad de los chips trabajan juntos. La pregunta para el futuro cercano 
no será si la IA puede ayudarnos, sino cómo diseñaremos estas herramientas para que sigan sintiéndose profundamente humanas.

    """)

st.divider()

# 4. BOTÓN PARA MOSTRAR REFERENCIAS [cite: 21, 38]
if "show_refs" not in st.session_state:
    st.session_state.show_refs = False

def toggle_refs():
    st.session_state.show_refs = not st.session_state.show_refs

st.button("📚 Ver Referencias", on_click=toggle_refs)

# Visualización de referencias separadas [cite: 22, 23, 24, 25]
if st.session_state.show_refs:
    st.markdown("### Referencias Bibliográficas")
    
    # Referencia 1
    st.markdown("""
    <div class="ref-card">
    <strong>Hernández Pérez, D. S. (2026). IA y ética en la evaluación psicológica.</strong><br>
    <em>Resumen:</em> Analiza el uso de IA para reconocer patrones y facilitar diagnósticos, advirtiendo sobre 
    sesgos algorítmicos y la necesidad de mantener el juicio clínico humano. [cite: 75, 76, 78, 80]
    </div>
    """, unsafe_allow_html=True)
    
    # Referencia 2
    st.markdown("""
    <div class="ref-card">
    <strong>Infocop. (2025). El uso ético de la IA en la psicología: directrices de la APA.</strong><br>
    <em>Resumen:</em> Presenta recomendaciones de la APA sobre protección de datos y supervisión humana, 
    subrayando que la IA complementa pero no reemplaza la responsabilidad del profesional. [cite: 82, 83, 85, 87]
    </div>
    """, unsafe_allow_html=True)
    
    # Referencia 3
    st.markdown("""
    <div class="ref-card">
    <strong>PAR, Inc. (2025). The ethical use of AI in psychology.</strong><br>
    <em>Resumen:</em> Describe cómo la IA ahorra tiempo en tareas administrativas y reportes, permitiendo 
    que el psicólogo se enfoque más en la atención directa del paciente. [cite: 88, 90, 92]
    </div>
    """, unsafe_allow_html=True)

# Pie de página educativo
st.markdown("---")
st.caption("Dashboard Interactivo - Ciencia y Psicología 2026")
