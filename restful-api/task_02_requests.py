import requests
import csv


def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {r.status_code}")
    if r.status_code == 200:
        data = r.json()
        for index, value in enumerate(data):
            print(data[index]['title'])


def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        dictionary = []
        data = r.json()
        for index, value in enumerate(data):
            item = {
                "id": data[index]['id'],
                "title": data[index]['title'],
                "body": data[index]['body']
            }
            dictionary.append(item)
        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for item in dictionary:
                writer.writerow(item)
