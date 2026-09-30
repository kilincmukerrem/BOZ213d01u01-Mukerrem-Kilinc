import tkinter as tk

# --- OYUN DURUM VERİLERİ ---
yon = 0      # 0:Yatak, 1:Ayna, 2:Kitaplar, 3:Kapı, 4:Tavan, 5:Zemin
duvar = 0    
siir_fark_edildi = False
siir_inceleniyor = False
anahtar_ipucu = False
anahtar_alindi = False

# --- ÇİZİM MOTORU ---
def cizim_yap():
    tuval.delete("all")
    
    # 1. ŞİİR VE KAĞIT EKRANI (İpucu Ekranı)
    if siir_inceleniyor:
        tuval.configure(bg="white") # Kağıt görünümü için arka plan beyaz
        
        # Şiir Dizeleri
        siir_metni = "Ey şu küçücük hücrenin infaz memuru!\nBugün bana biraz acıyamaz mısın? \nZaten her gün, \nHer gün daha da uzaklaşmak,\nAsla tanıyamadığım benliğimden,\nSence de yeterince ağır bir ceza değil mi?"
        tuval.create_text(200, 50, text=siir_metni, font=("Courier", 10, "italic"), fill="black", justify=tk.CENTER)
        
        # Kağıttaki Yatak Çizimi (Siyah beyaz eskiz gibi)
        tuval.create_rectangle(120, 160, 280, 220, fill="white", outline="black", width=2)
        tuval.create_line(120, 130, 120, 220, fill="black", width=3) # Başlık
        tuval.create_line(280, 130, 280, 220, fill="black", width=3) # Ayakucu
        
        # Yatağın yanındaki küçük kare nokta (Anahtar İpucu)
        tuval.create_rectangle(105, 210, 115, 220, outline="red", width=2)
        
        return # Çizimi bitir, normal odayı çizme

    # 2. NORMAL ODA GÖRÜNÜMLERİ
    if yon == 0: # Yatak
        tuval.configure(bg="#2c3e50")
        tuval.create_rectangle(150, 40, 250, 140, fill="black", outline="gray", width=4)
        tuval.create_line(200, 40, 200, 140, fill="gray", width=4)
        tuval.create_rectangle(100, 200, 300, 280, fill="#34495e", outline="black", width=3)
        tuval.create_line(100, 160, 100, 280, fill="black", width=5)
        tuval.create_line(300, 160, 300, 280, fill="black", width=5)
        
    elif yon == 1: # Ayna
        tuval.configure(bg="#2c3e50")
        tuval.create_oval(150, 60, 250, 220, fill="lightblue", outline="silver", width=5)
        tuval.create_line(170, 90, 200, 140, fill="black", width=2)
        tuval.create_line(200, 140, 170, 180, fill="black", width=2)
        
    elif yon == 2: # Kitaplar
        tuval.configure(bg="#2c3e50")
        tuval.create_rectangle(120, 200, 280, 300, fill="#7f8c8d")
        tuval.create_rectangle(140, 180, 200, 200, fill="#c0392b")
        tuval.create_rectangle(150, 165, 210, 180, fill="#2980b9")
        tuval.create_rectangle(130, 150, 190, 165, fill="#f1c40f")
        
    elif yon == 3: # Kapı
        tuval.configure(bg="#2c3e50")
        tuval.create_rectangle(130, 40, 270, 300, fill="#34495e", outline="black", width=4)
        tuval.create_oval(240, 150, 255, 165, fill="gold")
        
    elif yon == 4: # Tavan
        tuval.configure(bg="#111111")
        tuval.create_line(200, 0, 200, 120, fill="gray", width=3)
        tuval.create_oval(170, 120, 230, 180, fill="yellow")
        
    elif yon == 5: # Zemin
        tuval.configure(bg="#7f8c8d")
        tuval.create_line(0, 100, 400, 150, fill="#95a5a6", width=2)
        tuval.create_line(0, 200, 400, 250, fill="#95a5a6", width=2)


