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
![Ekran görüntüsü 2025-02-19 015027](https://github.com/user-attachments/assets/d7f5650e-7c0c-4863-b642-10e34b24a271)
- `books.json`:
    {
        "title": "A Light in the Attic",
        "rating": "Three",
        "price": "£51.77",
        "description": "It's hard to imagine a world without A Light in the Attic.This..",
        "stock_quantity": 22
    },
- `book_groups.json`:
"2": [
        "A Light in the Attic",
        "The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics",
        "Shakespeare's Sonnets",
        "Olio",
     ]

### Ekran Görüntüleri
- `books.json`:![resim](https://github.com/user-attachments/assets/f0946cbf-607b-4563-8994-9a9b259d0b66)

- `book_groups.json`:![resim](https://github.com/user-attachments/assets/fe45df33-82dc-49bf-a4f0-3085d3b04a7a)![resim](https://github.com/user-attachments/assets/3518178d-daed-4796-abd3-3ca7fccd996c)



### Kaynaklar
Aşağıdaki projelerden fikir ve yardım alınmıştır :
https://www.kaggle.com/code/takanorihasebe/kmeans-recommendation
https://github.com/Vidito/webscraping_books
https://github.com/hmignon/P2_BooksToScrape/blob/main/scraper.py
https://www.kaggle.com/code/samson8/how-to-create-wikipedia-embeddings
