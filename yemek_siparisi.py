
corba = ['domates', 'mercimek', 'yayla', 'tarhana']
anayemek= ['orman kebap', 'fırında tavuk', 'makarna', 'köfte', 'fasulye']
tatlı = ['baklava', 'kemal paşa', 'helva', 'şekerpare']
print("Hoşgeldiniz...")
print("Corba Çeşitlerimiz:\n ",corba)
print("Ana Yemeklerimiz:\n",anayemek)
print("Tatlı Çeşitlerimiz:\n",tatlı)

print("---------------------------------")
siparis = input("Sipariş vermek ister misiniz? [E/H] ")

if siparis == "h":
    print("Sipariş vermediniz")

if siparis == "e":
    print("Sipariş vermeye hazırsınız... ")

siparis_corba = input("Corba Tercihiniz: ")
kontrol_corba = siparis_corba.lower()
if any(kontrol_corba in s for s in corba):
    print(siparis_corba, "sipariş verdiniz...")
else:
    print("Menüde olmayan sipariş verdiniz." )


siparis_anayemek  = input("Ana Yemek Tercihiniz: ")
kontrol_anayemek = siparis_anayemek.lower()

if any(kontrol_anayemek in s for s in anayemek):
    print(siparis_anayemek, "Siparişi verdiniz.")
else:
    print("Menüde olmayan sipariş verdiniz.")

siparis_tatli = input("Tatlı Tercihiniz: ")
kontrol_tatli = siparis_tatli.lower()

if any(kontrol_tatli in s for s in tatlı):
    print(kontrol_tatli, "Siparişi verdiniz.")
else:
    print("Menüde olmayan sipariş verdiniz.")

print('Tüm siparişleriniz alınmıştır. Tercihleriniz:\n', '\n'+ kontrol_tatli, '\n'+ kontrol_anayemek, '\n'+ kontrol_corba)