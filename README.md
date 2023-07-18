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
Dikarenakan file > 25mb, download model pre-trained disini [Link](https://drive.google.com/drive/folders/1nMbqrzNenaCwjQUPqgtJqWPxbgbFAdYV)

### Tahap-tahap proses
1. Scraping data di https://www.liputan6.com/
2. Clearning data(Preprocessing data)
3. Tokenize data (Merubah data kedalam tensor matrix)
4. Split data (Membagi data training dan data test)
5. Training model
6. Evaluasi model (Menggunakan metrix Rogue-L F1-Score)
7. Prediksi data
8. Save model yang sudah di training(pre-trained model)

- Total **90rb++ baris
- Total Jam training **110 menit
