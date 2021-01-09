import os
import re
import pandas as pd
import numpy as np

all_data = list()

for file_name in os.listdir("real_estate_scraper"):
    if file_name.endswith(".csv"):
        data = pd.read_csv(os.path.join("real_estate_scraper", file_name), dtype="unicode")
        print(f"File name -> {file_name}\tdataset len -> {len(data)}")
        all_data.append(data)

houses = pd.concat(all_data)
houses = houses.drop_duplicates()

print("Datasets concatted")


houses["fiyat"].fillna("0", inplace=True)
houses["depozito"].fillna("0", inplace=True)
houses["kira_getirisi"].fillna("0", inplace=True)
houses["krediye_uygunluk"].fillna("False", inplace=True)
houses["esya_durumu"].fillna("Yok", inplace=True)
houses["takas"].fillna("Yok", inplace=True)
houses["site_icerisinde"].fillna("False", inplace=True)
houses["tapu_durumu"].fillna("False", inplace=True)
houses["il"].fillna("", inplace=True)
houses["ilce"].fillna("", inplace=True)
houses["mahalle"].fillna("", inplace=True)
houses["adsl"].fillna("False", inplace=True)
houses["ahsap_dograma"].fillna("False", inplace=True)
houses["alarm"].fillna("False", inplace=True)
houses["ankastre_mutfak"].fillna("False", inplace=True)
houses["balkon"].fillna("False", inplace=True)
houses["barbeku"].fillna("False", inplace=True)
houses["beyaz_esyali"].fillna("False", inplace=True)
houses["camasir_odasi"].fillna("False", inplace=True)
houses["celik_kapi"].fillna("False", inplace=True)
houses["dusakabin"].fillna("False", inplace=True)
houses["duvar_kagidi"].fillna("False", inplace=True)
houses["ebeveyn_banyolu"].fillna("False", inplace=True)
houses["giyinme_odasi"].fillna("False", inplace=True)
houses["gomme_dolap"].fillna("False", inplace=True)
houses["goruntulu_diafon"].fillna("False", inplace=True)
houses["hali_kaplama"].fillna("False", inplace=True)
houses["hazir_mutfak"].fillna("False", inplace=True)
houses["hilton_banyo"].fillna("False", inplace=True)
houses["isicam"].fillna("False", inplace=True)
houses["jakuzi"].fillna("False", inplace=True)
houses["kablo_tv_uydu"].fillna("False", inplace=True)
houses["kapali_balkon"].fillna("False", inplace=True)
houses["kartonpiyer"].fillna("False", inplace=True)
houses["klima"].fillna("False", inplace=True)
houses["laminant_mutfak"].fillna("False", inplace=True)
houses["marley"].fillna("False", inplace=True)
houses["mermer_zemin"].fillna("False", inplace=True)
houses["mobilyali"].fillna("False", inplace=True)
houses["mutfak_dogalgazi"].fillna("False", inplace=True)
houses["panel_kapi"].fillna("False", inplace=True)
houses["panjur"].fillna("False", inplace=True)
houses["parke"].fillna("False", inplace=True)
houses["parke___laminant"].fillna("False", inplace=True)
houses["saten_alci"].fillna("False", inplace=True)
houses["saten_boya"].fillna("False", inplace=True)
houses["sauna"].fillna("False", inplace=True)
houses["seramik_zemin"].fillna("False", inplace=True)
houses["spot_isik"].fillna("False", inplace=True)
houses["somine"].fillna("False", inplace=True)
houses["teras"].fillna("False", inplace=True)
houses["vestiyer"].fillna("False", inplace=True)
houses["yerden_isitma"].fillna("False", inplace=True)
houses["parke___lamine"].fillna("False", inplace=True)
houses["asansor"].fillna("False", inplace=True)
houses["bahceli"].fillna("False", inplace=True)
houses["cam_mozaik_kaplama"].fillna("False", inplace=True)
houses["fitness"].fillna("False", inplace=True)
houses["guvenlik"].fillna("False", inplace=True)
houses["hidrofor"].fillna("False", inplace=True)
houses["isi_yalitim"].fillna("False", inplace=True)
houses["jenerator"].fillna("False", inplace=True)
houses["kapici"].fillna("False", inplace=True)
houses["otopark___acik"].fillna("False", inplace=True)
houses["otopark___kapali"].fillna("False", inplace=True)
houses["oyun_parki"].fillna("False", inplace=True)
houses["pvc_dograma"].fillna("False", inplace=True)
houses["siding"].fillna("False", inplace=True)
houses["site_icerisinde"].fillna("False", inplace=True)
houses["kullanim_durumu"].fillna("bos", inplace=True)
houses["su_deposu"].fillna("False", inplace=True)
houses["tenis_kortu"].fillna("False", inplace=True)
houses["yangin_merdiveni"].fillna("False", inplace=True)
houses["yuzme_havuzu"].fillna("False", inplace=True)
houses["ahsap_dograma"].fillna("False", inplace=True)
houses["arka_cephe"].fillna("False", inplace=True)
houses["caddeye_yakin"].fillna("False", inplace=True)
houses["denize_sifir"].fillna("False", inplace=True)
houses["denize_yakin"].fillna("False", inplace=True)
houses["havaalanina_yakin"].fillna("False", inplace=True)
houses["manzara"].fillna("False", inplace=True)
houses["manzara___bogaz"].fillna("False", inplace=True)
houses["manzara___deniz"].fillna("False", inplace=True)
houses["manzara___doga"].fillna("False", inplace=True)
houses["manzara___gol"].fillna("False", inplace=True)
houses["manzara___sehir"].fillna("False", inplace=True)
houses["merkezde"].fillna("False", inplace=True)
houses["metroya_yakin"].fillna("False", inplace=True)
houses["otobana_yakin"].fillna("False", inplace=True)
houses["on_cephe"].fillna("False", inplace=True)
houses["toplu_ulasima_yakin"].fillna("False", inplace=True)
houses["metrobuse_yakin"].fillna("False", inplace=True)
houses["deniz_ulasimina_yakin"].fillna("False", inplace=True)
houses["cadde_uzerinde"].fillna("False", inplace=True)
houses["tramvaya_yakin"].fillna("False", inplace=True)
houses["marmaraya_yakin"].fillna("False", inplace=True)
houses["e_5_e_yakin"].fillna("False", inplace=True)
houses["tem_e_yakin"].fillna("False", inplace=True)
houses["minibus___dolmusa_yakin"].fillna("False", inplace=True)
houses["avrasya_tuneli_ne_yakin"].fillna("False", inplace=True)
houses["bogaz_koprulerine_yakin"].fillna("False", inplace=True)

