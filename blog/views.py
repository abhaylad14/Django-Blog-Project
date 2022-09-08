from django.shortcuts import render
from datetime import date
# Create your views here.

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "https://www.hindustantimes.com/web-stories/10-most-beautiful-mountains-in-the-world-641/assets/19.jpeg",
        "author": "Abhay",
        "date": date(2022, 9, 1),
        "title": "Mountain Hiking",
        "excert": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus optio iusto consectetur aut. Sit tenetur
        libero laboriosam. Deleniti doloribus itaque modi, est adipisci ratione, veritatis, sed impedit assumenda facere
        dignissimos.
        
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus optio iusto consectetur aut. Sit tenetur
        libero laboriosam. Deleniti doloribus itaque modi, est adipisci ratione, veritatis, sed impedit assumenda facere
        dignissimos.
        
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus optio iusto consectetur aut. Sit tenetur
        libero laboriosam. Deleniti doloribus itaque modi, est adipisci ratione, veritatis, sed impedit assumenda facere
        dignissimos."""
    }
]

def get_date(post):
    return post["date"]
 
def index(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts" : latest_posts})

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })