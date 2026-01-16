import streamlit as st
import time

# --- 1. AYARLAR VE TASARIM ---
st.set_page_config(page_title="Yalan Dünya Karakter Testi", page_icon="🎬", layout="centered")

# CSS ile butonları ve resimleri güzelleştirelim
st.markdown("""
    <style>
    .stRadio > label {font-size: 20px; font-weight: bold; padding: 10px; cursor: pointer;}
    .stButton > button {
        width: 100%; 
        border-radius: 12px; 
        height: 3.5em; 
        font-weight: bold; 
        background-color: #FF4B4B; 
        color: white;
    }
    .stProgress > div > div > div > div { background-color: #FF4B4B; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. VERİ TABANI (Karakterler) ---
karakterler = {
    "Rıza": {"desc": "Sabırlısın, düzgünsün ama arada kalmaktan yorulmadın mı?",
             "img": "https://i.pinimg.com/736x/db/96/9f/db969f9948aaff0d53846a1c36a1b6bc.jpg"},
    "Deniz": {"desc": "Mantıklısın ama etrafındaki saçmalıklara kapılmaktan kurtulamıyorsun.",
              "img": "https://i.pinimg.com/736x/fb/a6/e0/fba6e0086ebd481940cdd9cc1c72f4c5.jpg"},
    "Nurhayat": {"desc": "TERBİYESİZLER! Mükemmeliyetçisin ve her şey senin kontrolünde olsun istiyorsun.",
                 "img": "https://i.pinimg.com/736x/2d/a8/00/2da80059f556aa2df086240abf909374.jpg"},
    "Orçun": {"desc": "Dünya yansa umurunda değil. Olayın 'öpüşelim mi' ve Playstation.",
              "img": "https://i.pinimg.com/1200x/e9/f8/ca/e9f8cadac4eb78571ad2e2b20b868bf7.jpg"},
    "Bora": {"desc": "Karşıyaka delikanlisi , biraz entel biraz kabadayısın.",
             "img": "https://i.pinimg.com/736x/c3/a6/dc/c3a6dcd295ac59b37d0da8b4ff86ff15.jpg"},
    "Emir": {"desc": "Egon tavan yapmış ama şeytan tüyün var, kendini sevdiriyorsun.",
             "img": "https://i.pinimg.com/736x/80/b7/3c/80b73ccea526dc2279a27cff8006953b.jpg"},
    "Açılay": {"desc": "Enerjin hiç bitmiyor! Biraz safsın, biraz çılgınsın,çabana sağlık tatlım!",
               "img": "https://i.pinimg.com/1200x/bf/5f/e0/bf5fe0b6b3c7f2feae82a1e3eb651c48.jpg"},
    "Selahattin": {"desc": "Gözün biraz dışarıda, başın hep belada ama paçayı kurtarıyorsun.",
                   "img": "https://i.pinimg.com/736x/d1/8f/ac/d18fac8aa77f0f9d9273cce75ae3d7dd.jpg"},
    "Tülay": {"desc": "Aşk kadınısın! 'Ben bu oyunu bozarım' diyecek kadar delikanlısın.",
              "img": "https://i.pinimg.com/736x/0d/63/b4/0d63b466f96968a0a17d9aa15a4027db.jpg"},
    "Gülistan": {"desc": "Panik atak senin göbek adın! Her şeyden nem kapıyorsun.",
                 "img": "https://i.pinimg.com/736x/c9/36/32/c93632e19b99974ea1cc1052d12fc394.jpg"}
}

# --- 3. SORULAR (Resimli) ---
# Not: 'img' kısmına her soru için farklı bir resim linki koyabilirsin.
sorular = [
    {
        "soru": "Birisi sana çok saçma bir fikirle geldi. Tepkin?",
        "img": "https://i.pinimg.com/1200x/69/8c/91/698c91ec749b12e11369037082c15ef7.jpg",  # Örnek GIF
        "siklar": {
            "Güler geçerim, bana ne ya.": ["Orçun", "Emir"],
            "Hemen eleştirip doğrusunu anlatırım.": ["Bora", "Nurhayat"],
            "Sabır çekerim, kırmadan anlatırım.": ["Rıza", "Deniz"],
            "Ay fenalıklar bastı! Üstüme gelmeyin!": ["Gülistan", "Açılay"]
        }
    },
    {
        "soru": "Hafta sonu Cihangir'de bir kafedesin. Ne içersin?",
        "img": "https://i.pinimg.com/1200x/69/8c/91/698c91ec749b12e11369037082c15ef7.jpg",  # Örnek GIF
        "siklar": {
            "Organik, detoks suyu veya latte.": ["Bora", "Deniz", "Açılay"],
            "Çay. Yanında da börek.": ["Rıza", "Gülistan"],
            "Viski veya kokteyl, hava atmalıyız.": ["Emir", "Nurhayat"],
            "Bira.": ["Orçun", "Selahattin"]
        }
    },
    {
        "soru": "Hayat motton nedir?",
        "img": "https://i.pinimg.com/1200x/69/8c/91/698c91ec749b12e11369037082c15ef7.jpg",
        "siklar": {
            "Hayat çok zor, her an kötü bir şey olabilir.": ["Gülistan"],
            "Sanat için soyunurum, sanat için giyinirim.": ["Bora", "Açılay", "Emir"],
            "Düzen, intizam, temizlik.": ["Nurhayat"],
            "Yalan dünya be, kafana göre takıl.": ["Selahattin", "Tülay", "Orçun"]
        }
    },
    {
        "soru": "Kıyafet dolabın nasıl?",
        "img": "https://i.pinimg.com/1200x/69/8c/91/698c91ec749b12e11369037082c15ef7.jpg",  # Temsili
        "siklar": {
            "Marka, şık, ütülü ve renklerine göre.": ["Nurhayat", "Emir"],
            "Salaş, siyah ağırlıklı veya rahat.": ["Orçun", "Rıza"],
            "Renkli, pullu payetli veya iddialı.": ["Tülay", "Açılay"],
            "Fularlar, şapkalar, vintage.": ["Bora", "Deniz"]
        }
    },
    {
        "soru": "Sevgilinin telefonunda şüpheli bir mesaj yakaladın. İlk tepkin?",
        "img": "https://i.pinimg.com/1200x/69/8c/91/698c91ec749b12e11369037082c15ef7.jpg",
        "siklar": {
            "Gözlerim döner, o telefonu ona yediririm!": ["Nurhayat", "Tülay"],
            "Hemen panik atak geçiririm, nefesim kesilir.": ["Gülistan"],
            "Yalan söylemeye başlarsa inanmış gibi yaparım, sonra hallederim.": ["Selahattin", "Emir"],
            "Çok banalsiniz... Medeni insanlar gibi konuşur ayrılırız.": ["Bora", "Deniz"]
        }
    },
    {
        "soru": "Bir restorana gittin, hesap geldi ama cüzdanını evde unutmuşsun...",
        "img": "https://i.pinimg.com/1200x/69/8c/91/698c91ec749b12e11369037082c15ef7.jpg",
        "siklar": {
            "Yanımızdakilere kitlerim, 'Siz ödeyin sonra halleşiriz' derim.": ["Selahattin", "Emir"],
            "Rezalet! Yerim dibine girerim, hemen birini aratırım.": ["Nurhayat", "Rıza"],
            "Bulaşıkları yıkarız ya, nolcak?": ["Orçun", "Açılay"],
            "Garsona sanat ve hayat üzerine nutuk çekip kafasını karıştırırım.": ["Bora"]
        }
    },
    {
        "soru": "Sana başrol teklif edildi ama rol gereği saçını kazıtman lazım.",
        "img": "https://i.pinimg.com/1200x/69/8c/91/698c91ec749b12e11369037082c15ef7.jpg",
        "siklar": {
            "Asla! Saçlarım benim her şeyim, sponsorlarım ne der?": ["Emir", "Nurhayat"],
            "Sanat için soyunurum da, kazıtırım da. Ben oyuncuyum!": ["Açılay", "Deniz", "Bora"],
            "Kazıtsak da uzuyor mu geri? İyi tamam, fark etmez.": ["Orçun"],
            "Babamlar ne der? Elalem ne der? Oynayamam ben.": ["Rıza", "Gülistan"]
        }
    },
    {
        "soru": "Trafikte sıkıştın, yanındaki araba sürekli korna çalıyor!",
        "img": "https://i.pinimg.com/1200x/69/8c/91/698c91ec749b12e11369037082c15ef7.jpg",
        "siklar": {
            "Camı açar 'Ne basıyorsun be!' diye çemkiririm.": ["Tülay", "Nurhayat", "Selahattin"],
            "Kornanın ritmine göre kafamı sallar müzik dinlerim.": ["Orçun", "Açılay"],
            "Hiç muhatap olmam, camı kapatır önüme bakarım.": ["Rıza", "Deniz"],
            "İstanbul'un kaosunu ve insanlığın çöküşünü izlerim...": ["Bora"]
        }
    },
    {
        "soru": "Evde yangın çıktı! Yanına alacağın ilk şey?",
        "img": "https://i.pinimg.com/1200x/69/8c/91/698c91ec749b12e11369037082c15ef7.jpg",
        "siklar": {
            "Kombine biletlerim ve fön makinem.": ["Emir", "Açılay"],
            "Playstation'ım ve şarj aletim.": ["Orçun"],
            "Tapular, altınlar ve çeyiz sandığım!": ["Nurhayat", "Gülistan"],
            "Senaryolarım ve fular koleksiyonum.": ["Bora", "Deniz"]
        }
    },
    {
        "soru": "Arkadaş ortamında biri sana 'Kilo mu aldın sen?' dedi.",
        "img": "https://i.pinimg.com/1200x/69/8c/91/698c91ec749b12e11369037082c15ef7.jpg",
        "siklar": {
            "Sensin şişko! Hasetinizden çatlayın ayol!": ["Nurhayat", "Tülay"],
            "Depresyondayım, üstüme gelmeyin...": ["Gülistan", "Orçun"],
            "Bu balık etli halim, ekran bunu seviyor.": ["Açılay", "Emir"],
            "Beden algısı üzerine kapitalist sistemin dayatmaları bunlar...": ["Bora"]
        }
    },
    {
        "soru": "Yolda yürürken eski sevgilini yeni sevgilisiyle gördün.",
        "img": "https://i.pinimg.com/1200x/69/8c/91/698c91ec749b12e11369037082c15ef7.jpg",
        "siklar": {
            "Görmezden gelirim, kafamı çevirip hızla uzaklaşırım.": ["Rıza", "Deniz"],
            "Yanlarına gidip rezillik çıkarırım, laf sokmadan duramam!": ["Nurhayat", "Tülay"],
            "Yeni sevgilisini süzerim, 'Benden çirkinmiş' derim.": ["Selahattin", "Emir"],
            "Gidip 'Naber ya?' derim, hiç takılmam.": ["Orçun", "Açılay"]
        }
    },
    {
        "soru": "Cihangir'de bir sergi açılışına davetlisin. Ne giyersin?",
        "img": "https://i.pinimg.com/1200x/69/8c/91/698c91ec749b12e11369037082c15ef7.jpg",
        "siklar": {
            "En pahalı, en marka kıyafetlerimi. Zengin görüneyim.": ["Nurhayat", "Emir"],
            "Siyah, bol, yırtık pırtık bir şeyler.": ["Orçun", "Bora"],
            "Parlak, pullu, dikkat çeken bir abiye/takım.": ["Tülay", "Selahattin", "Açılay"],
            "Temiz, ütülü, düzgün bir gömlek pantolon.": ["Rıza", "Deniz"]
        }
    }
]

# --- 4. SESSION STATE (Hafıza) ---
if 'step' not in st.session_state:
    st.session_state.step = 0  # Şu an kaçıncı sorudayız (0'dan başlar)
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = []  # Cevapları burada biriktireceğiz


# --- 5. FONKSİYONLAR ---
def sonraki_soruya_gec():
    # Seçilen cevabı kaydetmemiz lazım ama Streamlit radio butonu zaten state tutuyor.
    # Biz sadece step'i artıracağız.
    st.session_state.step += 1


def testi_sifirla():
    st.session_state.step = 0
    st.session_state.user_answers = []


def hesapla_ve_goster():
    puanlar = {k: 0 for k in karakterler.keys()}

    # Kullanıcının verdiği cevapları analiz et
    for i, cevap_anahtari in enumerate(st.session_state.user_answers):
        # Cevap anahtarı bir liste döndürür: ["Orçun", "Emir"] gibi
        for karakter in cevap_anahtari:
            if karakter in puanlar:
                puanlar[karakter] += 1

    # En yüksek puanı alanı bul
    kazanan = max(puanlar, key=puanlar.get)
    return kazanan


# --- 6. ARAYÜZ AKIŞI ---

# HEADER (Her sayfada sabit kalsın)
st.title("🎭 Hangi Yalan Dünya Karakterisin?")

# Eğer sorular bitmediyse:
if st.session_state.step < len(sorular):
    current_q = sorular[st.session_state.step]

    # İlerleme Çubuğu
    progress = (st.session_state.step) / len(sorular)
    st.progress(progress)
    st.caption(f"Soru {st.session_state.step + 1} / {len(sorular)}")

    # SORU GÖRSELİ
    st.image(current_q["img"], use_container_width=True)

    # SORU METNİ
    st.subheader(current_q["soru"])

    # ŞIKLAR
    # Radio butonu her soruda benzersiz olmalı, key parametresine step ekliyoruz
    secilen_sik = st.radio(
        label="Cevabını seç:",
        options=list(current_q["siklar"].keys()),
        key=f"q_{st.session_state.step}",
        label_visibility="collapsed"
    )

    # İLERLE BUTONU
    if st.button("SONRAKİ SORU ➡️"):
        # Cevabı kaydet
        puan_verilecek_karakterler = current_q["siklar"][secilen_sik]
        st.session_state.user_answers.append(puan_verilecek_karakterler)
        # Sayfayı yenile (step artacak)
        sonraki_soruya_gec()
        st.rerun()

# Sorular bittiyse (SONUÇ EKRANI):
else:
    st.progress(100)

    # Yükleniyor efekti (Heyecan yaratmak için)
    with st.spinner('Cihangir muhtarı kayıtları inceliyor...'):
        time.sleep(1.5)

    kazanan_isim = hesapla_ve_goster()
    kazanan_bilgi = karakterler[kazanan_isim]

    st.balloons()
    st.success("Test Tamamlandı!")

    st.markdown(f"<h1 style='text-align: center; color: #FF4B4B;'>SEN {kazanan_isim.upper()} KARAKTERİSİN!</h1>",
                unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(kazanan_bilgi["img"], caption=kazanan_isim)
        st.info(kazanan_bilgi["desc"])

        if st.button("🔄 Testi Tekrar Başlat"):
            testi_sifirla()
            st.rerun()