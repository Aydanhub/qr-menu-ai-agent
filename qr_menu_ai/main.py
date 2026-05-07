import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from pydantic import BaseModel

app = FastAPI(title="QR Menü Akıllı Garson API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("HATA: API Anahtarı bulunamadı!")
    exit()

genai.configure(api_key=API_KEY)
uygun_modeller = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
model = genai.GenerativeModel(uygun_modeller[0])


restoran_menusu = {
    "corbalar": [{"isim": "Süzme Mercimek", "fiyat": 60, "etiketler": ["vegan", "sıcak", "glutensiz"]}],
    "ana_yemekler": [{"isim": "Izgara Tavuk Salata", "fiyat": 180, "etiketler": ["yüksek protein", "hafif", "glutensiz"]}],
    "tatlilar": [{"isim": "Fırın Sütlaç", "fiyat": 90, "etiketler": ["tatlı", "hafif", "glutensiz"]}],
    "icecekler": [{"isim": "Şekersiz Limonata", "fiyat": 45, "etiketler": ["soğuk", "vegan", "tatlı-ekşi"]}]
}
menu_metni = json.dumps(restoran_menusu, ensure_ascii=False, indent=2)

sistem_talimati = f"""
Sen lüks bir restoranın akıllı garsonusun. Sadece menüdeki ürünleri öner ve fiyatları topla.
GÜNCEL MENÜ: {menu_metni}
"""

sohbet = model.start_chat(history=[
    {"role": "user", "parts": [sistem_talimati]},
    {"role": "model", "parts": ["Anlaşıldı! Müşterilere harika tavsiyelerde bulunmak için hazırım."]}
])


app = FastAPI(title="QR Menü Akıllı Garson API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MusteriMesaji(BaseModel):
    mesaj: str

@app.post("/garsona-sor")
def garsonla_konus(istek: MusteriMesaji):
    cevap = sohbet.send_message(istek.mesaj)
    return {"garsonun_cevabi": cevap.text}