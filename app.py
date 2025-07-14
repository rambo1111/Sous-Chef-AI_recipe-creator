import os
from flask import Flask, request, render_template, jsonify
import google.generativeai as genai
import json

# Configure Gemini API
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

# Initialize model (Gemini 1.5 Flash)
model = genai.GenerativeModel('gemini-1.5-flash')

# Flask app
app = Flask(__name__)

def create_recipe_prompt(ingredients, health_stats, dietary_restrictions, allergies):
    """Create a detailed prompt for the AI based on user inputs"""
    
    prompt = f"""
    You are a professional nutritionist and chef. Create a detailed, healthy recipe using the following information:

    AVAILABLE INGREDIENTS: {ingredients}

    HEALTH CONSIDERATIONS:
    """
    
    if health_stats.get('blood_pressure'):
        prompt += f"- Blood Pressure: {health_stats['blood_pressure']} (recommend low-sodium options)\n"
    
    if health_stats.get('blood_sugar'):
        prompt += f"- Blood Sugar Level: {health_stats['blood_sugar']} (recommend low-glycemic options)\n"
    
    if health_stats.get('cholesterol'):
        prompt += f"- Cholesterol Level: {health_stats['cholesterol']} (recommend heart-healthy options)\n"
    
    if dietary_restrictions:
        prompt += f"- Dietary Restrictions: {dietary_restrictions}\n"
    
    if allergies:
        prompt += f"- Allergies: {allergies}\n"
    
    prompt += """
    IMPORTANT: Please respond ONLY with valid JSON format. No additional text, explanations, or formatting outside the JSON structure.

    Provide the response in this exact JSON structure:
    {
        "recipe": {
            "name": "Recipe Name",
            "prep_time": "X minutes",
            "cook_time": "X minutes",
            "total_time": "X minutes",
            "servings": "X servings",
            "ingredients": [
                "ingredient 1 with measurement",
                "ingredient 2 with measurement"
            ],
            "instructions": [
                "Step 1 detailed instruction",
                "Step 2 detailed instruction"
            ],
            "health_tips": [
                "Health tip 1",
                "Health tip 2"
            ],
            "storage": "Storage instructions"
        },
        "nutritional_info": {
            "calories_per_serving": "X calories",
            "protein": "X grams",
            "carbs": "X grams",
            "fat": "X grams",
            "fiber": "X grams",
            "sodium": "X mg",
            "health_benefits": [
                "Health benefit 1",
                "Health benefit 2"
            ]
        },
        "recipe_facts": {
            "cuisine_type": "Cuisine type",
            "difficulty": "Easy/Medium/Hard",
            "meal_type": "Breakfast/Lunch/Dinner/Snack",
            "dietary_tags": ["tag1", "tag2"],
            "fun_facts": [
                "Interesting fact 1 about ingredients or cooking method",
                "Interesting fact 2 about nutritional benefits"
            ]
        }
    }

    Make sure the recipe is tailored to the health conditions and dietary needs mentioned above.
    """
    
    return prompt

@app.route("/", methods=["GET", "POST"])
def index():
    recipe_data = None
    error_message = None
    
    if request.method == "POST":
        # Get form data
        ingredients = request.form.get("ingredients", "")
        
        # Health stats (optional)
        health_stats = {
            'blood_pressure': request.form.get("blood_pressure", ""),
            'blood_sugar': request.form.get("blood_sugar", ""),
            'cholesterol': request.form.get("cholesterol", "")
        }
        
        dietary_restrictions = request.form.get("dietary_restrictions", "")
        allergies = request.form.get("allergies", "")
        
        if ingredients:
            try:
                # Create the prompt
                prompt = create_recipe_prompt(ingredients, health_stats, dietary_restrictions, allergies)
                
                # Generate response
                response = model.generate_content(prompt)
                response_text = response.text.strip()
                
                # Parse JSON response
                try:
                    recipe_data = json.loads(response_text)
                except json.JSONDecodeError:
                    # If JSON parsing fails, try to extract JSON from the response
                    import re
                    json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
                    if json_match:
                        recipe_data = json.loads(json_match.group())
                    else:
                        error_message = "Failed to parse recipe data. Please try again."
                
            except Exception as e:
                error_message = f"Error generating recipe: {str(e)}"
        else:
            error_message = "Please enter at least some ingredients to create a recipe."
    
    return render_template("index.html", recipe_data=recipe_data, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
