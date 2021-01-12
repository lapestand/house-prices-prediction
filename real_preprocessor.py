import os
import re
import pandas as pd
import numpy as np
import random
import logging
import argparse

def aidat_p(x):
    val = x["aidat"]
    if pd.isnull(val):
        return val
    if "gbp" in val:
        return int(val.replace("gbp", '').split()[0].replace(',', '')) * 10
    if "usd" in val:
        return int(val.replace("usd", '').split()[0].replace(',', '')) * 7.5
    return int(val.replace("tl", '').split()[0].replace(',', ''))

def by(x):
    if pd.isnull(x["bina_yasi"]):
        return x["bina_yasi"]

    if x["bina_yasi"] == "sifir bina":
        return 0

    return x["bina_yasi"].replace(',', '')

def bm(x):
    if isinstance(x["brut_m2"], str):
        return int(x["brut_m2"].replace(',', ''))
    return x["brut_m2"]
    
def nm(x):
    if pd.isnull(x["net_m2"]):
        return x["net_m2"]
    if isinstance(x["net_m2"], str):
        if x["net_m2"] == "belirtilmemis":
            return str(random.randint(50, 150))
        return x["net_m2"].replace(',', '')
    return x["net_m2"]

def ks(x):
    if pd.isnull(x["kat_sayisi"]):
        return x["kat_sayisi"]
    if "katli" in x["kat_sayisi"]:
        return x["kat_sayisi"].split()[0]
    return x["kat_sayisi"]

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

def kuzey(x):
    if pd.isnull(x["cephe"]):
        return False
    return "kuzey" in x["cephe"]
    
def guney(x):
    if pd.isnull(x["cephe"]):
        return False
    return "guney" in x["cephe"]

def dogu(x):
    if pd.isnull(x["cephe"]):
        return False
    return "dogu" in x["cephe"]

def bati(x):
    if pd.isnull(x["cephe"]):
        return False
    return "bati" in x["cephe"]

def fiyat_p(x):
    return int(x["fiyat"].split()[0].replace(',', ''))

def kira_p(x):
    val = x["kira_getirisi"]
    if pd.isnull(val):
        return val
    if "gbp" in val:
        return int(val.replace("gbp", '').split()[0].replace(',', '')) * 10
    if "usd" in val:
        return int(val.replace("usd", '').split()[0].replace(',', '')) * 7.5
    if "eur" in val:
        return int(val.replace("eur", '').split()[0].replace(',', '')) * 9
    return int(val.replace("tl", '').split()[0].replace(',', ''))

def depozito_p(x):
    if pd.isnull(x["depozito"]):
        return x["depozito"]
    if "usd" in x["depozito"]:
        return int(x["depozito"].replace("usd", '').split()[0].replace(',', '')) * 7.5
    return int(x["depozito"].replace("tl", '').split()[0].replace(',', ''))

def kredi_u(x):
    return 1 if x["krediye_uygunluk"] == "uygun" else 0

def site_i(x):
    return 0 if x["site_icerisinde"] in ["False", "hayir"] else 1

def guncelleme_t(x):
    if x["son_guncelleme_tarihi"] == "dun":
        return 1
    if x["son_guncelleme_tarihi"] == "bugun":
        return 0
    return int(x["son_guncelleme_tarihi"].split()[0])

def yapi_d(x):
    return 0 if x["yapinin_durumu"] == "ikinci el" else 1

def takas(x):
    if x["takas"] != "evet":
        return 0
    return 1

def kullanim_d(x):
    val = x["kullanim_durumu"]
    if val in ["bos", "belirtilmemis"]:
        return 0
    if val == "ev sahibi oturuyor":
        return 1
    return 2

def o2i(x):
    return ''.join(x["nufus"].split('.'))

def t2e(x):
    trans_table = str.maketrans("ğĞıİöÖüÜşŞçÇ", "gGiIoOuUsScC")
    return x["sehir"].translate(trans_table).lower()


