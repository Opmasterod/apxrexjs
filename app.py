from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/<message_id>')
def serve_file(message_id):
    # Here, you'll need to look up the file from your server using the message_id
    # For simplicity, assume files are stored in a directory named 'files'
    try:
        return send_from_directory('files', f'{message_id}.mp4')  # Change the file extension based on file type
    except Exception as e:
        return f"File not found: {e}", 404

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
