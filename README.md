### Proje Açıklaması
Bu proje, `Books to Scrape` sitesinden kitap verilerini çekmek, JSON formatında kaydetmek ve Kitapların açıklamalarına göre benzerliklerini hesaplayarak gruplandırmak için geliştirilmiştir. Projenin amacı, web scraping ve nlp teknikleri kullanarak kitapları gruplandırmaktır.

### Kullanılan Teknolojiler ve Bağımlılıklar
- **Python 3.11**
- **BeautifulSoup** - HTML parse etmek için
- **requests** - Web istekleri yapmak için
- **sentence-transformers** - `paraphrase-MiniLM-L6-v2` modelini kullanarak embedding işlemi için
- **scikit-learn** - KMeans ile gruplama yapmak için

### Kurulum

gerekli kütüphaneleri yükleyin:
pip install beautifulsoup4 requests sentence-transformers scikit-learn numpy


### Projeyi Çalıştırma

python main.py


### Örnek Çıktı Formatı


### Ekran Görüntüleri
- `books.json`:
- `book_groups.json`:

### Kaynaklar
Aşağıdaki projelerden fikir ve yardım alınmıştır :
https://www.kaggle.com/code/takanorihasebe/kmeans-recommendation
https://github.com/Vidito/webscraping_books
https://github.com/hmignon/P2_BooksToScrape/blob/main/scraper.py
https://www.kaggle.com/code/samson8/how-to-create-wikipedia-embeddings
