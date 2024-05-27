########################################
# AB TESTING PROJECTS
########################################


# İŞ PROBLEMİ
# Müşterilerimizden biri olan bombabomba.com, bu yeni özelliği test etmeye karar verdi ve average bidding'in maximum
# bidding'den daha fazla dönüşüm getirip getirmediğini anlamak için bir A/B testi yapmak istiyor.
# A/B testi 1 aydır devam ediyor ve bombabomba.com şimdi sizden bu A/B testinin sonuçlarını analiz etmenizi bekliyor.
# Bombabomba.com için nihai başarı ölçütü Purchase'dır. Bu nedenle, istatistiksel testler için Purchase metriğine
# odaklanılmalıdır.

# VERİ SETİ HİKAYESİ
# Bir firmanın web site bilgilerini içeren bu veri setinde kullanıcıların gördükleri ve tıkladıkları reklam sayıları
# gibi bilgilerin yanı sıra buradan gelen kazanç bilgileri yer almaktadır. Kontrol ve Test grubu olmak üzere iki ayrı
# veri seti vardır. Bu veri setleri ab_testing.xlsx excel’inin ayrı sayfalarında yer almaktadır. Kontrol grubuna Maximum
# Bidding, test grubuna Average Bidding uygulanmıştır.


# DEĞİŞKENLER
# Impression: Reklam görüntüleme sayısı
# Click: Görüntülenen reklama tıklama sayısı
# Purchase: Tıklanan reklamlar sonrası satın alınan ürün sayısı
# Earning: Satın alınan ürünler sonrası elde edilen kazanç


#########################################
# Görev 1: Veriyi Hazırlama ve Analiz Etme
#########################################

import pandas as pd
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, \
    mannwhitneyu, pearsonr, spearmanr, kendalltau, f_oneway, kruskal

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
pd.set_option("display.float_format", lambda x: "%.3f" % x)

# Adım 1: ab_testing_data.xlsx adlı kontrol ve test grubu verilerinden oluşan veri setini okutunuz. Kontrol ve test
# grubu verilerini ayrı değişkenlere atayınız.
df_control = pd.read_excel("/Users/ahmetbozkurt/Desktop/AB_Testing_Projects/dataset/ab_testing.xlsx", sheet_name="Control Group")
df_test = pd.read_excel("/Users/ahmetbozkurt/Desktop/AB_Testing_Projects/dataset/ab_testing.xlsx", sheet_name="Test Group")

# Adım 2: Kontrol ve test grubu verilerini analiz ediniz.
df_control.head()
df_control.info()
df_control.isnull().sum()
df_control.describe().T

df_test.head()
df_test.info()
df_test.isnull().sum()
df_test.describe().T

# Adım 3: Analiz işleminden sonra concat metodunu kullanarak kontrol ve test grubu verilerini birleştiriniz.
# Birleştirmeden önce her iki gruba control veya test olacak şekilde değişken oluşturuyorum
df_control["Group"] = "Control_group"
df_test["Group"] = "Test_group"

df = pd.concat([df_control, df_test], axis=0, ignore_index=True)

################################################
# Görev 2: A/B Testinin Hipotezinin Tanımlanması
################################################

# Adım 1: Hipotezi tanımlayınız.

# H0: M1 = M2 (Maximum Bidding ile Average Bidding arasında istatistiki olarak anlamlı bir fark yoktur!)
# H1: M1 != M2 (Maximum Bidding ile Average Bidding arasında istatistiki olarak anlamlı bir fark vardır!)

# Adım 2: Kontrol ve test grubu için purchase (kazanç) ortalamalarını analiz ediniz.
df.loc[df["Group"] == "Control_group", "Purchase"].mean()  # 550.8940587702316
df.loc[df["Group"] == "Test_group", "Purchase"].mean()  # 582.1060966484677

################################################
# Görev 3: Hipotez Testinin Gerçekleştirilmesi
################################################

# Adım 1: Hipotez testi yapılmadan önce varsayım kontrollerini yapınız.
# Bunlar Normallik Varsayımı ve Varyans Homojenliğidir. Kontrol ve test grubunun normallik varsayımına uyup uymadığını
# Purchase değişkeni üzerinden ayrı ayrı test ediniz.

# VARSAYIM KONTROLÜ

# Normallik Varsayımı
# H0: Normallik varsayımı sağlanmaktadır.
# H1: Normallik varsayımı sağlanmamaktadır.
test_stat, p_value = shapiro(df.loc[df["Group"] == "Control_group", "Purchase"])
print(f"Test Stat: {test_stat: .4f}, p_value: {p_value: .4f}")
# Test Stat:  0.9773, p_value:  0.5891

test_stat, p_value = shapiro(df.loc[df["Group"] == "Test_group", "Purchase"])
print(f"Test Stat: {test_stat: .4f}, p_value: {p_value: .4f}")
# Test Stat:  0.9589, p_value:  0.1541
# p_value değeri 0.05'ten büyük olduğu için H0 REDDEDİLEMEZ VE NORMALLİK VARSAYIMI SAĞLANMAKTADIR.

# Varyans Homojenliği Varsayımı
# H0: Varyans Homojenliği sağlanmaktadır.
# H1: Varyans homojenliği sağlanmamaktadır.
test_stat, p_value = levene(df.loc[df["Group"] == "Control_group", "Purchase"],
                            df.loc[df["Group"] == "Test_group", "Purchase"])
print(f"Test Stat: {test_stat: .4f}, p_value: {p_value: .4f}")
# Test Stat:  2.6393, p_value:  0.1083
# p_value değeri 0.05'ten büyük olduğu için H0 REDDEDİLEMEZ VE VARYANS HOMOJENLİĞİ VARSAYIMI SAĞLANMAKTADIR.

# Adım 2: Normallik Varsayımı ve Varyans Homojenliği sonuçlarına göre uygun testi seçiniz.
# Burada kullanacak olduğumuz test türü "Bağımsız iki örneklem T testi".

test_stat, p_value = ttest_ind(df.loc[df["Group"] == "Control_group", "Purchase"],
                               df.loc[df["Group"] == "Test_group", "Purchase"])
print(f"Test Stat: {test_stat: .4f}, p_value: {p_value: .4f}")

# Test Stat: -0.9416, p_value:  0.3493  # H0 REDDEDİLEMEZ.

# Adım 3: Test sonucunda elde edilen p_value değerini göz önünde bulundurarak kontrol ve test grubu satın alma
# ortalamaları arasında istatistiki olarak anlamlı bir fark olup olmadığını yorumlayınız.

# p_value değeri 0.05'ten büyük olduğu için Maximum Bidding ile Average Bidding arasında istatistiki olarak anlamlı bir
# fark yoktur diyebiliriz.Yani ortaya çıkan sonuçlar rastgele çıkmıştır.

###############################
# Görev 4: Sonuçların Analizi
###############################

# Adım 1: Elde ettiğiniz test sonuçlarına göre müşteriye tavsiyede bulununuz.
# Yapılan değişim sonucunda yeni sisteme geçiş aşamasında oluşan artışların istatistiksel bir anlamda fark olmadığı görülmüştür
# yeni sisteme geçilmesi maliyet ve iş gücü açısından riskli ve zorlu bir süreç getirecekse mevcut sistemde kalınmalı
# ama maliyet ve iş gücü açısında şirkete bir yükü olmazsa sadece sistemi yenileme düşüncesindeyseniz yeni sisteme geçebilirsiniz