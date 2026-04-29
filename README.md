# 🔗 URL Shortener & Analytics API

A fast, lightweight RESTful API built with Django that converts long URLs into short, manageable links and tracks click analytics in real-time. 

This project demonstrates core backend concepts including database modeling, URL routing, HTTP redirection, and API design.

## ✨ Features

* **URL Shortening:** Generates unique, random 6-character short codes for any valid URL.
* **Redirection:** Instantly redirects users from the short link to the original destination (HTTP 302).
* **Click Analytics:** Tracks the total number of clicks for each generated short link.
* **Idempotent Creation:** Returns the existing short code if the same original URL is submitted multiple times, preventing database bloat.

## 🛠️ Tech Stack

* **Backend Framework:** Python / Django
* **Database:** SQLite (Easily scalable to PostgreSQL)
* **Architecture:** RESTful API

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
* Python 3.x
* pip (Python package installer)

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR-USERNAME/url-shortener-api.git](https://github.com/YOUR-USERNAME/url-shortener-api.git)
   cd url-shortener-api