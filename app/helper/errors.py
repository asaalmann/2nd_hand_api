from flask import jsonify

def makeJsonError(message):
    error = {
        "status": "error",
        "message": message
    }
    return jsonify(error)