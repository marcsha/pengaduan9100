import streamlit as st
import pandas as pd
from datetime import date, datetime
import time
from streamlit_js_eval import streamlit_js_eval
import gspread
from google.oauth2 import service_account
import json
import pytz

# Set Timezone
tzInfo = pytz.timezone('Asia/Jayapura')

# Setup Google Sheets API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = service_account.Credentials.from_service_account_file('isi-formpengaduan9100-44a5fb7650a2.json', scopes=scope)
client = gspread.authorize(creds)

# Buka Spreadsheet
sheet = client.open("db Groundcheck")
worksheet1 = sheet.worksheet('Sheet1')

# Baca Google Spreadsheet
sheet_url = "https://docs.google.com/spreadsheets/d/1dKKG4L40D-rQuWCKwymsRBkvALeq3KfgqqjEyDeOgkA/edit#gid=0"
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')

try:
    df = pd.read_csv(url_1, header=0, on_bad_lines='skip')
except Exception as e:
    df = pd.DataFrame()  # Buat dataframe kosong jika terjadi error

hari = date.today()

# Konfigurasi Streamlit
st.set_page_config(
    page_title="Form Pengaduan",
    page_icon="📋"
)

# UI Streamlit
st.markdown("<h1 style='text-align: center; color: green;'>Form Pelaporan Groundcheck</h1>", unsafe_allow_html=True)

# Input dari pengguna
nama = st.text_input('Nama Pelapor')
email = st.text_input('Email')
notelp = st.text_input('Nomor Telepon')
domisili = st.text_input('Alamat Domisili')
judul = st.text_input('Judul Laporan')
kategori = st.selectbox("Kategori", ["-PILIH-", "Peraturan", "Pelayanan Terpadu", "Pegawai", "Birokrasi", "Fasilitas", "Fraud/Kecurangan", "Pelayanan Umum", "Gratifikasi", "Benturan Kepentingan", "Lainnya"], 0)
isi = st.text_area('Isi Laporan')
bukti = st.text_input('Bukti Pengaduan')

# Tombol Submit
if st.button('Submit'):
    if nama and email and notelp and kategori != "-PILIH-" and isi:
        worksheet1.append_row([datetime.now(tz=tzInfo).isoformat(), nama, email, notelp, domisili, judul, kategori, isi, bukti])
        st.success('Data berhasil tersubmit!', icon="✅")
        time.sleep(3)
        streamlit_js_eval(js_expressions="parent.window.location.reload()")
    else:
        st.warning("Harap isi semua bidang yang diperlukan!", icon="⚠️")
