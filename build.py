#!/usr/bin/env python3
"""
Gera as páginas estáticas do site AJ Estética Beauty dentro de ./site
Uso:  python3 build.py
Edite textos, telefones e endereço nos blocos CONFIG e CONTEÚDO abaixo.
"""
import os
from urllib.parse import quote

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")

# ============================== CONFIG ==============================
WA_NUMBER = "5534912345678"                      # +55 34 91234-5678
PHONE_LABEL = "+55 34 91234-5678"
EMAIL = "contato@ajesteticabeauty.com.br"        # trocar pelo e-mail real
ADDRESS = "Centro, Uberlândia – MG"              # incluir rua e número quando definir
HOURS = [("Segunda a sexta", "9h às 18h"), ("Sábado", "9h às 13h")]
INSTAGRAM = "https://www.instagram.com/ajesteticabeauty?stkn=MWI2N2Nsb25tYTFxbA=="
MAPS_LINK = "https://www.google.com/maps/search/?api=1&query=" + quote("Centro, Uberlândia - MG")
WA_TEXT = "Olá, Dra. Ana Júlia! Gostaria de agendar uma avaliação."
WA = f"https://wa.me/{WA_NUMBER}?text={quote(WA_TEXT)}"

MAP_IFRAME = ('<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d7548.67223767131!2d-48.281305132744976!3d-18.91651087872586!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94a445aada9bfd7f%3A0x49cb222d8986cde3!2sCentro%2C%20Uberl%C3%A2ndia%20-%20MG!5e0!3m2!1spt-BR!2sbr!4v1791438851136!5m2!1spt-BR!2sbr" '
              'width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" title="Mapa com a localização do AJ Estética Beauty"></iframe>')

# Foto verificada (Unsplash, licença livre). Se o link falhar, o espaço mostra o placeholder.
UNSPLASH_FACIAL = "https://unsplash.com/photos/Xxs9WvkUPLo/download?force=true&w=1400"

# ============================== ÍCONES ==============================
def svg(paths, cls=""):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{paths}</svg>'

ICON = {
    "massagem": '<path d="M12 4c1.5 2.2 2.5 4 2.5 6a2.5 2.5 0 01-5 0c0-2 1-3.8 2.5-6z"/><path d="M5 10c2 .2 3.6 1.2 4.5 3M19 10c-2 .2-3.6 1.2-4.5 3M3.5 16c2.5-1.4 5.2-1.2 8.5 1.5 3.3-2.7 6-2.9 8.5-1.5"/>',
    "limpeza": '<path d="M11 3.5c3.2 3.8 5 6.4 5 9a5 5 0 01-10 0c0-2.6 1.8-5.2 5-9z"/><path d="M19 3.5v4M17 5.5h4"/>',
    "estrias": '<path d="M4 7c2.5-2 5.5 2 8 0s5.5 2 8 0M4 12c2.5-2 5.5 2 8 0s5.5 2 8 0M4 17c2.5-2 5.5 2 8 0s5.5 2 8 0"/>',
    "botox": '<path d="M4 20l5-5M14 4l6 6M12 6l6 6-7 7-6-6 7-7zM9 9l6 6"/>',
    "harmonizacao": '<path d="M12 3c-4 0-6 3-6 7 0 5 2.5 9 6 11 3.5-2 6-6 6-11 0-4-2-7-6-7z"/><path d="M9.5 11h.01M14.5 11h.01M10 15c1.2.8 2.8.8 4 0"/>',
    "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    "pin": '<path d="M12 21s-6.5-5.6-6.5-11a6.5 6.5 0 0113 0c0 5.4-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.3"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "phone": '<path d="M5 4h3.5l1.5 4-2 1.5a11 11 0 006 6L15.5 13.5 19.5 15v3.5a1.5 1.5 0 01-1.5 1.5A15 15 0 013.5 5.5 1.5 1.5 0 015 4z"/>',
    "mail": '<rect x="3.5" y="5.5" width="17" height="13" rx="2"/><path d="M4 7l8 6 8-6"/>',
    "shield": '<path d="M12 3l7 3v5.5c0 4.5-3 7.8-7 9.5-4-1.7-7-5-7-9.5V6l7-3z"/><path d="M9 12l2.2 2.2L15.5 10"/>',
    "clipboard": '<rect x="6" y="4.5" width="12" height="16" rx="2"/><path d="M9.5 4.5h5v2.5h-5zM9 12h6M9 16h4"/>',
    "leaf": '<path d="M5 19c0-8 5-13 14-14 0 9-5 14-13 14"/><path d="M5 19c2-4 5-6.5 9-8"/>',
    "heart": '<path d="M12 20s-7.5-4.6-7.5-10A4.3 4.3 0 0112 7.5 4.3 4.3 0 0119.5 10c0 5.4-7.5 10-7.5 10z"/>',
}
WA_ICON = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>'
IG_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r=".8" fill="currentColor"/></svg>'
STAR = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.8l2.8 5.8 6.4.9-4.6 4.5 1.1 6.3L12 17.2l-5.7 3.1 1.1-6.3L2.8 9.5l6.4-.9L12 2.8z"/></svg>'
CHEV = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>'

def icon(name, cls=""):
    return svg(ICON[name], cls)