houses["bulundugu_kat"].fillna("1", inplace=True)
houses["kat_sayisi"].fillna("1", inplace=True)

def aidat_p(x):
    if pd.isnull(x["aidat"]):
        return x["aidat"]
    return x["aidat"].replace("tl", '').split()[0]

houses["aidat"] = houses.apply(aidat_p, axis=1)
houses["aidat"] = houses["aidat"].astype(float)
houses["aidat"].fillna(value=houses['aidat'].mean(), inplace=True)



def by(x):
    if pd.isnull(x["bina_yasi"]) or x["bina_yasi"] != "sifir_bina":
        return x["bina_yasi"]
    return '0'

houses["bina_yasi"] = houses.apply(by, axis=1)
houses["bina_yasi"] = houses["bina_yasi"].astype(float)
houses["bina_yasi"].fillna(value=houses['bina_yasi'].mean(), inplace=True)







for col in houses.columns:
    print(houses[col])
    print(houses[col].unique(), end='\t')
    print(len(houses[col].unique()))
    input()
"""

f = lambda x: x["fiyat"].replace("tl", '').split()[0]

def s(x):
    if x["site_icerisinde"] != "True" and x["site_icerisinde"] != "False":
        return "True"

def bk(x):
    try:
        int(x["bulundugu_kat"])
        return x["bulundugu_kat"]
    except ValueError:
        if x["bulundugu_kat"] == "yüksek giris" or x["bulundugu_kat"] == "giris kati" or x["bulundugu_kat"] == "zemin" or x["bulundugu_kat"] == "teras kati":
            return "0"
        elif x["bulundugu_kat"] == "en ust kat" or x["bulundugu_kat"] == "cati kati":
            return x["kat_sayisi"]
        
        #elif x["bulundugu_kat"].startswith("kat"):
        #   return x["bulundugu_kat"][-1]
        #elif x["bulundugu_kat"].startswith("ara kat") == "ara kat":
        #    return "2"
        #else:
        #    return "0"

def ks(x):
    if x["kat_sayisi"] == "":
        return "1"
    else:
        return x["kat_sayisi"].split()[0]

def ed(x):
    if x["esya_durumu"] == "esyali":
        return "True"
    else:
        return "False"

def by(x):
    if x["bina_yasi"] == "sifir_bina":
        return "0"

print("dataset loading")
df = pd.read_csv("dataset.csv")

print("fiyat")
df["fiyat"] = df.apply(f, axis=1)
print("aidat")
print("kira_getirisi")
df["kira_getirisi"] = df.apply(f, axis=1)

df["bina_yasi"] == df.apply(by, axis=1)

print("site_icerisinde")
df["site_icerisinde"] = df.apply(s, axis=1)

print("kat_sayisi")
# df["kat_sayisi"] = df.apply(ks, axis=1)

df["esya_durumu"] = df.apply(ed, axis=1)

"""