# --- HİKAYE VE METİNLER ---
def ekran_yenile():
    cizim_yap()
    
    if siir_inceleniyor:
        metin = "Kağıttaki yatak çiziminin hemen yanında kırmızı, küçük kare bir nokta fark ettin.\nBu bir anahtar olabilir mi?\n\n[ Geri dönmek için yön tuşlarına basın ]"
        bilgi_alani.config(text=metin, fg="yellow")
        return
        
    if yon == 0:
        metin = "Köşede paslı demirleri olan bir yatak ve pencere var.\n[ \"Pencere?\" ]\n[ İncelemek için 'Boşluk' tuşuna basın ]\n[ hareket etmek için yön tuşlarını kullanın ]"
    elif yon == 1:
        metin = "Duvarda asılı kırık bir ayna duruyor.\n[ İncelemek için 'Boşluk' tuşuna basın ]"
    elif yon == 2:
        if not siir_fark_edildi:
            metin = "Dağınık halde kitaplar var.\n[ İncelemek için 'Boşluk' tuşuna basın ]"
        else:
            metin = "Kitapların arasında bir şiir sayfası duruyor...\n[ İyice incelemek için 'Boşluk' tuşuna basın ]"
    elif yon == 3:
        metin = "Kilitli demir bir kapı var.\n[ İncelemek için 'Boşluk' tuşuna basın ]"
    elif yon == 4:
        metin = "Tavanda loş ve titreyen bir lamba yanıyor. \nAma ışığı çevreyi aydınlatmıyor \n[hareket etmek için aşağı tuşuna bas]"
    elif yon == 5:
        metin = "Yerde soğuk gri bir beton var. \n[hareket etmek için yukarı tuşuna bas]"
        
    bilgi_alani.config(text=metin, fg="white")


# --- TUŞ KONTROLLERİ ---
def yon_degistir(yeni_yon, yeni_duvar=None):
    global yon, duvar, siir_inceleniyor
    siir_inceleniyor = False # Yön değiştirilirse kağıttan çık
    yon = yeni_yon
    if yeni_duvar is not None:
        duvar = yeni_duvar
    ekran_yenile()

def sol(event):
    if yon < 4: yon_degistir((yon - 1) % 4, (yon - 1) % 4)
def sag(event):
    if yon < 4: yon_degistir((yon + 1) % 4, (yon + 1) % 4)
def yukari(event):
    if yon == 5: yon_degistir(duvar)
    elif yon < 4: yon_degistir(4)
def asagi(event):
    if yon == 4: yon_degistir(duvar)
    elif yon < 4: yon_degistir(5)

# --- BOŞLUK (İNCELE) TUŞU ---
def incele(event):
    global siir_fark_edildi, siir_inceleniyor, anahtar_ipucu, anahtar_alindi
    
    if siir_inceleniyor:
        return # Kağıda bakarken incele tuşu çalışmaz
        
    if yon == 0: # Yatak
        if not anahtar_ipucu:
            bilgi_alani.config(text="Sadece soğuk rüzgar esiyor. Sıradan bir yatak. \nPencereden ince bir ay ışığı odayı aydınlatıyor. \n[devam etmek için yön tuşlarını kullan]", fg="lightblue")
        elif anahtar_ipucu and not anahtar_alindi:
            bilgi_alani.config(text="Şiirdeki çizimde gördüğün kare noktaya, yatağın yanına doğru eğildin...\nKüçük, sarı bir ANAHTAR buldun!", fg="yellow")
            anahtar_alindi = True
        else:
            bilgi_alani.config(text="Buradan anahtarı zaten aldın. Çıkma vakti.", fg="lightblue")
            
    elif yon == 1: # Ayna
        bilgi_alani.config(text="Bu yüz... Kim olduğunu gerçekten hatırlamıyorsun.", fg="lightblue")
        
    elif yon == 2: # Kitaplar ve Şiir
        if not siir_fark_edildi:
            bilgi_alani.config(text="[ 'infaz Memuru' şiiri dikkatini çekti ]\n[ İyice incelemek için tekrar 'Boşluk' tuşuna basın ]", fg="yellow")
            siir_fark_edildi = True
        else:
            # Şiiri iyice incele (Kağıt ekranına geçiş)
            siir_inceleniyor = True
            anahtar_ipucu = True # Artık kare noktayı görecek
            ekran_yenile()
            
    elif yon == 3: # Kapı
        if anahtar_alindi:
            bilgi_alani.config(text="Anahtarı kilide soktun ve çevirdin...\nKapı gıcırdayarak açıldı.\n\nKURTULDUN!", fg="lightgreen")
        else:
            bilgi_alani.config(text="Kapı kilitli. Açılmıyor.", fg="red")

# --- ARAYÜZ KURULUMU ---
pencere = tk.Tk()
pencere.title("Küçük Hücre")
pencere.geometry("600x550")
pencere.configure(bg="black")

tuval = tk.Canvas(pencere, width=400, height=300, bg="black", highlightthickness=0)
tuval.pack(pady=20)

bilgi_alani = tk.Label(pencere, bg="black", fg="white", font=("Arial", 12), justify=tk.CENTER)
bilgi_alani.pack(pady=10)

pencere.bind("<Left>", sol)
pencere.bind("<Right>", sag)
pencere.bind("<Up>", yukari)
pencere.bind("<Down>", asagi)
pencere.bind("<space>", incele)

ekran_yenile()
pencere.mainloop()