# ============================== TRATAMENTOS ==============================
TREATMENTS = [
    {
        "slug": "massagem", "file": "massagem.html", "nome": "Massagem", "icon": "massagem",
        "resumo": "Alivia a tensão muscular e devolve a sensação de leveza.",
        "tagline": "Manobras escolhidas para o que o seu corpo está pedindo: relaxar, aliviar a tensão ou estimular a circulação.",
        "sobre": [
            "A massagem é feita com manobras manuais e cremes ou óleos escolhidos conforme o objetivo da sessão: soltar a musculatura, estimular a circulação ou trabalhar o contorno do corpo.",
            "Antes de começar, a Dra. Ana Júlia conversa com você sobre dores, rotina e histórico de saúde. É essa conversa que define o tipo de massagem, a região e a pressão usada.",
        ],
        "indicado": [
            "Quem sente tensão no pescoço, nos ombros e nas costas por passar o dia sentado ou sob estresse.",
            "Quem tem sensação de peso e inchaço nas pernas ao fim do dia.",
            "Quem quer complementar o cuidado com o contorno corporal.",
            "Quem precisa de uma pausa de verdade na semana.",
        ],
        "atencao": "Febre, infecção de pele na região, trombose, gravidez sem liberação médica e lesões recentes pedem cuidado. Informe tudo na avaliação; em alguns casos a sessão é adiada ou adaptada.",
        "passos": [
            ("Conversa e avaliação", "Você conta onde sente desconforto e quais são seus objetivos. Registramos histórico de saúde e restrições."),
            ("Preparo", "Posicionamento confortável, toalhas para cobrir as áreas fora de trabalho e temperatura agradável na sala."),
            ("Massagem", "Manobras com ritmo e pressão ajustados ao seu corpo, avisando sempre que algo incomodar."),
            ("Finalização", "Alongamento leve, um copo de água e orientações para os próximos dias."),
        ],
        "duracao": [
            ("Sessão", "De 50 a 60 minutos, incluindo a conversa inicial."),
            ("Efeito", "O alívio é sentido logo depois. Para tensão acumulada, o benefício dura alguns dias."),
            ("Frequência", "Em geral a cada 15 dias. A avaliação indica o intervalo ideal para o seu caso."),
        ],
        "pos": [
            "Beba água ao longo do dia.",
            "Evite exercício intenso nas 24 horas seguintes.",
            "Fuja de sauna e calor excessivo no mesmo dia.",
            "Prefira refeições leves nas horas seguintes.",
            "Se sentir dor que não passa, fale com a Dra. Ana Júlia pelo WhatsApp.",
        ],
        "faq": [
            ("A massagem dói?", "Não deveria. A pressão é ajustada durante a sessão e você pode pedir para aliviar ou reforçar a qualquer momento. Pontos de tensão podem incomodar um pouco, mas o desconforto precisa ser tolerável."),
            ("A massagem modeladora emagrece?", "Não. Ela estimula a circulação e ajuda no aspecto do contorno, mas não substitui alimentação e atividade física. Se alguém prometer perda de peso só com massagem, desconfie."),
            ("Posso fazer durante a gravidez?", "Só com liberação do seu obstetra, e a técnica precisa ser adaptada. Conte sobre a gestação ao agendar."),
            ("Preciso ficar sem roupa?", "Você usa roupa íntima ou uma peça descartável e fica coberta por toalhas. Só a área trabalhada fica descoberta."),
            ("Qual a diferença entre relaxante e modeladora?", "A relaxante prioriza o alívio da tensão, com ritmo mais lento. A modeladora usa manobras mais firmes e vigorosas, voltadas à circulação e ao contorno. Na avaliação definimos a que faz sentido para você."),
        ],
        "hero_img": "massagem-hero", "gal": ["massagem-1", "massagem-2", "massagem-3"],
    },
    {
        "slug": "limpeza-de-pele", "file": "limpeza-de-pele.html", "nome": "Limpeza de pele", "icon": "limpeza",
        "resumo": "Remove impurezas e cravos, deixando a pele mais uniforme.",
        "tagline": "Higienização profunda feita em etapas, com produtos escolhidos para o seu tipo de pele.",
        "sobre": [
            "A limpeza de pele remove células mortas, excesso de oleosidade e cravos que a rotina em casa não alcança. O resultado é uma pele mais lisa, com poros menos obstruídos e melhor absorção dos cosméticos.",
            "Cada etapa muda conforme o tipo de pele. Pele sensível, por exemplo, recebe ativos mais suaves e extração mais cuidadosa do que uma pele oleosa com muitos cravos.",
        ],
        "indicado": [
            "Pele oleosa ou mista, com cravos e poros aparentes.",
            "Pele opaca, áspera ou com textura irregular.",
            "Quem usa maquiagem com frequência.",
            "Quem quer manter a pele em dia com uma rotina de manutenção.",
        ],
        "atencao": "Em acne inflamatória intensa, uso de isotretinoína ou doenças de pele ativas, a limpeza pode não ser indicada. Nesses casos a avaliação recomenda acompanhamento com dermatologista antes.",
        "passos": [
            ("Avaliação da pele", "Observamos o tipo de pele, o grau de oleosidade, sensibilidades e o que você já usa em casa."),
            ("Higienização e esfoliação", "Remoção de maquiagem e resíduos, seguida de esfoliação adequada ao seu tipo de pele."),
            ("Preparo e extração", "A pele é amolecida para facilitar a saída dos cravos. A extração é feita com técnica e materiais higienizados, sem forçar."),
            ("Máscara e proteção", "Máscara calmante, hidratação e protetor solar para encerrar a sessão."),
        ],
        "duracao": [
            ("Sessão", "De 60 a 90 minutos, conforme a necessidade da pele."),
            ("Recuperação", "Um pouco de vermelhidão é comum e costuma passar em algumas horas, às vezes em até 24."),
            ("Frequência", "Em média a cada 30 a 45 dias, que é o tempo de renovação da pele."),
        ],
        "pos": [
            "Evite maquiagem nas primeiras 24 horas.",
            "Use protetor solar todos os dias e reaplique durante o dia.",
            "Não esfolie a pele em casa por 3 a 5 dias.",
            "Não mexa em cravos ou lesões, para evitar manchas e inflamação.",
            "Evite sol direto, piscina e sauna por 48 horas.",
        ],
        "faq": [
            ("A limpeza de pele dói?", "Há um desconforto leve em alguns momentos, principalmente na extração. Se algo incomodar além do tolerável, é só avisar que a técnica é ajustada."),
            ("Fico vermelha depois?", "Pode ficar, principalmente em peles claras e sensíveis. Normalmente some em algumas horas. A máscara calmante no fim da sessão ajuda nisso."),
            ("Com que frequência devo fazer?", "Para a maioria das peles, a cada 30 a 45 dias. Pele muito oleosa pode precisar de intervalo menor, e pele sensível de um maior."),
            ("Posso fazer limpeza de pele grávida?", "Pode, com produtos compatíveis com a gestação. Avise ao agendar para que a avaliação já considere isso."),
            ("Quando vejo o resultado?", "A pele fica mais limpa e macia já no primeiro dia. Para melhora de textura e controle de oleosidade, o ideal é manter as sessões regulares."),
        ],
        "hero_img": "limpeza-hero", "gal": ["limpeza-1", "limpeza-2", "limpeza-3"],
    },
    {
        "slug": "tratamento-para-estrias", "file": "tratamento-para-estrias.html", "nome": "Tratamento para estrias", "icon": "estrias",
        "resumo": "Suaviza a aparência das estrias e melhora a textura.",
        "tagline": "Um protocolo montado a partir do tipo e da idade das suas estrias, com expectativa realista desde a primeira conversa.",
        "sobre": [
            "Estrias são marcas que surgem quando as fibras da pele se rompem, geralmente por crescimento, gravidez, variação de peso ou treino. As recentes, rosadas ou avermelhadas, respondem melhor ao tratamento. As antigas, esbranquiçadas, melhoram em textura e uniformidade, mas não desaparecem por completo.",
            "Por isso o protocolo não é igual para todo mundo. Na avaliação, a Dra. Ana Júlia analisa as estrias, define as técnicas e os ativos e explica o que é possível esperar do seu caso.",
        ],
        "indicado": [
            "Quem tem estrias recentes e quer agir enquanto respondem melhor.",
            "Quem tem estrias antigas e busca melhorar a textura e o aspecto.",
            "Quem passou por gravidez, mudança de peso ou crescimento rápido.",
            "Quem aceita seguir um protocolo de várias sessões.",
        ],
        "atencao": "Gravidez, amamentação com restrições, doenças de pele ativas na região e uso de alguns medicamentos podem limitar as técnicas. Conte seu histórico completo na avaliação.",
        "passos": [
            ("Avaliação e registro", "Analisamos cor, profundidade e extensão das estrias. Com a sua autorização, tiramos fotos para comparar ao longo do protocolo."),
            ("Preparo da área", "Higienização e preparo da pele para receber os ativos e as técnicas escolhidas."),
            ("Aplicação do protocolo", "As técnicas definidas na avaliação são aplicadas na área, com intensidade ajustada à sua sensibilidade."),
            ("Finalização e plano em casa", "Hidratação, proteção e orientação do que usar entre as sessões para sustentar o resultado."),
        ],
        "duracao": [
            ("Sessão", "De 45 a 60 minutos, dependendo da área tratada."),
            ("Protocolo", "Costuma pedir várias sessões, com intervalo de 15 a 30 dias. O número exato sai da avaliação."),
            ("Resultado", "Gradual. Comparamos as fotos ao longo do protocolo para ajustar o que for preciso."),
        ],
        "pos": [
            "Hidrate a área duas vezes ao dia, com o produto indicado.",
            "Proteja a região do sol com roupa ou protetor solar.",
            "Evite banhos muito quentes nas primeiras 24 horas.",
            "Não esfolie a área por alguns dias após a sessão.",
            "Siga o cuidado em casa combinado, porque ele faz diferença no resultado.",
        ],
        "faq": [
            ("As estrias somem de vez?", "Não é possível prometer isso. O que o tratamento faz é suavizar cor e textura, e isso varia com a idade da estria, o tipo de pele e a constância no protocolo."),
            ("Funciona em estria branca?", "Funciona de forma mais discreta do que nas recentes. Há melhora em textura e uniformidade, e na avaliação você vê qual é o ganho realista no seu caso."),
            ("Quantas sessões são necessárias?", "Depende da extensão e da idade das estrias. A avaliação define um número inicial, que pode mudar conforme a resposta da sua pele."),
            ("O tratamento dói?", "A sensação varia por técnica e por região. A intensidade é ajustada para que o procedimento seja confortável."),
            ("Posso fazer durante a gravidez?", "Em geral não é indicado. Para a gestação, o foco é prevenção com hidratação, e o tratamento fica para depois."),
        ],
        "hero_img": "estrias-hero", "gal": ["estrias-1", "estrias-2", "estrias-3"],
    },
]
SOON = [
    ("botox", "Botox", "Suaviza linhas de expressão com resultado natural."),
    ("harmonizacao", "Harmonização facial", "Equilibra os traços do rosto, sem exagero."),
]

