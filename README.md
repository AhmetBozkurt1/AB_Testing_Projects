<img width="1000" alt="Ekran Resmi 2024-05-27 09 34 58" src="https://github.com/AhmetBozkurt1/AB_Testing_Projects/assets/120393650/b1b07e6c-a176-44df-9b07-940136b3bbbb">

# AB Testi ile Bidding Yöntemlerinin Dönüşümünün Karşılaştırılması

## İş Problemi
Facebook kısa süre önce mevcut "maximumbidding" adı verilen teklif verme türüne alternatif olarak yeni bir teklif türü olan "average bidding"’i tanıttı. blabla.com, bu yeni özelliği test etmeye karar verdi ve average bidding'in maximum bidding'den daha fazla dönüşüm getirip getirmediğini anlamak için bir A/B testi yapmak istiyor. A/B testi 1 aydır devam ediyor ve blabla.com şimdi bu A/B testinin sonuçlarını analiz etmenizi bekliyor. blabla.com için nihai başarı ölçütü Purchase'dır. Bu nedenle, istatistiksel testler için Purchase metriğine odaklanılmalıdır.

## Veri Seti Hikayesi
Bir firmanın web sitesi bilgilerini içeren bu veri setinde kullanıcıların gördükleri ve tıkladıkları reklam sayıları gibi bilgilerin yanı sıra buradan gelen kazanç bilgileri yer almaktadır. Kontrol ve Test grubu olmak üzere iki ayrı veri seti vardır. Bu veri setleri ab_testing.xlsx excel’inin ayrı sayfalarında yer almaktadır. Kontrol grubuna Maximum Bidding, test grubuna Average Bidding uygulanmıştır.

## Proje Görevleri
- **AB Testing (Bağımsız İki Örneklem T Testi)**
  1. Hipotezleri Kur
  2. Varsayım Kontrolü
     - 1. Normallik Varsayımı (Shapiro)
     - 2. Varyans Homojenliği (Levene)
  3. Hipotezin Uygulanması
     - 1. Varsayımlar sağlanıyorsa bağımsız iki örneklem t testi
     - 2. Varsayımlar sağlanmıyorsa Mann-Whitney U testi
  4. p-value değerine göre sonuçları yorumla

## Görev 1: Veriyi Hazırlama ve Analiz Etme
- Kontrol ve test grubu verilerinin okunması ve analiz edilmesi
- Veri setlerinin birleştirilmesi (Concat)

## Görev 2: A/B Testinin Hipotezinin Tanımlanması
- Hipotezin tanımlanması
- Kontrol ve test grubu için purchase (kazanç) ortalamalarının analizi

## Görev 3: Hipotez Testinin Gerçekleştirilmesi
- AB Testing (Bağımsız İki Örneklem T Testi)
- Normallik Varsayımı ve Varyans Homojenliği sonuçlarına göre uygun testin seçilmesi
- Test sonuçlarının yorumlanması

## Görev 4: Sonuçların Analizi
- Hangi testin kullanıldığının ve sebeplerinin belirtilmesi
- Elde edilen test sonuçlarına göre müşteriye tavsiyede bulunulması
