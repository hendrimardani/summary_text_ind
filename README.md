### How to use

pip install -r requirement.txt
```
python3 utama.py --file {path file.txt} --model {path model model_summary_ind.h5}
```
### Options
```
python3 utama.py --help
```
### Models
Due to files > 25mb, download model pre-trained [here](https://drive.google.com/file/d/12mVdi-QeohhxxBv6cqKSZBNzugWnOPwf/view?usp=sharing)

### Process stages
1. Scraping data in https://www.liputan6.com/
2. Link data results scrap [here](https://drive.google.com/file/d/1_xZdzOD5X_f_KHYfUIeqwv27HzDDeK4f/view?usp=drive_link)
3. Cleaning data with Regex (Preprocessing data)
4. Tokenize data (Convert data into tensor matrix)
5. Split data (Divide training data and test data)
6. Training model
7. Data prediction
8. Model evalutaion (Use metrix rogue-L f1-score)
9. Save model(Pre-trained model)

##### NOTE:

- Total **214794 thousand lines**
- Total *clean data* **214184 thousand baris**
- Total training hours **2,3 hours (150 minutes)**
- Loss = 1.6616 dan Val_loss = 1.4471, slightly overfitting. (can be again added data) 

### Referensi
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Regex](https://regexr.com/)
- [Liputan 6](https://www.liputan6.com/)

![vokoscreenNG-2023-07-19_14-28-04](https://github.com/hendrimardani/summary_text_ind/assets/49816104/5fefd6bd-7d38-4fe1-8761-951450fc60d8)