# ============================== PARTES COMUNS ==============================
def ph(slot, label, shape="43", extra="", alt="", src=None):
    """Espaço de imagem. Coloque o arquivo em site/assets/img/<slot>.jpg para trocar a foto."""
    path = src or f"assets/img/{slot}.jpg"
    return (f'<div class="ph ph--{shape} {extra}" data-label="{label}">'
            f'<img src="{path}" alt="{alt}" loading="lazy" onerror="this.remove()"></div>')

def nav_links(active):
    def a(href, label, key):
        cur = ' aria-current="page"' if active == key else ""
        return f'<li><a href="{href}"{cur}>{label}</a></li>'
    sub = "".join(f'<li><a href="{t["file"]}"{" aria-current=page" if active == t["slug"] else ""}>{t["nome"]}</a></li>' for t in TREATMENTS)
    sub += "".join(f'<li class="soon"><span>{n}</span><span>em breve</span></li>' for _, n, _ in SOON)
    trat_cur = ' aria-current="page"' if active in [t["slug"] for t in TREATMENTS] else ""
    return (
        a("index.html", "Home", "home")
        + f'<li class="has-sub"><button class="sub-toggle" aria-expanded="false" aria-controls="sub"{trat_cur}>Tratamentos {CHEV}</button><ul class="sub" id="sub">{sub}</ul></li>'
        + a("sobre.html", "Sobre", "sobre")
        + a("depoimentos.html", "Depoimentos", "depoimentos")
        + a("contato.html", "Contato", "contato")
    )

