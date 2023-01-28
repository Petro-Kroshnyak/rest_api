import json
from flask import Flask, jsonify, request

app = Flask(__name__)

records = [
    {
        "text": "Hello"
    },
    {
        "text": "Bye!"
    },
]


def get_record(record):
    return next((e for e in records if e['text'] == record), None)


@app.route('/api/last_10_records', methods=['GET'])
def get_records():
    if len(records) <= 10:
        return jsonify({'last 10 added records': records})
    else:
        return jsonify({'last 10 added records': records[-10:]})


@app.route('/api/add_record/<record>', methods=['POST'])
def add_record(record):
    new_record = {"text": record}
    records.append(new_record)
    return jsonify({'New added record': new_record})


@app.route('/api/delete_record/<record>', methods=['DELETE'])
def delete_record(record):
    global records
    deleted_record = get_record(record)
    records = [e for e in records if e['text'] != record]
    return jsonify({'Removed record': deleted_record})


app.run()
