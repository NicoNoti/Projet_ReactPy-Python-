from flask import Flask, send_from_directory, request, jsonify
import os
from reactpy_app import generate_png, generate_pdf

app = Flask(__name__, static_folder='reactpy_build')

@app.route('/')
def index():
    reactpy_html_file = 'reactpy_build/index.html'
    if not os.path.exists(reactpy_html_file):
        return "ReactPy build not found!", 404
    return send_from_directory('reactpy_build', 'index.html')

@app.route('/generate-files', methods=['POST'])
def generate_files():
    data = request.get_json()
    name = data.get('name')
    title = data.get('title')
    company = data.get('company')
    email = data.get('email')

    pdf_base64 = generate_pdf(name, title, company, email)
    png_base64 = generate_png(name, title, company, email)

    return jsonify({
        'pdfUrl': f'data:application/pdf;base64,{pdf_base64}',
        'pngUrl': f'data:image/png;base64,{png_base64}'
    })

if __name__ == "__main__":
    app.run(debug=True)
