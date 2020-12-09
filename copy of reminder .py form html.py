from flask import Flask, request, jsonify, abort
from reminder_json_helper import read_reminder_json, create_reminder_json, write_reminder_json
import uuid
import os
from flask_cors import CORS

os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
CORS(app)

@app.route('/api/reminders', methods=['GET'])
def get_reminders():
    reminders = read_reminder_json()
    return jsonify({'reminders': reminders})

@app.route('/api/reminders', methods=['POST'])
def create_reminder():
    print(request.content_type)
    if not request.content_type == 'application/x-www-form-urlencoded':
        req_data = request.get_json()
        print('REQ-DATA:', req_data)
    else:
        req_data = request.form

    print(req_data)
    if not all(item in req_data
               for item in ("message", "due_date", "interval")):
        abort(400)

    reminder = {
        'id': uuid.uuid4().hex,
        'message': req_data['message'],
        'interval': req_data['interval'],
        'due_date': req_data['due_date']
    }

    create_reminder_json(reminder)
    return jsonify({'reminder': reminder}), 201


@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad Request'}), 400

@app.route('/api/reminders/<reminder_id>', methods=['DELETE'])
def delete_reminder(reminder_id):
    reminders = read_reminder_json()
    reminder = [
        reminder for reminder in reminders if reminder['id'] == reminder_id
    ]
    if len(reminder) == 0:
        abort(404)
    reminders.remove(reminder[0])
    data = {}
    data['reminders'] = reminders
    write_reminder_json(data)
    return jsonify({'message': 'Reminder has been removed successfully'})


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Sorry The Reminder App Encountered An Error'}), 500

if __name__ == '__main__':
    app.run()
