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
3. Cleaning data dengan Regex (Preprocessing data)
4. Tokenize data (Merubah data kedalam tensor matrix)
5. Split data (Membagi data training dan data test)
6. Training model
7. Prediksi data
8. Evaluasi model (Menggunakan metrix Rogue-L F1-Score)
9. Save model yang sudah di training(pre-trained model)

##### NOTE

- Total **214794rb baris**
- Total setelah data bersih *clean data* **214184rb baris**
- Total jam training **2,3 Jam (150 menit)**
- Loss = 1.6616 dan Val_loss = 1.4471, sedikit mengalami overfitting. (Bisa ditambahkan lagi datanya) 

### Referensi
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Regex](https://regexr.com/)
- [Liputan 6](https://www.liputan6.com/)

![vokoscreenNG-2023-07-19_14-28-04](https://github.com/hendrimardani/summary_text_ind/assets/49816104/5fefd6bd-7d38-4fe1-8761-951450fc60d8)