def header(active):
    return f'''<a class="skip" href="#conteudo">Ir para o conteúdo</a>
<header class="site-header">
  <div class="container header__in">
    <a class="brand" href="index.html" aria-label="AJ Estética Beauty, página inicial">
      <img src="assets/logo.png" alt="" width="52" height="52"><span>AJ Estética Beauty</span>
    </a>
    <nav class="nav" id="nav" aria-label="Principal"><ul>{nav_links(active)}</ul></nav>
    <div class="header__actions">
      <button class="icon-btn theme-toggle" type="button" aria-label="Alternar entre tema claro e escuro">
        <svg class="i-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 14.5A8 8 0 019.5 4a8 8 0 1010.5 10.5z"/></svg>
        <svg class="i-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.3 5.3l1.4 1.4M17.3 17.3l1.4 1.4M5.3 18.7l1.4-1.4M17.3 6.7l1.4-1.4"/></svg>
      </button>
      <a class="btn btn--primary btn--sm" href="{WA}" target="_blank" rel="noopener">Agendar consulta</a>
      <button class="icon-btn menu-toggle" type="button" aria-label="Abrir menu" aria-expanded="false" aria-controls="nav">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
      </button>
    </div>
  </div>
</header>'''

def footer():
    trat = "".join(f'<li><a href="{t["file"]}">{t["nome"]}</a></li>' for t in TREATMENTS)
    trat += "".join(f'<li>{n} <span style="opacity:.6">(em breve)</span></li>' for _, n, _ in SOON)
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="foot-grid">
      <div class="foot-brand">
        <img src="assets/logo.png" alt="AJ Estética Beauty" width="72" height="72">
        <p>Estética com avaliação, protocolo individual e atendimento com hora marcada em Uberlândia.</p>
      </div>
      <div>
        <h4>Navegação</h4>
        <ul><li><a href="index.html">Home</a></li><li><a href="sobre.html">Sobre</a></li><li><a href="depoimentos.html">Depoimentos</a></li><li><a href="contato.html">Contato</a></li></ul>
      </div>
      <div>
        <h4>Tratamentos</h4>
        <ul>{trat}</ul>
      </div>
      <div>
        <h4>Contato</h4>
        <ul>
          <li><a href="tel:+{WA_NUMBER}">{PHONE_LABEL}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>{ADDRESS}</li>
          <li>Seg a sex, 9h às 18h<br>Sáb, 9h às 13h</li>
        </ul>
        <div class="social">
          <a href="{INSTAGRAM}" target="_blank" rel="noopener" aria-label="Instagram do AJ Estética Beauty">{IG_ICON}</a>
          <a href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{WA_ICON}</a>
        </div>
      </div>
    </div>
    <div class="foot-bottom"><span>© 2026 Dra. Ana Júlia — Todos os direitos reservados.</span><span>AJ Estética Beauty</span></div>
  </div>
</footer>
<a class="wa-float" href="{WA}" target="_blank" rel="noopener" aria-label="Falar com a Dra. Ana Júlia no WhatsApp">{WA_ICON}</a>
<script src="js/main.js" defer></script>'''

def page(file, title, desc, body, active, extra_head=""):
    html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#CBAE99">
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Jost:wght@400;500;600&display=swap" rel="stylesheet">
<script>try{{var t=localStorage.getItem('aj-theme')||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');document.documentElement.dataset.theme=t}}catch(e){{document.documentElement.dataset.theme='light'}}</script>
<link rel="stylesheet" href="css/style.css">
{extra_head}
</head>
<body>
{header(active)}
<main id="conteudo">
{body}
</main>
{footer()}
</body>
</html>
'''
    with open(os.path.join(OUT, file), "w", encoding="utf-8") as f:
        f.write(html)
    print("ok", file)

def pair(key, nome, legenda="", chip=True):
    cap = f'<figcaption><strong>{nome}</strong>{(" — " + legenda) if legenda else ""}</figcaption>'
    return f'''<figure class="pair">
  <div class="pair__imgs">
    <div style="position:relative">{ph(key + "-antes", "Foto antes", "34")}<span class="pair__chip">Antes</span></div>
    <div style="position:relative">{ph(key + "-depois", "Foto depois", "34")}<span class="pair__chip">Depois</span></div>
  </div>{cap}
</figure>'''

