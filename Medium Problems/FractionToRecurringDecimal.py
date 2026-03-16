def find_fraction(a: int, b: int) -> str:
    if b == 0:
        return "Tanımsız (Sıfıra Bölme Hatası)"
    if a == 0:
        return "0"

    a, b = abs(a), abs(b)

    # 1. Tam Kısım
    tam_kisim = a // b
    kalan = a % b
    
    # Eğer tam bölünüyorsa (kalan 0 ise), işimiz bitti
    if kalan == 0:
        return tam_kisim

    res = [str(tam_kisim), "."]
    
    # Daha önce gördüğümüz kalanları ve onların 'res' listesindeki konumlarını tutacağız
    gorulen_kalanlar = {}

    # 2. Ondalıklı Kısım (Kalan 0 olana kadar dön)
    while kalan != 0:
        # Eğer bu kalanı daha önce gördüysek, DÖNGÜYÜ BULDUK!
        if kalan in gorulen_kalanlar:
            baslangic_indexi = gorulen_kalanlar[kalan]
            # Tekrar eden kısmın başına ve sonuna standart gösterim olan parantez koyalım
            res.insert(baslangic_indexi, "(")
            res.append(")")
            break
            
        # Kalanı ve şu anki pozisyonunu sözlüğe kaydet
        gorulen_kalanlar[kalan] = len(res)
        
        # Bakkal bölmesi: Kalanın yanına 0 at (10 ile çarp) ve böl
        kalan *= 10
        res.append(str(kalan // b))
        kalan %= b

    return "".join(res)

if __name__ == "__main__":
    test_nums = [
        (1, 2),    # 0.5
        (50, 22),  # 2.2(72) -> 72 tekrar eder
        (101, 10), # 10.1
        (2, 3),    # 0.(6)
        (1, 6),    # 0.1(6) -> Koda takla attıran o meşhur örnek
        (1, 17),
        (989, 12),
        (1, 7)     # 0.(142857) -> Float limitlerini aşan efsanevi uzun desen
    ]
    for a, b in test_nums:
        print(f"{a} / {b} = {find_fraction(a, b)}")