import streamlit as st

class VirtualNutritionCoachApp:
    def __init__(self, user_profile):
        self.user_profile = user_profile

    def calculate_bmi(self):
        height_m = self.user_profile['height_cm'] / 100
        bmi = self.user_profile['weight_kg'] / (height_m ** 2)
        return round(bmi, 2)

    def daily_calorie_intake(self, meals):
        total_calories = sum(meal['calories'] for meal in meals)
        return total_calories

    def nutritional_options(self):
        return [
            "Increase intake of fruits and vegetables",
            "Choose whole grains over refined grains",
            "Limit processed foods and sugar",
            "Stay hydrated and avoid sugary drinks"
        ]

    def weight_loss_suggestions(self):
        return [
            "Eat smaller portions",
            "Exercise regularly (at least 30 minutes a day)",
            "Track your food intake",
            "Get adequate sleep"
        ]

    def recommend_supplements(self):
        return [
            "Multivitamins",
            "Omega-3 fatty acids",
            "Vitamin D",
            "Protein powders (for muscle gain)"
        ]

    def analyze_uploaded_study(self, study_text):
        if "cholesterol" in study_text.lower():
            return "The study discusses cholesterol levels. Consider limiting saturated fats."
        return "Study analyzed. No immediate recommendations."

    def fitness_routines(self):
        return {
            "Beginner": ["Walking", "Bodyweight exercises", "Stretching"],
            "Intermediate": ["Jogging", "Dumbbell workouts", "Yoga"],
            "Advanced": ["HIIT", "Weight training", "Cycling"]
        }

    def sports_advice(self):
        return [
            "Warm up before workouts",
            "Cool down and stretch after workouts",
            "Stay hydrated",
            "Maintain consistency in your routines"
        ]

    def suggest_free_exercise_resources(self):
        return {
            "Websites": [
                "https://www.fitnessblender.com",
                "https://www.darebee.com",
                "https://www.nerdfitness.com"
            ],
            "YouTube Channels": [
                "FitnessBlender",
                "HASfit",
                "Yoga With Adriene"
            ]
        }

# Streamlit App UI
st.title("🏋️ Virtual Nutrition Coach")
st.write("Welcome to your personal virtual nutritionist and fitness coach!")

st.sidebar.header("📋 User Profile")
height = st.sidebar.number_input("Height (cm)", min_value=100, max_value=250, value=170)
weight = st.sidebar.number_input("Weight (kg)", min_value=30, max_value=200, value=70)

app = VirtualNutritionCoachApp({'height_cm': height, 'weight_kg': weight})

if st.button("Calculate BMI"):
    bmi = app.calculate_bmi()
    st.success(f"Your BMI is: {bmi}")

st.header("🍽 Daily Calorie Intake")
meal1 = st.number_input("Meal 1 Calories", value=500)
meal2 = st.number_input("Meal 2 Calories", value=700)
if st.button("Calculate Total Calories"):
    total = app.daily_calorie_intake([{ 'calories': meal1 }, { 'calories': meal2 }])
    st.success(f"Total Calorie Intake: {total} kcal")

st.header("🥗 Nutritional Recommendations")
st.write("\n".join(app.nutritional_options()))

st.header("🔥 Weight Loss Tips")
st.write("\n".join(app.weight_loss_suggestions()))

st.header("💊 Supplement Suggestions")
st.write("\n".join(app.recommend_supplements()))

st.header("📄 Analyze a Study")
study_text = st.text_area("Paste study text here")
if st.button("Analyze Study") and study_text:
    result = app.analyze_uploaded_study(study_text)
    st.info(result)

st.header("💪 Fitness Routines")
routines = app.fitness_routines()
for level, routine in routines.items():
    st.markdown(f"**{level}**: {', '.join(routine)}")

st.header("🏀 Sports Advice")
st.write("\n".join(app.sports_advice()))

st.header("🌐 Free Resources")
resources = app.suggest_free_exercise_resources()
st.write("**Websites**:", ", ".join(resources["Websites"]))
st.write("**YouTube Channels**:", ", ".join(resources["YouTube Channels"]))