def cta_band(title, text, cls=""):
    return f'''<section class="sec cta-band {cls}">
  <div class="container">
    <h2>{title}</h2>
    <p class="lead">{text}</p>
    <a class="btn btn--primary" href="{WA}" target="_blank" rel="noopener">{WA_ICON} Agendar pelo WhatsApp</a>
  </div>
</section>'''

def map_section(cls="sec--nude"):
    hrs = "".join(f"<li><span style='display:flex;justify-content:space-between;gap:20px;width:100%'><b style='display:inline'>{d}</b><span>{h}</span></span></li>" for d, h in HOURS)
    return f'''<section class="sec {cls}" id="localizacao">
  <div class="container map-wrap">
    <div>
      <h2>Onde fica o espaço</h2>
      <p class="lead">O atendimento é com hora marcada, no centro de Uberlândia. O endereço completo é enviado na confirmação do agendamento.</p>
      <ul class="info-list">
        <li>{icon("pin")}<div><b>Endereço</b><span>{ADDRESS}</span></div></li>
        <li>{icon("clock")}<div><b>Horário de atendimento</b><span>Segunda a sexta, 9h às 18h<br>Sábado, 9h às 13h</span></div></li>
      </ul>
      <a class="btn btn--primary" href="{MAPS_LINK}" target="_blank" rel="noopener">Abrir no Google Maps</a>
    </div>
    <div class="map-frame">{MAP_IFRAME}</div>
  </div>
</section>'''

# ============================== HOME ==============================
def build_home():
    cards = ""
    for t in TREATMENTS:
        cards += f'''<a class="card" href="{t["file"]}">
  <div class="card__icon">{icon(t["icon"])}</div>
  <h3>{t["nome"]}</h3><p>{t["resumo"]}</p><span class="go">Ver tratamento</span></a>'''
    for key, nome, resumo in SOON:
        cards += f'''<div class="card card--soon">
  <div class="card__icon">{icon(key)}</div>
  <h3>{nome}</h3><p>{resumo}</p><span class="tag">Em breve</span></div>'''

    marquee_items = "".join(
        pair(k, n, l) for k, n, l in [
            ("home-limpeza", "Limpeza de pele", "pele mais uniforme"),
            ("home-estrias", "Tratamento para estrias", "textura e cor suavizadas"),
            ("home-massagem", "Massagem modeladora", "contorno e circulação"),
            ("home-limpeza2", "Limpeza de pele", "poros desobstruídos"),
            ("home-estrias2", "Tratamento para estrias", "protocolo completo"),
        ])
    studio = "".join(
        f'<button class="studio__item" type="button" aria-label="Ampliar foto do estúdio {i}">{ph(f"studio-{i}", lab, "sq", alt="Ambiente do estúdio AJ Estética Beauty", src=(UNSPLASH_FACIAL if i == 1 else None))}</button>'
        for i, lab in enumerate(["Foto do estúdio: sala de atendimento", "Foto do estúdio: maca e iluminação", "Foto do estúdio: recepção", "Foto do estúdio: produtos", "Foto do estúdio: detalhe", "Foto do estúdio: ambiente geral"], 1))

    body = f'''
<section class="hero">
  <div class="container hero__grid">
    <div>
      <span class="rule"></span>
      <h1>Estética com critério para a sua pele e o seu corpo</h1>
      <p class="lead">Atendimento da Dra. Ana Júlia, formada em Estética e Cosmética. Toda sessão começa com avaliação e termina com orientação clara para o cuidado em casa.</p>
      <div class="hero__cta">
        <a class="btn btn--primary" href="{WA}" target="_blank" rel="noopener">{WA_ICON} Agendar pelo WhatsApp</a>
        <a class="btn btn--ghost" href="#tratamentos">Conhecer os tratamentos</a>
      </div>
      <div class="hero__facts">
        <span>Atendimento com hora marcada, no Centro de Uberlândia</span>
        <span>Segunda a sexta, 9h às 18h. Sábado, 9h às 13h.</span>
      </div>
    </div>
    <div class="hero__photo">{ph("doutora-hero", "Foto da Dra. Ana Júlia", "45", "ph--arch", "Dra. Ana Júlia Silva Gonçalves")}</div>
  </div>
</section>

<section class="sec sec--nude" id="sobre-resumo">
  <div class="container split">
    <div class="split__media">{ph("doutora-sobre", "Foto da Dra. Ana Júlia em atendimento", "34", "", "Dra. Ana Júlia em atendimento")}</div>
    <div>
      <h2>Dra. Ana Júlia Silva Gonçalves</h2>
      <p class="lead">Formada em Estética e Cosmética, ela conduz cada atendimento do começo ao fim: avalia a pele, explica o que será feito e monta o protocolo com você.</p>
      <ul class="facts">
        <li><strong>Formação</strong><span>Estética e Cosmética</span></li>
        <li><strong>Atendimento</strong><span>Individual, com hora marcada</span></li>
        <li><strong>Abordagem</strong><span>Avaliação antes de qualquer procedimento</span></li>
      </ul>
      <a class="btn btn--primary" href="sobre.html">Conhecer a trajetória</a>
    </div>
  </div>
</section>

<section class="sec" id="tratamentos">
  <div class="container">
    <div class="sec-head"><h2>Tratamentos</h2><p class="lead">Cada um começa por uma avaliação, para o protocolo caber na sua pele e não o contrário.</p></div>
    <div class="cards">{cards}</div>
  </div>
</section>

<section class="sec sec--nude" id="resultados">
  <div class="container"><div class="sec-head"><h2>Antes e depois</h2><p class="lead">Resultados de clientes atendidas no espaço. Cada pele responde de um jeito, e as fotos mostram isso.</p></div></div>
  <div class="marquee" aria-label="Galeria de antes e depois em movimento"><div class="marquee__track">{marquee_items}{marquee_items}</div></div>
  <div class="container gallery-tools">
    <p class="note">Imagens publicadas com autorização das clientes. Os resultados variam de pessoa para pessoa.</p>
    <button class="btn btn--ghost btn--sm" type="button" data-marquee-toggle aria-pressed="false">Pausar movimento</button>
  </div>
</section>

<section class="sec" id="estudio">
  <div class="container">
    <div class="sec-head"><h2>O estúdio</h2><p class="lead">Um espaço reservado e silencioso, pensado para que você consiga relaxar desde a chegada.</p></div>
    <div class="studio">{studio}</div>
  </div>
</section>
<dialog class="lightbox" id="lightbox" aria-label="Foto ampliada"><img src="" alt=""><button class="icon-btn" type="button" aria-label="Fechar" style="background:var(--bg)"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg></button></dialog>

{map_section()}
'''
    ld = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"BeautySalon","name":"AJ Estética Beauty","telephone":"+5534912345678","address":{"@type":"PostalAddress","addressLocality":"Uberlândia","addressRegion":"MG","addressCountry":"BR"},"openingHours":["Mo-Fr 09:00-18:00","Sa 09:00-13:00"],"sameAs":["https://www.instagram.com/ajesteticabeauty"]}</script>'''
    page("index.html", "AJ Estética Beauty | Estética em Uberlândia com a Dra. Ana Júlia",
         "Massagem, limpeza de pele e tratamento para estrias em Uberlândia, com avaliação individual e atendimento da Dra. Ana Júlia.",
         body, "home", ld)

# ============================== TRATAMENTO ==============================
def build_treatment(t):
    sobre = "".join(f"<p>{p}</p>" for p in t["sobre"])
    indicado = "".join(f"<li>{icon('check')}<span>{i}</span></li>" for i in t["indicado"])
    passos = "".join(f"<li><div><h3>{h}</h3><p>{p}</p></div></li>" for h, p in t["passos"])
    dur = "".join(f"<div><h3>{h}</h3><p>{p}</p></div>" for h, p in t["duracao"])
    pos = "".join(f"<li>{icon('check')}<span>{i}</span></li>" for i in t["pos"])
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in t["faq"])
    gal = "".join(pair(k, t["nome"], f"caso {i}") for i, k in enumerate(t["gal"], 1))
    hero_src = UNSPLASH_FACIAL if t["slug"] == "limpeza-de-pele" else None

    body = f'''
