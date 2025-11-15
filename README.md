🤖 AI FAQ Chatbot – CodeAlpha Internship

This project is an AI-powered FAQ Chatbot developed as part of the CodeAlpha Artificial Intelligence Internship.

The chatbot intelligently matches user questions against a predefined FAQ dataset using Natural Language Processing (NLP) techniques like Cosine Similarity.

It features a modern floating chat UI, complete with typing animation, timestamps, iMessage/WhatsApp-style chat bubbles, and a Royal Violet full-screen design.

🌟 Features

🧠 AI Chatbot

1. Matches user input with closest FAQ using cosine similarity

2. Highly accurate FAQ retrieval

3. Supports flexible, natural wording from users

4. Easy to expand by adding more questions

💬 Modern Chat UI

1. Full-screen chat interface

2. Floating chat button

3. iMessage / WhatsApp-like bubble design

4. Smooth animations

5. Typing indicator (animated dots)

6. Auto-scroll

7. Message timestamps

8. Mobile-friendly responsive UI

⚙️ Technical Features

1. JSON-based FAQ dataset

2. Fast similarity matching

3. Flask backend API

4. Clean JavaScript frontend

5. Easily deployable

📂 Project Structure

FAQ Chatbot/

│

├── static/

│   ├── css/

│   │   └── chatbot.css

│   └── js/

│       └── chatbot.js

│

├── templates/

│   └── chatbot.html

│

├── faq_data.json           # All 50–100 FAQs

├── app.py                  # Flask backend with cosine similarity

├── requirements.txt

└── README.md


Your file names may differ slightly, but this is the recommended structure.

⚙️ Installation & Setup

✔ 1. Clone the repository

git clone https://github.com/Antro845/CodeAlpha_FAQ_Chatbot.git

cd CodeAlpha_FAQ_Chatbot

✔ 2. Create a virtual environment

python -m venv venv

✔ 3. Activate virtual environment

Windows:

venv\Scripts\activate

✔ 4. Install dependencies

pip install -r requirements.txt

✔ 5. Run the Flask server

python app.py


Open your browser and visit:

👉 http://127.0.0.1:5000/

🔍 How It Works (NLP Logic)

1. User enters a question into the chat

2. The question is preprocessed

3. Cosine similarity is calculated between:

      1.User question

      2.All FAQ questions in the dataset

4. The highest similarity score determines the best match

5. Chatbot returns the corresponding answer

6. UI displays:

    1.User bubble

    2.Typing animation

    3.Bot bubble with timestamp

🧠 Tech Stack

Backend:

1. Python

2. Flask

3. NLTK / SpaCy (optional)

Cosine Similarity (sklearn)

1. Frontend:

2. HTML

3. CSS (Royal Violet Theme)

4. JavaScript (Fetch API)

Data:

1. JSON FAQ dataset

💬 UI Features Breakdown

✔ Floating Chat Button

Appears centered on screen → Opens full-screen chat UI.

✔ Full-Screen Chat Window

Smooth scale animation with dark purple theme.

✔ Chat Bubbles

User = right aligned (violet gradient)

Bot = left aligned (soft purple)

Rounded iMessage-style corners

✔ Typing Indicator

Animated three-dot bubble for realistic feel.

✔ Timestamps

Each message includes readable time format (e.g., 4:26 PM).

✔ Auto Scroll

Chat window scrolls automatically as messages appear.

📦 Requirements

All libraries used in this project are listed in:

requirements.txt


Install using:

pip install -r requirements.txt

🏅 About CodeAlpha Internship

This chatbot project was completed as part of the:

📌 CodeAlpha Artificial Intelligence Internship Program

It demonstrates practical skills in:

Natural Language Processing

Vector similarity

Frontend design

API development

UI/UX

Chat system engineering

📬 Contact

Developer: M. ANTRO PRATHIK SAM

GitHub: https://github.com/Antro845

⭐ Help this project grow!

If you found this chatbot useful, please ⭐ star the repository on GitHub.
