import os
import re
import pandas as pd
import numpy as np
import random

if True:
    all_data = list()

    for file_name in os.listdir("real_estate_scraper"):
        if file_name.endswith(".csv"):
            data = pd.read_csv(os.path.join("real_estate_scraper", file_name), dtype="unicode")
            print(f"File name -> {file_name}\tdataset len -> {len(data)}")
            all_data.append(data)

    houses = pd.concat(all_data)
    houses = houses.drop_duplicates()

    # houses.to_csv("concatted_df.csv", index=False)

    print("Datasets concatted")


    def esya_d(x):
        return "True" if x["esya_durumu"] == "esyali" else "False"

    houses["esya_durumu"].fillna("esyali degil", inplace=True)
    houses["esya_durumu"] = houses.apply(esya_d, axis=1)

    def kat_m(x):
        val = x["tapu_durumu"]
        if val == "arsa":
            return "0"
        return "1"
    houses["tapu_durumu"].fillna("1", inplace=True)
    houses["tapu_durumu"] = houses.apply(kat_m, axis=1)

    # houses["il"].fillna("", inplace=True)
    # houses["ilce"].fillna("", inplace=True)
    # houses["mahalle"].fillna("", inplace=True)
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
    houses["su_deposu"].fillna("False", inplace=True)
    houses["tenis_kortu"].fillna("False", inplace=True)
    houses["yangin_merdiveni"].fillna("False", inplace=True)
    houses["yuzme_havuzu"].fillna("False", inplace=True)
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


    # houses.to_csv("lot_of_fillna_applied.csv", index=False)

    # houses["bulundugu_kat"].fillna("1", inplace=True)
    # houses["kat_sayisi"].fillna("1", inplace=True)
