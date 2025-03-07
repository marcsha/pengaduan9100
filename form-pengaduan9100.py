import streamlit as st
import pandas as pd
from datetime import date
import time
from streamlit_js_eval import streamlit_js_eval
import gspread
import streamlit as st
from google.oauth2 import service_account
from oauth2client.service_account import ServiceAccountCredentials
from gsheetsdb import connect
import datetime
import json
import pytz

tzInfo = pytz.timezone('Asia/Jayapura')
# Create a connection object.
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('isi-formpengaduan9100-44a5fb7650a2.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("db Groundcheck")
worksheet1 = sheet.worksheet('Sheet1')

## Membaca db asal
sheet_url = "https://docs.google.com/spreadsheets/d/1dKKG4L40D-rQuWCKwymsRBkvALeq3KfgqqjEyDeOgkA/edit#gid=0"
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')

df = pd.read_csv(url_1, header=0, on_bad_lines='skip')
#df["ID SLS"] = df["ID SLS"].astype(str)
hari = date.today()

         
st.set_page_config(
         page_title="Form Pengaduan",
         page_icon="📋"
)

if __name__ == "__main__":

    st.markdown("<h1 style='text-align: center; color: green;'>Form Pelaporan Groundcheck</h1>", unsafe_allow_html=True)
    #st.subheader(f"Tanggal: {hari}")
    #st.dataframe(df)


    nama = st.text_input('Nama Pelapor', )
    email = st.text_input('Email', )
    notelp = st.text_input('Nomor Telepon', )
    domisili = st.text_input('Alamat Domisili', )
    judul = st.text_input('Judul Laporan', )
    kategori = st.selectbox("Kategori ", ["-PILIH-", "Peraturan","Pelayanan Terpadu","Pegawai","Birokrasi","Fasilitas","Fraud/Kecurangan","Pelayanan Umum","Gratifikasi","Benturan Kepentingan", "Lainnya"], 0)
    isi = st.text_input('Isi Laporan', )
    bukti = st.text_input('Bukti Pengaduan', )

if st.button('Submit'):
         st.success(f'Data berhasil tersubmit', icon="✅")
         worksheet1.append_row([datetime.datetime.now(tz=tzInfo).isoformat(), FirstFilter, SecondFilter, ThirdFilter, JumlahL2])
         time.sleep(3)
         streamlit_js_eval(js_expressions="parent.window.location.reload()")
         
