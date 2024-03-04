from flask import Flask, render_template, request, jsonify
from chatbot import get_intent, get_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        print("mensaje de usuario",request.form['message'])
        user_message = request.form['message']
        intent = get_intent(user_message)
        word = intent
        
        # Extract product name from the user's message
        product = None
        if intent == "product_inquiry":
            # You can enhance this part based on your specific use case and product naming conventions
            print("user message:",word)
            for word in user_message.lower().split():
                if word in ["hierro", "cemento", "griferia"]:
                    product = word
                    break

        bot_response = get_response(intent, product)
        return jsonify({'response': bot_response})
    except Exception as e:
        print(f"Server error: {str(e)}")
        return jsonify({'response': 'Server error'})

if __name__ == '__main__':
     app.run(debug=True)