if True:
    # houses = pd.read_csv("lot_of_fillna_applied.csv")

    print("2nd PART")

    def aidat_p(x):
        val = x["aidat"]
        if pd.isnull(val):
            return val
        if "gbp" in val:
            return str(int(val.replace("gbp", '').split()[0].replace(',', '')) * 10)
        if "usd" in val:
            return str(int(val.replace("usd", '').split()[0].replace(',', '')) * 7.5)
        return val.replace("tl", '').split()[0].replace(',', '')

    houses["aidat"] = houses.apply(aidat_p, axis=1)
    houses["aidat"] = houses["aidat"].astype(float)
    houses["aidat"].fillna(value=int(houses[houses["aidat"] < 10000]["aidat"].mean()), inplace=True)
    # houses["aidat"] = houses["aidat"].astype(int)

    aidat_mean = houses[houses["aidat"] < 10000]["aidat"].mean()
    houses.loc[houses["aidat"] > 10000, "aidat"] = aidat_mean

    print("aidat -- DONE")


    def by(x):
        if pd.isnull(x["bina_yasi"]):
            return x["bina_yasi"]

        if x["bina_yasi"] == "sifir bina":
            return "0"

        return x["bina_yasi"].replace(',', '')

    houses["bina_yasi"] = houses.apply(by, axis=1)
    houses["bina_yasi"] = houses["bina_yasi"].astype(float).astype(int)
    houses["bina_yasi"].fillna(value=int(houses['bina_yasi'].mean()), inplace=True)
    houses["bina_yasi"] = houses["bina_yasi"].astype(int)

    print("bina_yasi -- DONE")

    houses["banyo_sayisi"] = houses["banyo_sayisi"].astype(float)
    houses["banyo_sayisi"].fillna(value=houses['banyo_sayisi'].mean(), inplace=True)
    houses["banyo_sayisi"] = houses["banyo_sayisi"].astype(int)

    print("banyo_sayisi -- DONE")

    def bm(x):
        if isinstance(x["brut_m2"], str):
            return x["brut_m2"].replace(',', '')
        return x["brut_m2"]

    houses["brut_m2"] = houses.apply(bm, axis=1)
    houses["brut_m2"] = houses["brut_m2"].astype(float)
    houses["brut_m2"].fillna(value=houses['brut_m2'].mean(), inplace=True)
    houses["brut_m2"] = houses["brut_m2"].astype(int)

    print("brut_m2 -- DONE")

    def nm(x):
        if pd.isnull(x["net_m2"]):
            return x["net_m2"]
        if isinstance(x["net_m2"], str):
            if x["net_m2"] == "belirtilmemis":
                return str(random.randint(50, 150))
            return x["net_m2"].replace(',', '')
        return x["net_m2"]

    houses["net_m2"] = houses.apply(nm, axis=1)
    houses["net_m2"] = houses["net_m2"].astype(float)
    houses["net_m2"].fillna(value=houses['net_m2'].mean(), inplace=True)
    houses["net_m2"] = houses["net_m2"].astype(int)

    print("net_m2 -- DONE")

    def ks(x):
        if pd.isnull(x["kat_sayisi"]):
            return x["kat_sayisi"]
        if "katli" in x["kat_sayisi"]:
            return x["kat_sayisi"].split()[0]
        return x["kat_sayisi"]


    houses["kat_sayisi"] = houses.apply(ks, axis=1)
    houses["kat_sayisi"] = houses["kat_sayisi"].astype(float)
    houses["kat_sayisi"].fillna(value=houses['kat_sayisi'].mean(), inplace=True)
    houses["kat_sayisi"] = houses["kat_sayisi"].astype(int)

    def bk(x):
        if pd.isnull(x["bulundugu_kat"]) or isinstance(x["bulundugu_kat"], int):
            return x["bulundugu_kat"]

        if x["bulundugu_kat"] in ["yuksek giris", "giris kati", "zemin", "bahce kati"]:
            return "0"
        
        if x["bulundugu_kat"] in ["en ust kat", "cati kati", "villa kati", "teras kati"]:
            return x["kat_sayisi"]
        
        if x["bulundugu_kat"] == "ara kat":
            return random.randint(1, int(x["kat_sayisi"]))

        if x["bulundugu_kat"] in ["yari bodrum", "bodrum", "bodrum ve zemin"]:
            return "-1"
        
        if "ve uzeri" in x["bulundugu_kat"]:
            return x["bulundugu_kat"].split()[0]
        
        if "kot" in x["bulundugu_kat"]:
            return x["bulundugu_kat"].split()[-1]

        return x["bulundugu_kat"]


    houses["bulundugu_kat"] = houses.apply(bk, axis=1)
    houses["bulundugu_kat"] = houses["bulundugu_kat"].astype(float)
    houses["bulundugu_kat"].fillna(value=houses['bulundugu_kat'].mean(), inplace=True)
    houses["bulundugu_kat"] = houses["bulundugu_kat"].astype(int)

    print("bulundugu_kat -- DONE")

    # BRUT(FLOAT) - NET(OBJECT) - FIYAT(OBJECT) - AIDAT(FLOAT) - KIRA(USD - EUR - GBP - TL) - DEPOZITO(FLOAT) FILLNA
    # ODA SAYISI - SALON SAYISI
    # son_guncelleme_tarihi



    def kuzey(x,):
        if pd.isnull(x["cephe"]):
            return False
        return "kuzey" in x["cephe"]
        
    def guney(x,):
        if pd.isnull(x["cephe"]):
            return False
        return "guney" in x["cephe"]

    def dogu(x,):
        if pd.isnull(x["cephe"]):
            return False
        return "dogu" in x["cephe"]

    def bati(x,):
        if pd.isnull(x["cephe"]):
            return False
        return "bati" in x["cephe"]

    houses["kuzey_cephe"]   = houses.apply(kuzey, axis=1)
    houses["kuzey_cephe"]   = houses["kuzey_cephe"].astype(int)

    print("Kuzey applied")

    houses["guney_cephe"]   = houses.apply(guney, axis=1)
    houses["guney_cephe"]   = houses["guney_cephe"].astype(int)

    print("Guney applied")

    houses["dogu_cephe"]    = houses.apply(dogu, axis=1)
    houses["dogu_cephe"]    = houses["dogu_cephe"].astype(int)
    print("Dogu applied")

    houses["bati_cephe"]    = houses.apply(bati, axis=1)
    houses["bati_cephe"]    = houses["bati_cephe"].astype(int)
    print("Batı applied")


    houses.drop("cephe", axis=1, inplace=True)
    print("Old cephe column deleted")


    houses.to_csv("save_point.csv", index=False)

    def fiyat_p(x):
        if pd.isnull(x["fiyat"]):
            return x["fiyat"]
        return x["fiyat"].split()[0].replace(',', '')

    houses["fiyat"] = houses.apply(fiyat_p, axis=1)
    houses["fiyat"] = houses["fiyat"].astype(float)
    houses["fiyat"].fillna(value=houses['fiyat'].mean(), inplace=True)
    

    print(houses[houses["fiyat"] < 0])

    print("fiyat -- DONE")


    def kira_p(x):
        val = x["kira_getirisi"]
        if pd.isnull(val):
            return val
        if "gbp" in val:
            return str(int(val.replace("gbp", '').split()[0].replace(',', '')) * 10)
        if "usd" in val:
            return str(int(val.replace("usd", '').split()[0].replace(',', '')) * 7.5)
        if "eur" in val:
            return str(int(val.replace("eur", '').split()[0].replace(',', '')) * 9)
        return val.replace("tl", '').split()[0].replace(',', '')

    houses["kira_getirisi"] = houses.apply(kira_p, axis=1)
    houses["kira_getirisi"] = houses["kira_getirisi"].astype(float)
    houses["kira_getirisi"].fillna(value=houses['kira_getirisi'].mean(), inplace=True)

    print("kira_getirisi -- DONE")


    def depozito_p(x):
        if pd.isnull(x["depozito"]):
            return x["depozito"]
        if "usd" in x["depozito"]:
            return str(int(x["depozito"].replace("usd", '').split()[0].replace(',', '')) * 7.5)
        return x["depozito"].replace("tl", '').split()[0].replace(',', '')


    houses["depozito"] = houses.apply(depozito_p, axis=1)
    houses["depozito"] = houses["depozito"].astype(float)
    houses["depozito"].fillna(value=houses['depozito'].mean(), inplace=True)

    print("depozito  -- DONE")


    houses["isinma_tipi"].fillna("isinma yok", inplace=True)
    print("isinma_tipi  --  DONE")




    def kredi_u(x):
        return "1" if x["krediye_uygunluk"] == "uygun" else "0"

    houses["krediye_uygunluk"].fillna("False", inplace=True)
    houses["krediye_uygunluk"] = houses.apply(kredi_u, axis=1)
    houses["krediye_uygunluk"] = houses["krediye_uygunluk"].astype(int)

    print("krediye_uygunluk  -- DONE")

    def site_i(x):
        return "0" if x["site_icerisinde"] in ["False", "hayir"] else "1"

    houses["site_icerisinde"].fillna("False", inplace=True)
    houses["site_icerisinde"] = houses.apply(site_i, axis=1)
    houses["site_icerisinde"] = houses["site_icerisinde"].astype(int)

    print("site_icerisinde  -- DONE")

    def guncelleme_t(x):
        if x["son_guncelleme_tarihi"] == "dun":
            return "1"
        if x["son_guncelleme_tarihi"] == "bugun":
            return "0"
        return x["son_guncelleme_tarihi"].split()[0]

    houses["son_guncelleme_tarihi"] = houses.apply(guncelleme_t, axis=1)
    houses["son_guncelleme_tarihi"] = houses["son_guncelleme_tarihi"].astype(int)

    print("son_guncelleme_tarihi  -- DONE")


    def yapi_d(x):
        return "0" if x["yapinin_durumu"] == "ikinci el" else "1"

    houses["yapinin_durumu"].fillna("sifir", inplace=True)
    houses["yapinin_durumu"] = houses.apply(yapi_d, axis=1)
    houses["yapinin_durumu"] = houses["yapinin_durumu"].astype(int)

    houses["yapi_tipi"].fillna("betonarme", inplace=True)

    houses["yakit_tipi"].fillna("yok", inplace=True)




    def takas(x):
        if x["takas"] != "evet":
            return "0"
        return "1"

    houses["takas"].fillna("Yok", inplace=True)
    houses["takas"] = houses.apply(takas, axis=1)
    houses["takas"] = houses["takas"].astype(int)



    def kullanim_d(x):
        val = x["kullanim_durumu"]
        if val in ["bos", "belirtilmemis"]:
            return "0"
        if val == "ev sahibi oturuyor":
            return "1"
        return "2"
    
    houses["kullanim_durumu"].fillna("bos", inplace=True)
    houses["kullanim_durumu"] = houses.apply(kullanim_d, axis=1)
    houses["kullanim_durumu"] = houses["kullanim_durumu"].astype(int)


    houses.set_axis([re.sub('_+', '_', col) for col in houses.columns], axis=1, inplace=True)

    re_arranged_cols = houses.columns.tolist()
    re_arranged_cols.remove("fiyat")
    re_arranged_cols.append("fiyat")
    houses = houses[re_arranged_cols]


    print(houses.columns)

    houses.drop(houses.columns[0], axis=1, inplace=True)
    houses.drop("url", axis=1, inplace=True)
    houses.drop("ilan_no", axis=1, inplace=True)
    houses.drop("ilan_durumu", axis=1, inplace=True)
    houses.drop("konut_sekli", axis=1, inplace=True)


        
    for col in [col for col in houses.columns.tolist() if col not in ["il", "ilce", "mahalle", "esya_durumu", "isinma_tipi", "yakit_tipi", "yapi_tipi"]]:
        houses.loc[houses[col] == "True", col] = 1
        houses.loc[houses[col] == "False", col] = 0


if True:
    sehirler = pd.read_csv("sehirler.csv")

    trans_table = str.maketrans("ğĞıİöÖüÜşŞçÇ", "gGiIoOuUsScC")

    def o2i(x):
        return ''.join(x["nufus"].split('.'))

    def t2e(x):
        return x["sehir"].translate(trans_table).lower()


    sehirler["nufus"] = sehirler.apply(o2i, axis=1)
    sehirler["nufus"] = sehirler["nufus"].astype(int)
    sehirler["sehir"] = sehirler.apply(t2e, axis=1)

    sehirler.sort_values(by=["nufus"], inplace=True, ignore_index=True)

    evler = pd.read_csv("house_prices2.csv")

    def n2i(x):
        if x["il"] == "mersin(icel)":
            x["il"] = "mersin"
        if x["il"] == "k.k.t.c.":
            return 81
        return sehirler.index[sehirler["sehir"] == x["il"]][0]

    evler["il"] = evler.apply(n2i, axis=1)

    evler.to_csv("house_prices3.csv", index=False)

