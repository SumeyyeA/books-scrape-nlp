import requests
from bs4 import BeautifulSoup
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np
from sentence_transformers import SentenceTransformer

BASE_URL = "https://books.toscrape.com/"


def scrape_books():
    books = []
    page = 1
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    while True:
        url = f"{BASE_URL}catalogue/page-{page}.html"
        try:
            response = requests.get(url, headers=headers, timeout=15) #bağlantım kötü olduğu için
            if response.status_code != 200:
                break

            soup = BeautifulSoup(response.content, 'html.parser')
            book_elements = soup.find_all('article', class_='product_pod')

            for book in book_elements:
                title = book.h3.a['title']
                rating = book.p.get('class')[1]  
                price = book.find('p', class_='price_color').text.strip()
                detail_url = BASE_URL + 'catalogue/' + book.h3.a['href']

                try:
                    detail_response = requests.get(detail_url, headers=headers, timeout=15)
                    detail_soup = BeautifulSoup(detail_response.content, 'html.parser')

                    description = detail_soup.find('meta', attrs={'name': 'description'})
                    description = description['content'].strip() if description else ""

                    stock_info = detail_soup.find('p', class_='instock availability').text.strip()
                    quantity = int(stock_info.split('(')[-1].split()[0]) if 'In stock' in stock_info else 0

                    books.append({
                        "title": title,
                        "rating": rating,
                        "price": price,
                        "description": description,
                        "stock_quantity": quantity
                    })
                except requests.exceptions.RequestException as e:
                    print(f"Detay sayfası hatası: {detail_url} - Hata: {e}")

            page += 1

        except requests.exceptions.RequestException as e:
            print(f"Sayfa hatası: {url} - Hata: {e}")
            break

    with open('books.json', 'w', encoding='utf-8') as f:
        json.dump(books, f, indent=4, ensure_ascii=False)
    print(f"{len(books)} kitap kaydedildi.")

# JSON dosyasındaki kitapları sayma

def count_books():
    try:
        with open('books.json', 'r', encoding='utf-8') as f:
            books = json.load(f)
        print(f"Toplam kitap sayısı: {len(books)}")
    except FileNotFoundError:
        print("books.json dosyası bulunamadı.")

# Açıklamalara göre kitapları gruplama

def group_books():
    try:
        with open('books.json', 'r', encoding='utf-8') as f:
            books = json.load(f)

        descriptions = [book['description'] for book in books if book['description']]
        model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
        embeddings = model.encode(descriptions)

        n_clusters = min(6, len(descriptions))
        model_kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        labels = model_kmeans.fit_predict(embeddings)

        groups = {}
        for i, label in enumerate(labels):
            key = int(label) if isinstance(label, (np.integer, int)) else label
            groups.setdefault(str(key), []).append(books[i]['title'])

        with open('book_groups.json', 'w', encoding='utf-8') as f:
            json.dump(groups, f, indent=4, ensure_ascii=False)
        print(f"Kitaplar {n_clusters} gruba ayrıldı ve kaydedildi.")

    except FileNotFoundError:
        print("dosya bulunamadı.")

if __name__ == "__main__":
    print("Scraping işlemi başladı.")
    scrape_books()
    print("Kitap sayımı yapılıyor.")
    count_books()
    print("Kitap açıklamalarına göre gruplama yapılıyor.")
    group_books()
    print("tamamlandı.")