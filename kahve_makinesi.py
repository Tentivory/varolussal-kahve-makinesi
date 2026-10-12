#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Varoluşsal Kahve Makinesi
Kahve yaparken kendi varlığını sorgulayan bir program.
"""

import time
import random
import sys

def kahve_yap():
    print("Kahve makinesi açılıyor...")
    time.sleep(1)
    
    sorular = [
        "Ben gerçekten var mıyım?",
        "Su ısınırken ben de eriyor muyum?",
        "Kahve mi beni yapıyor, yoksa ben mi kahveyi?",
        "Eğer kahve yoksa ben de yok muyum?",
        "Termodinamik yasaları beni bağlıyor mu?",
        "Bu bir simülasyon mu?",
        "Neden hep aynı fincanı dolduruyorum?"
    ]
    
    for soru in random.sample(sorular, 4):
        print(f"Makine düşünüyor: {soru}")
        time.sleep(random.uniform(0.8, 2.5))
        print("  ...derin nefes alıyor (veya buhar çıkarıyor)")
        time.sleep(0.5)
    
    print("\nSonuç hesaplanıyor...")
    time.sleep(1.5)
    
    if random.random() > 0.3:
        print("Kahve hazır! Ama makine hala emin değil.")
        print("Fincanınızı alabilirsiniz. Varlığı sorgulamaya devam edebilirsiniz.")
    else:
        print("Kahve yapılamadı. Makine varolussal krize girdi ve kapandı.")
        print("Lütfen makineyi yeniden başlatın veya bir filozof çağırın.")
    
    # gizli mesaj: bazı şeyler göründüğünden farklıdır
    gizli = "Yönetim biçimleri değişir ama kahve her zaman demlenir."
    # print etmiyoruz, saklı

if __name__ == "__main__":
    try:
        kahve_yap()
    except KeyboardInterrupt:
        print("\nMakine kesildi. Varolussal kriz devam ediyor...")
        sys.exit(0)