<section class="page-hero">
  <div class="container hero__grid">
    <div>
      <span class="rule"></span>
      <h1>{t["nome"]}</h1>
      <p class="lead">{t["tagline"]}</p>
      <div class="hero__cta"><a class="btn btn--primary" href="{WA}" target="_blank" rel="noopener">{WA_ICON} Agendar avaliação</a><a class="btn btn--ghost" href="#perguntas">Tirar dúvidas</a></div>
    </div>
    <div class="hero__photo">{ph(t["hero_img"], "Foto do tratamento", "45", "ph--arch", t["nome"], hero_src)}</div>
  </div>
</section>

<section class="sec sec--nude" id="antes-depois">
  <div class="container">
    <div class="sec-head"><h2>Antes e depois</h2><p class="lead">Casos atendidos no espaço, publicados com autorização.</p></div>
    <div class="pair-grid">{gal}</div>
    <p class="note" style="margin-top:24px">Os resultados variam conforme a pele, a constância no cuidado e o histórico de cada pessoa.</p>
  </div>
</section>

<section class="sec" id="sobre-tratamento">
  <div class="container split split--rev">
    <div><h2>Sobre o tratamento</h2>{sobre}</div>
    <div class="callout" style="margin:0"><strong>Antes de agendar</strong><br>A primeira conversa é uma avaliação. Você só segue para o procedimento depois de saber o que será feito, quanto tempo leva e o que esperar.</div>
  </div>
</section>

<section class="sec sec--nude" id="indicacao">
  <div class="container split">
    <div><h2>Para quem é indicado</h2><ul class="checks">{indicado}</ul></div>
    <div class="callout" style="margin:0"><strong>Quando pede cautela</strong><br>{t["atencao"]}</div>
  </div>
</section>

<section class="sec" id="como-e-feito">
  <div class="container"><div class="sec-head"><h2>Como é feito</h2></div><ol class="steps">{passos}</ol></div>
</section>

<section class="sec sec--nude" id="duracao">
  <div class="container"><div class="sec-head"><h2>Quanto tempo dura</h2></div><div class="duration">{dur}</div></div>
</section>

<section class="sec" id="cuidados">
  <div class="container split split--rev">
    <div><h2>Cuidados depois do tratamento</h2><p class="lead">O que você faz nos dias seguintes pesa no resultado.</p></div>
    <ul class="checks">{pos}</ul>
  </div>
</section>

<section class="sec sec--nude" id="perguntas">
  <div class="container"><div class="sec-head"><h2>Perguntas frequentes</h2></div><div class="faq">{faq}</div></div>
</section>

