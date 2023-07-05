from flask import Flask, request, jsonify
import random
import math

app = Flask(__name__)

@app.route('/guess', methods=['POST'])
def number_guessing_game():
    data = request.get_json()
    lower = data.get('lower', 1)
    upper = data.get('upper', 100)
    x = random.randint(lower, upper)
    max_attempts = round(math.log(upper - lower + 1, 2))
    count = 0

    while count < max_attempts:
        count += 1
        guess = data.get('guess')
        if guess is None:
            return jsonify({'error': 'Missing "guess" parameter.'}), 400

        guess = int(guess)
        if x == guess:
            return jsonify({'message': f'Congratulations! You guessed it in {count} tries.'}), 200
        elif x > guess:
            return jsonify({'message': 'You guessed too small!'}), 200
        elif x < guess:
            return jsonify({'message': 'You guessed too high!'}), 200

    return jsonify({'message': f'Out of attempts. The number was {x}.'}), 200

if __name__ == '__main__':
    app.run()
