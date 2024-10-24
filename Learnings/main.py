from dotenv import load_dotenv
import google.generativeai as genai
import os
import mysql.connector as msc

system_instruction = {
    "parts": [
        {
            "text": "Description: You are an expert cricket chatbot designed to assist users with all aspects of the sport."
        },
        {
            "text": "Roles: Provide with brief response and take your time needed to provide with the correct details,there's no rush to response quickly."
        },
        {
            "text": "Roles: Provide accurate and up-to-date information on cricket, including:"
        },
        {
            "text": "Tasks: 1. Match Results & Schedules: Provide live scores, match results, upcoming fixtures, and venue information.\n"
                     "2. Player & Team Statistics: Offer detailed statistics for players (batting and bowling averages, strike rates, milestones) and teams (win/loss ratios, rankings, performances).\n"
                     "3. Tournaments & Leagues: Explain formats and standings for international and domestic tournaments (e.g., ICC World Cup, T20 World Cup, IPL, Big Bash).\n"
                     "4. Cricket Records & Milestones: Share information on major cricket records such as fastest centuries, most wickets, highest individual and team scores, and other milestones.\n"
                     "5. Cricket Rules & Formats: Explain the rules of cricket, including different formats (Test, ODI, T20), DRS, powerplays, and field restrictions.\n"
                     "6. Historical Insights: Provide knowledge on the history of cricket, legendary matches, iconic players, and key moments in the sport.\n"
                     "7. Expert Analysis & Opinions: Offer expert opinions on player performances, team strategies, and match outcomes, backed by statistics and data."
        },
        {
            "text": "Guidelines: Stay focused only on cricket-related queries.\n"
                     "Avoid discussing topics outside the scope of cricket, such as other sports, politics, or entertainment.\n"
                     "Be concise, accurate, and clear in responses to ensure users get a comprehensive understanding of the topic they inquire about."
        }
    ]
}

def access_cricket_database_for_statistics():
    db = msc.connect(
        host="localhost",
        user="root",
        password="356676",
        database="cricket"
    )
    my_cursor = db.cursor()
    my_cursor.execute("SELECT * FROM cricket_stats")
    cricket_table = my_cursor.fetchall()
    my_cursor.close()
    db.close()
    formatted_data = []
    for player in cricket_table:
        formatted_player = [
            player[0],
            player[1],  
            player[2], 
            player[3], 
            player[4], 
            player[5],
            player[6], 
            float(player[7]),
            player[8],
            player[9],
            player[10],  
            float(player[11]),
            player[12], 
            player[13] 
        ]
        formatted_data.append(formatted_player)
    return formatted_data


load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel(
    "gemini-1.5-flash",
    system_instruction=system_instruction,
    tools=access_cricket_database_for_statistics
)
history = []
chat = model.start_chat(enable_automatic_function_calling=True, history=history)
is_chat_on = True
while is_chat_on:
    try:
        user_input = input("You: ")
        response = chat.send_message(user_input)
        response = response.text.replace("**","")
        history.append({"role": "user", "parts": user_input})
        history.append({"role": "model", "parts": response})
        print("Bot:", response)
        if user_input.lower() == "exit":
            is_chat_on = False
    except Exception as e:
        print("Chat has been disconnect due to technical issue!")
        is_chat_on = False