{cta_band("Quer saber se é indicado para você?", "Mande uma mensagem e agende sua avaliação com a Dra. Ana Júlia.")}
'''
    page(t["file"], f'{t["nome"]} em Uberlândia | AJ Estética Beauty',
         f'{t["nome"]} com avaliação individual na AJ Estética Beauty, em Uberlândia. Veja para quem é indicado, como é feito e os cuidados.',
         body, t["slug"])

# ============================== SOBRE ==============================
def build_about():
    body = f'''
<section class="page-hero">
  <div class="container hero__grid">
    <div>
      <span class="rule"></span>
      <h1>Ana Júlia Silva Gonçalves</h1>
      <p class="lead">Esteticista, formada em Estética e Cosmética. Atende em Uberlândia com avaliação individual e conversa franca sobre o que cada tratamento entrega.</p>
      <a class="btn btn--primary" href="{WA}" target="_blank" rel="noopener">{WA_ICON} Agendar avaliação</a>
    </div>
    <div class="hero__photo">{ph("doutora-sobre-hero", "Foto da Dra. Ana Júlia", "45", "ph--arch", "Dra. Ana Júlia Silva Gonçalves")}</div>
  </div>
</section>

<section class="sec sec--nude" id="trajetoria">
  <div class="container">
    <div class="sec-head"><h2>Trajetória</h2></div>
    <ol class="timeline">
      <li><h3>Formação</h3><p>Graduou-se em Estética e Cosmética, onde estudou anatomia e fisiologia da pele, cosmetologia e biossegurança. É a base de tudo o que faz na cabine.</p></li>
      <li><h3>Primeiros atendimentos</h3><p>Ao atender, notou que pele tratada sem avaliação prévia dá resultado irregular. Passou a não começar nenhum protocolo sem conversa e análise.</p></li>
      <li><h3>AJ Estética Beauty</h3><p>Abriu o próprio espaço para atender com tempo, hora marcada e um ambiente reservado, sem pressa entre uma cliente e outra.</p></li>
      <li><h3>Hoje</h3><p>Atende em Uberlândia e segue estudando. Novos procedimentos só entram no espaço depois de formação específica e respaldo técnico.</p></li>
    </ol>
  </div>
</section>

<section class="sec" id="diferencial">
  <div class="container">
    <div class="sec-head"><h2>O que a diferencia</h2><p class="lead">Nada disso é sofisticado. Só é feito sempre, em todo atendimento.</p></div>
    <div class="cols-2">
      <div class="item"><h3>Avaliação antes de tudo</h3><p>Ninguém recebe procedimento no primeiro minuto. Primeiro vem a conversa, o histórico e a análise da pele ou da região.</p></div>
      <div class="item"><h3>Protocolo sob medida</h3><p>Sem pacotes prontos. Técnicas, ativos e intervalo entre as sessões são definidos para o seu caso.</p></div>
      <div class="item"><h3>Expectativa realista</h3><p>Se um tratamento não é o mais indicado, ou se o resultado esperado não é possível, você ouve isso antes de pagar.</p></div>
      <div class="item"><h3>Acompanhamento depois da sessão</h3><p>Dúvidas sobre os cuidados em casa ou sobre uma reação da pele podem ser tiradas pelo WhatsApp.</p></div>
    </div>
  </div>
</section>

<section class="sec sec--nude" id="seguranca">
  <div class="container">
    <div class="sec-head"><h2>Saúde e segurança vêm primeiro</h2><p class="lead">São os dois pilares de todo procedimento feito no espaço. Se houver dúvida sobre a segurança, a sessão não acontece.</p></div>
    <div class="pillars">
      <div class="pillar"><div class="card__icon">{icon("clipboard")}</div><h3>Anamnese completa</h3><p>Histórico de saúde, alergias e medicamentos em uso são registrados antes de começar.</p></div>
      <div class="pillar"><div class="card__icon">{icon("shield")}</div><h3>Biossegurança</h3><p>Materiais descartáveis, instrumentos esterilizados e ambiente higienizado a cada atendimento.</p></div>
      <div class="pillar"><div class="card__icon">{icon("leaf")}</div><h3>Produtos regularizados</h3><p>Cosméticos e equipamentos com registro, de marcas conhecidas e dentro da validade.</p></div>
      <div class="pillar"><div class="card__icon">{icon("heart")}</div><h3>Indicação responsável</h3><p>Quando o caso pede avaliação médica, você é orientada a procurar o profissional adequado.</p></div>
    </div>
  </div>
</section>

{cta_band("Vamos conversar sobre o seu caso", "A primeira conversa é para entender o que você busca. O procedimento vem depois.")}
'''
    page("sobre.html", "Sobre a Dra. Ana Júlia | AJ Estética Beauty",
         "Conheça a trajetória da Dra. Ana Júlia Silva Gonçalves, esteticista formada em Estética e Cosmética, e como ela trabalha saúde e segurança em cada procedimento.",
         body, "sobre")

# ============================== DEPOIMENTOS ==============================
QUOTES = [
    ("Fiz a limpeza de pele sem esperar muito e saí surpresa. Ela me explicou cada etapa e a pele ficou calma, sem aquela vermelhidão forte que eu tinha em outros lugares.", "Mariana R.", "Limpeza de pele"),
    ("Tenho estrias desde a adolescência e já tinha ouvido muita promessa. A Ana Júlia foi direta sobre o que dava para melhorar. Seguindo o protocolo, a textura mudou bem.", "Carolina S.", "Tratamento para estrias"),
    ("A massagem foi o melhor momento da minha semana. Ela perguntou onde eu sentia mais dor e ajustou a pressão o tempo todo. Voltei no mês seguinte.", "Fernanda L.", "Massagem"),
    ("Gostei de ser avaliada antes de qualquer coisa. Ela chegou a me orientar a adiar um procedimento por causa de um remédio que eu usava. Isso me deu confiança.", "Patrícia M.", "Limpeza de pele"),
    ("O espaço é tranquilo e o horário é respeitado. Não fico esperando nem sinto que estou sendo apressada. Indico para as minhas amigas.", "Juliana A.", "Massagem"),
    ("Depois da gravidez, minhas estrias me incomodavam muito. Ela montou o protocolo, passou os cuidados para fazer em casa e acompanhou pelo WhatsApp.", "Renata T.", "Tratamento para estrias"),
]

def build_testimonials():
    cards = "".join(f'''<figure class="quote"><div class="stars" role="img" aria-label="5 de 5 estrelas">{STAR * 5}</div>