class Preprocessor:
    def __init__(self):
        self.houses = None
        self.bool_attributes =["adsl", "ahsap_dograma", "alarm", "ankastre_mutfak", "arka_cephe",
            "asansor", "avrasya_tuneli_ne_yakin", "bahceli", "balkon", "barbeku",
            "beyaz_esyali", "bogaz_koprulerine_yakin", "cadde_uzerinde", "caddeye_yakin",
            "cam_mozaik_kaplama", "camasir_odasi", "celik_kapi", "deniz_ulasimina_yakin",
            "denize_sifir", "denize_yakin", "dusakabin", "duvar_kagidi", "e_5_e_yakin",
            "ebeveyn_banyolu", "esya_durumu", "fitness", "giyinme_odasi", "gomme_dolap",
            "goruntulu_diafon", "guvenlik", "hali_kaplama", "havaalanina_yakin", "hazir_mutfak",
            "hidrofor", "hilton_banyo", "isi_yalitim", "isicam", "jakuzi", "jenerator",
            "kablo_tv_uydu", "kapali_balkon", "kapici", "kartonpiyer", "klima", "laminant_mutfak",
            "manzara", "manzara___bogaz", "manzara___deniz", "manzara___doga", "manzara___gol",
            "manzara___sehir", "marley", "marmaraya_yakin", "merkezde", "mermer_zemin",
            "metrobuse_yakin", "metroya_yakin", "minibus___dolmusa_yakin", "mobilyali",
            "mutfak_dogalgazi", "on_cephe", "otobana_yakin", "otopark___acik",
            "otopark___kapali", "oyun_parki", "panel_kapi", "panjur", "parke",
            "parke___laminant", "parke___lamine", "pvc_dograma", "saten_alci",
            "saten_boya", "sauna", "seramik_zemin", "siding", "site_icerisinde",
            "somine", "spot_isik", "su_deposu", "takas", "tem_e_yakin", "tenis_kortu",
            "teras", "toplu_ulasima_yakin", "tramvaya_yakin", "vestiyer", "yangin_merdiveni",
            "yerden_isitma", "yuzme_havuzu"]
        logging.info(f"Len of boolean attributes --> {len(self.bool_attributes)}")
        logging.info("Preprocessor initiliazed")

    def preprocess(self):
        # Define datasets path
        datasets = [os.path.join("real_estate_scraper", data) for data in os.listdir("real_estate_scraper") if data.endswith(".csv")]

        # Concat sub-datasets
        self.houses = self.concat_datasets(datasets)
        logging.info("Datasets concatted")

        self.houses.dropna(subset = ["fiyat"], inplace=True)
        self.houses.drop("url", axis=1, inplace=True)
        self.houses.drop("ilan_no", axis=1, inplace=True)
        self.houses.drop("ilan_durumu", axis=1, inplace=True)
        self.houses.drop("konut_sekli", axis=1, inplace=True)

        # Drop duplicates
        logging.debug(f"Len before drop_duplicates() --> {len(self.houses)}")
        self.houses.drop_duplicates(inplace=True)
        logging.info("Duplicates dropped")
        logging.debug(f"Len after drop_duplicates() --> {len(self.houses)}")

        # Fill missing values for boolean attributes
        
        self.houses[self.bool_attributes] = self.houses[self.bool_attributes].fillna(0)
        logging.info("Boolean attributes' missing value filled with 0")

        self.nominal2numeric()
        
        self.houses["aidat"] = self.houses.apply(aidat_p, axis=1)
        self.houses["aidat"] = self.houses["aidat"].astype(float)
        self.houses["aidat"].fillna(value=int(self.houses[self.houses["aidat"] < 10000]["aidat"].mean()), inplace=True)
        self.houses["aidat"] = self.houses["aidat"].astype(int)
        self.houses.loc[self.houses["aidat"] > 10000, "aidat"] = self.houses[self.houses["aidat"] < 10000]["aidat"].mean()



        self.houses["bina_yasi"] = self.houses.apply(by, axis=1)
        self.houses["bina_yasi"] = self.houses["bina_yasi"].astype(float)
        self.houses["bina_yasi"].fillna(value=int(self.houses['bina_yasi'].mean()), inplace=True)
        self.houses["bina_yasi"] = self.houses["bina_yasi"].astype(int)


        self.houses["banyo_sayisi"] = self.houses["banyo_sayisi"].astype(float)
        self.houses["banyo_sayisi"].fillna(value=self.houses['banyo_sayisi'].mean(), inplace=True)
        self.houses["banyo_sayisi"] = self.houses["banyo_sayisi"].astype(int)

        

        self.houses["brut_m2"] = self.houses.apply(bm, axis=1)
        self.houses["brut_m2"] = self.houses["brut_m2"].astype(float)
        self.houses["brut_m2"].fillna(value=self.houses['brut_m2'].mean(), inplace=True)
        self.houses["brut_m2"] = self.houses["brut_m2"].astype(int)


        

        self.houses["net_m2"] = self.houses.apply(nm, axis=1)
        self.houses["net_m2"] = self.houses["net_m2"].astype(float)
        self.houses["net_m2"].fillna(value=self.houses['net_m2'].mean(), inplace=True)
        self.houses["net_m2"] = self.houses["net_m2"].astype(int)


        


        self.houses["kat_sayisi"] = self.houses.apply(ks, axis=1)
        self.houses["kat_sayisi"] = self.houses["kat_sayisi"].astype(float)
        self.houses["kat_sayisi"].fillna(value=self.houses['kat_sayisi'].mean(), inplace=True)
        self.houses["kat_sayisi"] = self.houses["kat_sayisi"].astype(int)


        self.houses["bulundugu_kat"] = self.houses.apply(bk, axis=1)
        self.houses["bulundugu_kat"] = self.houses["bulundugu_kat"].astype(float)
        self.houses["bulundugu_kat"].fillna(value=self.houses['bulundugu_kat'].mean(), inplace=True)
        self.houses["bulundugu_kat"] = self.houses["bulundugu_kat"].astype(int)



        self.houses["kuzey_cephe"]   = self.houses.apply(kuzey, axis=1)
        self.houses["kuzey_cephe"]   = self.houses["kuzey_cephe"].astype(int)

        print("Kuzey applied")

        self.houses["guney_cephe"]   = self.houses.apply(guney, axis=1)
        self.houses["guney_cephe"]   = self.houses["guney_cephe"].astype(int)

        print("Guney applied")

        self.houses["dogu_cephe"]    = self.houses.apply(dogu, axis=1)
        self.houses["dogu_cephe"]    = self.houses["dogu_cephe"].astype(int)

        print("Dogu applied")

        self.houses["bati_cephe"]    = self.houses.apply(bati, axis=1)
        self.houses["bati_cephe"]    = self.houses["bati_cephe"].astype(int)

        print("Batı applied")


        self.houses.drop("cephe", axis=1, inplace=True)
        print("Old cephe column deleted")



        self.houses["fiyat"] = self.houses.apply(fiyat_p, axis=1)

        

        self.houses["kira_getirisi"] = self.houses.apply(kira_p, axis=1)
        self.houses["kira_getirisi"].fillna(value=int(self.houses['kira_getirisi'].mean()), inplace=True)


        self.houses["depozito"] = self.houses.apply(depozito_p, axis=1)
        self.houses["depozito"].fillna(value=int(self.houses['depozito'].mean()), inplace=True)

        self.houses["isinma_tipi"].fillna("isinma yok", inplace=True)


        self.houses["krediye_uygunluk"].fillna("False", inplace=True)
        self.houses["krediye_uygunluk"] = self.houses.apply(kredi_u, axis=1)
        self.houses["krediye_uygunluk"] = self.houses["krediye_uygunluk"].astype(int)

        
        self.houses["site_icerisinde"].fillna("False", inplace=True)
        self.houses["site_icerisinde"] = self.houses.apply(site_i, axis=1)
        self.houses["site_icerisinde"] = self.houses["site_icerisinde"].astype(int)

        

        self.houses["son_guncelleme_tarihi"] = self.houses.apply(guncelleme_t, axis=1)
        self.houses["son_guncelleme_tarihi"] = self.houses["son_guncelleme_tarihi"].astype(int)


        self.houses["yapinin_durumu"].fillna("sifir", inplace=True)
        self.houses["yapinin_durumu"] = self.houses.apply(yapi_d, axis=1)
        self.houses["yapinin_durumu"] = self.houses["yapinin_durumu"].astype(int)

        self.houses["yapi_tipi"].fillna("betonarme", inplace=True)

        self.houses["yakit_tipi"].fillna("yok", inplace=True)

        
        self.houses["takas"].fillna("Yok", inplace=True)
        self.houses["takas"] = self.houses.apply(takas, axis=1)
        self.houses["takas"] = self.houses["takas"].astype(int)

        
    
        self.houses["kullanim_durumu"].fillna("bos", inplace=True)
        self.houses["kullanim_durumu"] = self.houses.apply(kullanim_d, axis=1)
        self.houses["kullanim_durumu"] = self.houses["kullanim_durumu"].astype(int)


        self.houses.set_axis([re.sub('_+', '_', col) for col in self.houses.columns], axis=1, inplace=True)

        re_arranged_cols = self.houses.columns.tolist()
        re_arranged_cols.remove("fiyat")
        re_arranged_cols.append("fiyat")
        self.houses = self.houses[re_arranged_cols]

            
        # for col in [col for col in houses.columns.tolist() if col not in ["il", "ilce", "mahalle", "esya_durumu", "isinma_tipi", "yakit_tipi", "yapi_tipi"]]:
        #    houses.loc[houses[col] == "True", col] = 1
        #    houses.loc[houses[col] == "False", col] = 0

        sehirler = pd.read_csv("sehirler.csv")

        sehirler["nufus"] = sehirler.apply(o2i, axis=1)
        sehirler["nufus"] = sehirler["nufus"].astype(int)
        sehirler["sehir"] = sehirler.apply(t2e, axis=1)

        sehirler.sort_values(by=["nufus"], inplace=True, ignore_index=True)


        def n2i(x):
            if x["il"] == "mersin(icel)":
                x["il"] = "mersin"
            if x["il"] == "k.k.t.c.":
                return 81
            return sehirler.index[sehirler["sehir"] == x["il"]][0]

        self.houses["il"] = self.houses.apply(n2i, axis=1)
        # self.houses.to_csv("house_prices.csv", index=False)
        # print(self.houses[[col for col in self.houses if col in self.bool_attributes]])

        for col in self.houses.columns:
            print(col)
            print(self.houses[col])
            input()

    def nominal2numeric(self):
        self.houses.loc[self.houses["esya_durumu"] == "esyali", "esya_durumu"] = 1
        self.houses.loc[self.houses["esya_durumu"] == "esyali degil", "esya_durumu"] = 0

        for bool_attr in self.bool_attributes:
            self.houses.loc[self.houses[bool_attr] == "hayir", bool_attr] = 0
            self.houses.loc[(self.houses[bool_attr] == "True") | (self.houses[bool_attr] == "Evet") | (self.houses[bool_attr] == "evet"), bool_attr] = 1
            # self.houses.loc[(self.houses[bool_attr] != 1) & (self.houses[bool_attr] != 0), bool_attr] = 1
        
        self.houses.loc[(self.houses["site_icerisinde"] != 1) & (self.houses["site_icerisinde"] != 0), "site_icerisinde"] = 1

        self.houses[self.bool_attributes] = self.houses[self.bool_attributes].astype(int)


    def concat_datasets(self, dataset_list):
        all_data = list()
        for dataset in dataset_list:
            data = pd.read_csv(dataset, dtype="unicode")
            all_data.append(data)
        return pd.concat(all_data)



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="House price prediction preprocessing script.")

    parser.add_argument("-V", help="Verbose mode", action="store_true")

    args = parser.parse_args()

    if args.V:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)

    os.system("clear" if os.name == "posix" else "cls")

    logging.info("Preprocessing started")
    preprocesor = Preprocessor()
    preprocesor.preprocess()
    



    # [nan, 'True', 'evet', 'hayir', "dslakf" ]
