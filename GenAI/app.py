from flask import Flask, request, jsonify
import sqlite3
import openai

# ✅ OpenRouter setup (get your key from https://openrouter.ai/keys)
client = openai.OpenAI(
    api_key="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",  # 🔁 Replace with your actual key
    base_url="https://openrouter.ai/api/v1",
)

app = Flask(__name__)

# ✅ Convert natural language question to SQL using LLM
def question_to_sql(question):
    prompt = f"""
You are an expert SQL assistant.

Convert the question into a valid SQLite SQL query using ONLY these tables:

1. ad_sales(date, item_id, ad_sales, impressions, ad_spend, clicks, units_sold)
2. eligibility(eligibility_datetime_utc, item_id, eligibility, message)
3. total_sales(date, item_id, total_sales, total_units_ordered)

⚠️ Output ONLY a valid SQL query — no explanations or text.

Question: {question}
SQL:
"""

    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",  # Or try: openchat/openchat-3.5-0106
        messages=[
            {"role": "system", "content": "You convert plain English into valid SQL queries."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content.strip()

# ✅ API endpoint
@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json()
        question = data.get("question", "").strip()

        if not question:
            return jsonify({"error": "Missing 'question' in request"}), 400

        # Step 1: Convert question to SQL
        sql_query = question_to_sql(question)
        print("📥 User Question:", question)
        print("🧠 Generated SQL:\n", sql_query)

        # Step 2: Execute the SQL query
        conn = sqlite3.connect("ecommerce.db")
        cursor = conn.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        conn.close()

        # Step 3: Return the results
        results = [dict(zip(columns, row)) for row in rows]

        return jsonify({
            "question": question,
            "sql_query": sql_query,
            "results": results
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ Start Flask server
if __name__ == '__main__':
    app.run(debug=True)