<blockquote>“{q}”</blockquote>
<figcaption><span class="avatar" aria-hidden="true">{n[0]}</span><span><b>{n}</b>{t}</span></figcaption></figure>''' for q, n, t in QUOTES)
    body = f'''
<section class="page-hero">
  <div class="container">
    <span class="rule"></span>
    <h1>O que as clientes dizem</h1>
    <p class="lead">Relatos de quem já passou pelo espaço, com as palavras de cada uma.</p>
  </div>
</section>
<section class="sec sec--nude" style="padding-top:clamp(48px,6vw,72px)">
  <div class="container"><div class="quotes">{cards}</div></div>
</section>
{cta_band("Sua avaliação pode ser a próxima", "Conte o que você busca e escolha o melhor horário.")}
'''
    page("depoimentos.html", "Depoimentos | AJ Estética Beauty",
         "Veja o que as clientes dizem sobre os atendimentos da Dra. Ana Júlia na AJ Estética Beauty, em Uberlândia.", body, "depoimentos")

# ============================== CONTATO ==============================
def build_contact():
    opts = "".join(f'<option value="{t["nome"]}">{t["nome"]}</option>' for t in TREATMENTS)
    opts += '<option value="Botox / Harmonização facial (lista de espera)">Botox / Harmonização facial (lista de espera)</option><option value="Ainda não sei, quero orientação">Ainda não sei, quero orientação</option>'
    body = f'''
<section class="page-hero">
  <div class="container">
    <span class="rule"></span>
    <h1>Agende sua avaliação</h1>
    <p class="lead">A Dra. Ana Júlia atende cada pessoa com tempo e hora marcada. Antes de qualquer procedimento, ela avalia o seu histórico e explica o que será feito, com materiais descartáveis e ambiente higienizado. Segurança vem antes de qualquer resultado.</p>
  </div>
</section>

<section class="sec sec--nude" style="padding-top:clamp(48px,6vw,72px)">
  <div class="container contact-grid">
    <aside class="info-card">
      <h2>Informações</h2>
      <ul class="info-list">
        <li>{icon("phone")}<div><b>Telefone e WhatsApp</b><span><a href="tel:+{WA_NUMBER}">{PHONE_LABEL}</a></span></div></li>
        <li>{icon("mail")}<div><b>E-mail</b><span><a href="mailto:{EMAIL}">{EMAIL}</a></span></div></li>
        <li>{icon("pin")}<div><b>Endereço</b><span>{ADDRESS}</span></div></li>
        <li>{icon("clock")}<div><b>Horário de atendimento</b><span>Segunda a sexta, 9h às 18h<br>Sábado, 9h às 13h</span></div></li>
      </ul>
    </aside>
    <div class="form-card">
      <h2>Envie uma mensagem</h2>
      <p class="note" style="margin-bottom:24px">Campos com <span style="color:var(--accent)">*</span> são obrigatórios. Ao enviar, abrimos o WhatsApp com seus dados preenchidos.</p>
      <form class="form" id="contact-form" novalidate>
        <div class="two">
          <div class="field"><label for="nome">Nome <i>*</i></label><input id="nome" name="nome" type="text" autocomplete="name" required><span class="err" role="alert"></span></div>
          <div class="field"><label for="email">E-mail <i>*</i></label><input id="email" name="email" type="email" autocomplete="email" required><span class="err" role="alert"></span></div>
        </div>
        <div class="two">
          <div class="field"><label for="telefone">Telefone</label><input id="telefone" name="telefone" type="tel" autocomplete="tel" placeholder="(34) 91234-5678"></div>
          <div class="field"><label for="tratamento">Tratamento de interesse</label><select id="tratamento" name="tratamento"><option value="">Selecione</option>{opts}</select></div>
        </div>
        <div class="field"><label for="mensagem">Mensagem</label><textarea id="mensagem" name="mensagem" placeholder="Conte o que você gostaria de tratar ou tirar de dúvida."></textarea></div>
        <button class="btn btn--primary" type="submit">{WA_ICON} Enviar pelo WhatsApp</button>
        <p class="form-msg" id="form-msg" role="status"></p>
      </form>
    </div>
  </div>
</section>

{map_section("")}
'''
    page("contato.html", "Contato e agendamento | AJ Estética Beauty",
         "Agende sua avaliação com a Dra. Ana Júlia em Uberlândia. Telefone, e-mail, endereço, horários e formulário de contato.", body, "contato")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    build_home()
    for t in TREATMENTS:
        build_treatment(t)
    build_about()
    build_testimonials()
    build_contact()
