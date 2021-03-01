# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 23:28:30 2021

@author: anjas amar pradana
@lisensi: sumber terbuka
@aliansi: universitas dian nuswantoro
"""

#Mengambil perpus modul hashlib untuk digunakan pada program
import hashlib

#Fungsi program hash_file
def hash_file(namafile):
    
    #Mengindex kode hash ke sha1
    h = hashlib.sha1()
    
    #Membuka namafile dengan chmod atau izin membaca sebagai file
    with open(namafile,'rb') as file:
        
        #Bingkah 0 untuk program menginisiasikan proses
        chunk = 0
        
        #Ketika Bingkah ada isinya maka
        while chunk != b'':
            
            #Bingkah = membaca file, dengan besaran binary 1024bit
            chunk = file.read(1024)
            
            #Lalu memperbarui Bingkah yang kosong
            h.update(chunk)
            
            #Dan kembali ke hexadigest
        return h.hexdigest()
    
    #Lalu menampilkan pesan file (ubah variable di bawah dengan file kamu di dalam folder).
    message= hash_file("Ubah-Dengan-File-Kamu.ekstensi")
    
    #Menampilkan hasil pesan dari file hash_file
    print(message)