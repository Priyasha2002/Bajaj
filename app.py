from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def handle_post_request():
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        college_email_id = data.get('college_email_id')
        college_roll_number = data.get('college_roll_number')
        raw_data = data.get('data')

        if not raw_data or not isinstance(raw_data, str):
            return jsonify({"error": "Invalid data field"}), 400

        numbers = [char for char in raw_data if char.isdigit()]
        alphabets = [char for char in raw_data if char.isalpha()]
        lowercase_alphabets = [char for char in alphabets if char.islower()]
        highest_lowercase = max(lowercase_alphabets) if lowercase_alphabets else None

        response = {
            "status": 200,
            "user_id": user_id,
            "college_email_id": college_email_id,
            "college_roll_number": college_roll_number,
            "numbers_array": numbers,
            "alphabets_array": alphabets,
            "highest_lowercase_alphabet": highest_lowercase
        }

        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/operation', methods=['GET'])
def handle_get_request():
    return jsonify({"operation_code": "OP12345"}), 200

if __name__ == '__main__':
    app.run(port=5001)

