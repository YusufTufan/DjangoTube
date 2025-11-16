# DjangoTube - Video Sharing Platform

## About The Project / Proje Hakkında

**EN:** DjangoTube is a robust web application developed to provide a high-quality video streaming and sharing service. This project mirrors the core functionalities of major video platforms like YouTube, built on a powerful and secure backend powered by the Django framework. The primary goal was to create a scalable and maintainable application that delivers a clean, intuitive, and engaging user experience.

-----

**TR:** DjangoTube, yüksek kaliteli bir video akışı ve paylaşım hizmeti sunmak amacıyla geliştirilmiş sağlam bir web uygulamasıdır. Bu proje, Django çatısının gücüyle desteklenen güvenli bir backend üzerinde, YouTube gibi büyük video platformlarının temel işlevlerini taklit etmektedir. Temel amaç, temiz, sezgisel ve ilgi çekici bir kullanıcı deneyimi sunan, ölçeklenebilir ve bakımı kolay bir uygulama oluşturmaktı.

## ✨ Key Features / ✨ Ana Özellikler

**EN:**

  - **🎥 Video Upload & Management:** Authenticated users can easily upload, process, and manage their video content.
  - **▶️ Seamless Playback:** A clean video detail page with an integrated HTML5 player for a smooth viewing experience.
  - **👤 User Authentication:** Secure user registration and login system.
  - **💬 Interactive Commenting:** Users can engage with content by posting comments.
  - **🔍 Powerful Search:** A search bar to quickly find videos by title.
  - **🎨 Clean & Responsive UI:** A user interface built with HTML5 and CSS for a consistent experience.

-----

**TR:**

  - **🎥 Video Yükleme & Yönetimi:** Kimliği doğrulanmış kullanıcılar video içeriklerini kolayca yükleyebilir ve yönetebilir.
  - **▶️ Sorunsuz Video Oynatma:** Sorunsuz bir izleme deneyimi için entegre HTML5 oynatıcılı video detay sayfası.
  - **👤 Kullanıcı Kimlik Doğrulama:** Güvenli kullanıcı kayıt ve giriş sistemi.
  - **💬 Etkileşimli Yorum Sistemi:** Kullanıcılar, yorum göndererek içerikle etkileşime girebilir.
  - **🔍 Güçlü Arama Fonksiyonu:** Videoları başlığa göre hızla bulmayı sağlayan arama çubuğu.
  - **🎨 Temiz ve Duyarlı Arayüz:** HTML5 ve CSS ile oluşturulmuş, cihazlar arasında tutarlı bir deneyim sağlayan arayüz.

## 🛠️ Tech Stack / 🛠️ Kullanılan Teknolojiler

**EN:**

  - **Backend:** Python, Django
  - **Frontend:** HTML5, CSS3
  - **Database:** SQLite 3
  - **Version Control:** Git & GitHub


## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following installed on your system:

  - Python 3.10 or higher
  - pip (Python package installer)
  - Git

### Installation

1.  **Clone the repository:**

    ```sh
    git clone https://github.com/YusufTufan/DjangoTube.git
    cd DjangoTube
    ```

2.  **Create and activate a virtual environment:**

    ```sh
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS / Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    *(Note: If you don't have a `requirements.txt` file yet, create one by running `pip freeze > requirements.txt` in your terminal.)*

    ```sh
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**

    ```sh
    python manage.py migrate
    ```

5.  **Create a superuser to access the admin panel:**

    ```sh
    python manage.py createsuperuser
    ```

6.  **Run the development server:**

    ```sh
    python manage.py runserver
    ```

    The application will be available at `http://127.0.0.1:8000/`.


### ✨ Modern React Versiyonu

**TR:** Bu proje, modern ve ayrıştırılmış bir mimariyle tamamen yeniden yazıldı! Bu yeni versiyon, backend için tam bir Django REST Framework API'si ve frontend için dinamik bir React arayüzü içermektedir.

**[➡️ Check out the DjangoTube React API Version Here](https://github.com/YusufTufan/DjangoTube-React-API)**


## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
