import streamlit as st
import streamlit.components.v1 as components
import base64, json
from pathlib import Path

st.set_page_config(page_title="Salud Mental en IT", page_icon="🧠", layout="wide")

st.markdown("""
<style>
    .hero-container {
        background: linear-gradient(135deg, rgba(23,89,124,0.95) 0%, rgba(132,179,206,0.85) 100%);
        padding: 3rem 2rem; border-radius: 20px; text-align: center;
        box-shadow: 0 10px 20px rgba(4,22,33,.2); margin-bottom: 2rem;
    }
    .hero-title { font-size: 3.5rem; font-weight: 900; margin-bottom: .5rem; color: #fff; }
    .hero-subtitle { font-size: 1.4rem; color: #bee8ff; font-style: italic; }
    [class*="st-key-card_"] { border: 2px solid #84B3CE; border-radius: 18px; padding: 1rem 1.2rem; }
</style>

<div class="hero-container">
    <div class="hero-title">Salud Mental en la Industria Tech</div>
    <div class="hero-subtitle">
        Un análisis estadístico sobre la percepción de perjuicio profesional según la jerarquía y la edad.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("### Explora el proyecto")

secciones = [
    ("teoria", "📚 Marco Teórico", "Descubre los modelos de estrés laboral y el contexto histórico.",
     "pages/02_Marco_Teorico.py", "Leer Teoría ➔", "📖"),
    ("metodo", "🧪 Marco Metodológico", "Conoce el proceso de limpieza de datos y las variables operacionalizadas.",
     "pages/03_Marco_Metodologico.py", "Ver Metodología ➔", "🔬"),
    ("result", "📊 Resultados y ANOVA", "Explora las visualizaciones interactivas, las pruebas de supuestos y el modelo.",
     "pages/04_Resultados.py", "Ver Resultados ➔", "🚀"),
]

for col, (k, titulo, desc, pag, lbl, ico) in zip(st.columns(3), secciones):
    with col, st.container(key=f"card_{k}"):
        st.markdown(f"#### {titulo}")
        st.write(desc)
        st.page_link(pag, label=lbl, icon=ico)

st.divider()

DUR_GIF = 3000
INTRO = "¡Hola! Soy <b>Pelusa</b>, tu asistente en esta investigación. Haz clic en mí y te cuento datos curiosos."
DATOS = [
    "Analizamos una muestra de 1.311 profesionales del sector tech del año 2016.",
    "El modelo de Karasek sugiere que los operativos, al tener menos control, son más vulnerables al estrés.",
    "Aunque la edad no mostró diferencias significativas, la jerarquía sí resultó ser un factor clave.",
    "Este proyecto usa la base de datos de OSMI, una iniciativa para visibilizar la salud mental en IT.",
    "La prueba ANOVA reveló que el puesto de trabajo influye en cómo se percibe el estigma (p = 0,0168).",
]

@st.cache_data
def b64(ruta, mime):
    try:
        return f"data:{mime};base64," + base64.b64encode(Path(ruta).read_bytes()).decode()
    except FileNotFoundError:
        return ""

# el iframe no ve la carpeta assets, por eso las imágenes van en base64
gif = b64("assets/pelusa.gif", "image/gif")
png = b64("assets/pelusa1.png", "image/png")

HTML = r"""
<style>
  * { box-sizing: border-box; }
  body { margin: 0; font-family: 'Segoe UI', sans-serif; background: transparent; }
  .stage { display: flex; align-items: center; gap: 30px; flex-wrap: wrap; padding: 6px; }

  .quote { flex: 1 1 360px; padding: 10px 10px 10px 4px; }
  .quote .mark { display: block; font: 110px/.6 Georgia, serif; color: #84B3CE; height: 52px; }
  .quote p { margin: 0; color: #17597C; font-family: Georgia, serif; font-weight: 700;
             font-size: clamp(1.6rem, 3vw, 2.4rem); line-height: 1.35; }
  .quote em { font-style: italic; padding: 0 4px; background: linear-gradient(transparent 58%, #ffd98a 58%); }
  .quote .line { width: 90px; height: 5px; border-radius: 4px; background: #84B3CE; margin-top: 22px; }

  .pelusa { flex: 1 1 440px; display: flex; flex-direction: column; align-items: center; }
  .bubble { position: relative; width: 100%; max-width: 420px; min-height: 118px;
            background: #d6e8f3; color: #17597C; border: 2px solid #84B3CE; border-radius: 20px;
            padding: 14px 20px 16px; font-size: 16px; line-height: 1.45; text-align: center;
            box-shadow: 0 8px 20px rgba(23,89,124,.14); margin-bottom: 16px; }
  /* la cola son dos triángulos: uno de borde y otro encima de relleno */
  .bubble::after, .bubble::before { content: ""; position: absolute; left: 50%; transform: translateX(-50%);
                                    border-style: solid; }
  .bubble::after { bottom: -13px; border-width: 13px 12px 0; border-color: #84B3CE transparent transparent; }
  .bubble::before { bottom: -9px; border-width: 11px 10px 0; border-color: #d6e8f3 transparent transparent; z-index: 2; }
  .label { font-weight: 800; font-size: 12px; letter-spacing: .1em; text-transform: uppercase;
           color: #2f86b0; margin-bottom: 4px; }

  #char { width: 460px; max-width: 100%; cursor: pointer; user-select: none; transition: transform .15s; }
  #char:hover { transform: scale(1.04); }
</style>

<div class="stage">
  <div class="quote">
    <span class="mark">&ldquo;</span>
    <p>Un entorno laboral saludable no es un lujo, es el cimiento sobre el cual se construye el <em>verdadero éxito</em>.</p>
    <div class="line"></div>
  </div>
  <div class="pelusa">
    <div class="bubble"><div class="label" id="label">Pelusa</div><div id="txt"></div></div>
    <img src="__PNG__" id="char" alt="Pelusa">
  </div>
</div>

<script>
  const GIF = "__GIF__", PNG = "__PNG__", DUR = __DUR__, DATOS = __DATOS__;
  const char = document.getElementById("char"), txt = document.getElementById("txt"),
        label = document.getElementById("label");
  let tw, playing = false, last = -1;

  txt.innerHTML = __INTRO__;

  function escribir(t) {
    clearInterval(tw);
    txt.textContent = "";
    let i = 0;
    tw = setInterval(() => {
      txt.textContent += t[i++];
      if (i >= t.length) clearInterval(tw);
    }, 22);
  }

  char.onclick = () => {
    if (!playing) {
      playing = true;
      char.src = GIF;
      setTimeout(() => { char.src = PNG; playing = false; }, DUR);
    }
    let n;
    // evita repetir el mismo dato dos veces seguidas
    do { n = Math.floor(Math.random() * DATOS.length); } while (n === last);
    last = n;
    label.textContent = "💡 Dato curioso";
    escribir(DATOS[n]);
  };
</script>
"""

reemplazos = {
    "__GIF__": gif, "__PNG__": png, "__DUR__": str(DUR_GIF),
    "__DATOS__": json.dumps(DATOS, ensure_ascii=False),
    "__INTRO__": json.dumps(INTRO, ensure_ascii=False),
}
for k, v in reemplazos.items():
    HTML = HTML.replace(k, v)

components.html(HTML, height=470)