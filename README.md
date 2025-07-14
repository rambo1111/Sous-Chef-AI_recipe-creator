# 🍳 Sous-Chef AI – Personalized Healthy Recipe Creator

[Live Demo 🚀](https://sous-chef-ai-recipe-creator.onrender.com)

[](https://www.youtube.com/watch?v=0fXcSyrjjgc)

Sous-Chef AI is an intelligent recipe generator that transforms your available ingredients, health stats, and dietary preferences into personalized, healthy, and delicious recipes – all powered by **Gemini API**.

---

## 🌟 Features

* **🥕 Ingredient-Based Recipes:** Enter ingredients you have, and get a full recipe tailored around them.
* **🏥 Health-Conscious Cooking:** Customize based on blood pressure, blood sugar, and cholesterol levels.
* **🌱 Dietary Filters:** Enter allergies or dietary restrictions like vegan, keto, gluten-free, etc.
* **📊 Nutritional Breakdown:** Includes calories, macros, fiber, and sodium per serving.
* **🧠 Fun Facts & Tags:** Learn interesting facts, meal type, cuisine, and difficulty levels.
* **🔥 Stylish UI:** Modern and responsive interface built with HTML, CSS, and JavaScript.
* **⚙️ Gemini-Powered Backend:** Uses Google Gemini 1.5 Flash API to dynamically generate accurate JSON-based recipes.

---

## 🛠️ Tech Stack

* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **Backend:** Python (Flask)
* **AI Model:** Google Gemini 1.5 Flash (via `google-generativeai`)
* **Deployment:** Render.com
* **API Integration:** Environment-based Gemini API key usage

---

## 📂 Project Structure

```bash
Sous-Chef-AI_recipe-creator/
├── app.py                  # Main Flask app
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Main UI template
├── static/
│   ├── styles.css          # App styling
│   ├── favicon.svg         # Favicon
│   └── github-mark.svg     # Github logo
└── README.md               # Readme
```

---

## 🧪 Getting Started (Local Setup)

1. **Clone the repository**

   ```bash
   git clone https://github.com/rambo1111/Sous-Chef-AI_recipe-creator.git
   cd Sous-Chef-AI_recipe-creator
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set your Gemini API key**

   ```bash
   export GEMINI_API_KEY=your_gemini_api_key  # Windows: set GEMINI_API_KEY=...
   ```

5. **Run the Flask app**

   ```bash
   python app.py
   ```

6. **Visit the app**
   Open your browser and go to: [http://localhost:5000](http://localhost:5000)

---

## 🚀 Deployment (Render)

1. Push your code to GitHub.
2. Create a new **Web Service** on [Render](https://render.com).
3. Add environment variable:

   * `GEMINI_API_KEY`: your API key from Google.
4. Use the following **start command**:

   ```bash
   gunicorn app:app
   ```

---

## 🔐 Environment Variables

| Key              | Description                    |
| ---------------- | ------------------------------ |
| `GEMINI_API_KEY` | Your API key for Google Gemini |

---

## 🧠 How It Works

1. **User Input:** The frontend collects ingredients, health data, and dietary preferences.
2. **Prompt Building:** A structured prompt is created combining all details.
3. **Gemini AI Call:** Sent to Gemini 1.5 Flash model using `google-generativeai`.
4. **Structured Output:** The model returns a strictly JSON-formatted recipe.
5. **Frontend Display:** Output is shown across three interactive tabs:

   * 🍽️ Recipe
   * 📊 Nutrition
   * 🧠 Facts

---

## ⚙️ Example Prompt

```json
AVAILABLE INGREDIENTS: chicken, broccoli, olive oil
HEALTH STATS: High Blood Pressure
DIETARY RESTRICTIONS: keto
ALLERGIES: dairy
```

Gemini returns a fully structured JSON like:

```json
{
  "recipe": {
    "name": "Keto Chicken Broccoli Stir Fry",
    ...
  },
  ...
}
```

---

## 📎 Dependencies

From `requirements.txt`:

```
flask
gunicorn
uvicorn
google-genai
google-generativeai
```

---

## 🧑‍💻 Author

**Vibhaw Kureel**

🔗 [GitHub](https://github.com/rambo1111)


---

## 🙌 Acknowledgements

* [Google Gemini](https://ai.google.dev)
* [Render](https://render.com)
* [Flask](https://flask.palletsprojects.com)

---
