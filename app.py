from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os
import uuid

app = Flask(__name__)

# -----------------------------
# Configuration
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")

os.makedirs(UPLOAD_DIR, exist_ok=True)

ALLOWED_EXTENSIONS = {
    "py", "zip", "js", "html", "css", "json", "txt"
}


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


# -----------------------------
# Home / API status
# -----------------------------
@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "service": "Muzaffar Hosting",
        "message": "Backend is running"
    })


# -----------------------------
# Upload file
# -----------------------------
@app.route("/api/upload", methods=["POST"])
def upload_file():

    if "file" not in request.files:
        return jsonify({
            "success": False,
            "message": "No file selected"
        }), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({
            "success": False,
            "message": "Filename is empty"
        }), 400

    if not allowed_file(file.filename):
        return jsonify({
            "success": False,
            "message": "File type not allowed"
        }), 400

    bot_id = str(uuid.uuid4())[:8]

    bot_folder = os.path.join(UPLOAD_DIR, bot_id)
    os.makedirs(bot_folder, exist_ok=True)

    filename = secure_filename(file.filename)
    file_path = os.path.join(bot_folder, filename)

    file.save(file_path)

    return jsonify({
        "success": True,
        "bot_id": bot_id,
        "filename": filename,
        "message": "File uploaded successfully"
    })


# -----------------------------
# List hosted files
# -----------------------------
@app.route("/api/files", methods=["GET"])
def list_files():

    result = []

    if not os.path.exists(UPLOAD_DIR):
        return jsonify(result)

    for bot_id in os.listdir(UPLOAD_DIR):

        bot_folder = os.path.join(UPLOAD_DIR, bot_id)

        if not os.path.isdir(bot_folder):
            continue

        files = os.listdir(bot_folder)

        result.append({
            "bot_id": bot_id,
            "files": files
        })

    return jsonify(result)


# -----------------------------
# Download / access hosted file
# -----------------------------
@app.route("/host/<bot_id>/<filename>")
def hosted_file(bot_id, filename):

    bot_folder = os.path.join(UPLOAD_DIR, secure_filename(bot_id))
    filename = secure_filename(filename)

    if not os.path.exists(os.path.join(bot_folder, filename)):
        return jsonify({
            "success": False,
            "message": "File not found"
        }), 404

    return send_from_directory(bot_folder, filename)


# -----------------------------
# Delete hosted bot/file
# -----------------------------
@app.route("/api/delete/<bot_id>/<filename>", methods=["DELETE"])
def delete_file(bot_id, filename):

    bot_folder = os.path.join(UPLOAD_DIR, secure_filename(bot_id))
    filename = secure_filename(filename)

    file_path = os.path.join(bot_folder, filename)

    if not os.path.exists(file_path):
        return jsonify({
            "success": False,
            "message": "File not found"
        }), 404

    os.remove(file_path)

    return jsonify({
        "success": True,
        "message": "File deleted successfully"
    })


# -----------------------------
# Admin status
# -----------------------------
@app.route("/api/admin")
def admin():

    return jsonify({
        "success": True,
        "panel": "Muzaffar Hosting Admin",
        "status": "online"
    })


# -----------------------------
# Run server
# -----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
  )
