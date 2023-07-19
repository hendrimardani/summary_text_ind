### Cara Penggunaaan

pip install -r requirement.txt
```
python3 utama.py --file {lokasi file.txt} --model {lokasi model model_summary_ind.h5}
```
### Untuk keterangan selengkapnya
```
python3 utama.py --help
```
### Models
Dikarenakan file > 25mb, download model pre-trained [disini](https://drive.google.com/file/d/12mVdi-QeohhxxBv6cqKSZBNzugWnOPwf/view?usp=sharing)

### Tahap-tahap proses
1. Scraping data di https://www.liputan6.com/
2. Link data hasil scrap [disini](https://drive.google.com/file/d/1_xZdzOD5X_f_KHYfUIeqwv27HzDDeK4f/view?usp=drive_link)
3. Clearning data dengan Regex(Preprocessing data)
4. Tokenize data (Merubah data kedalam tensor matrix)
5. Split data (Membagi data training dan data test)
6. Training model
7. Tampilkan hasil training
8. Prediksi data
9. Evaluasi model (Menggunakan metrix Rogue-L F1-Score)
10. Save model yang sudah di training(pre-trained model)

##### NOTE
- Total **214794rb baris**
- Total setelah data bersih *clean data* **214184rb baris**
- Total Jam training **2.1 Jam(250 menit)**

### Referensi
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Regex](https://regexr.com/)
- [Liputan 6](https://www.liputan6.com/)
