# FMCW Radar

Aplikasi FMCW radar OmniPresence, aplikasi ini ditulis dengan python.
Digunakan untuk keperluan penelitian PUI-PT Intelligent Sensing Iot.


## Cara Penggunaan

1. Mengatur Nomor Port Radar
   ![image](https://github.com/rc-iot-telu/fmcw/assets/60130740/bb5d57c7-bc7e-4a3d-83e0-e7d69e40b28f)
   Buka tombol ```setting``` di pojok kiri aplikasi.
   
2. Masukan Nomor Port
   
   ![image](https://github.com/rc-iot-telu/fmcw/assets/60130740/a824cb85-f06c-49fc-af2b-fe858b5b3375)
   
   Di dalam kolom ```FMCW Port``` digunakan untuk mengatur nomor port aplikasi yang akan digunakan untuk
   berkomunikasi dengan radar. ```Detected Port``` merupakan kolom yang berisi semua nomor port yang terdeteksi
   oleh aplikasi. Untuk <b>input data</b> masukan <b>hanya</b> nomor port, contoh: ```COM13```. Biasanya
   nomor port radar, selalu diikuti oleh kata: ```USB Serial Device```.
   
3. Start dan Stop
   ![image](https://github.com/rc-iot-telu/fmcw/assets/60130740/06c20d5d-3795-43bb-b7f8-8511d685be16)
   Setelah mengatur nomor port, tekan tombol ```Start```. Jika plot berubah seperti gambar di atas, maka
   radar berjalan normal. Untuk menghentikan jalanya radar, tekan tombol ```Stop``` di pojok kiri atas.
   
5. Save Data
   Setelah menghentikan radar, tekan tombol ```Save Data```, secara default data tersebut akan terimpan di
   dalam folder ```Documents``` masing - masing komputer. Lebih tepatnya tersimpan di dalam folder: ```Documents\phase```
   untuk data <b>phase</b>, sedangkan untuk data magnitude ada di lokasi: ```Documents\magnitude```.
