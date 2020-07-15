from flask import Flask, render_template, jsonify,request, send_from_directory,redirect,url_for
import os

UPLOAD_DIRECTORY = os.path.dirname(__file__) + '/files'

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

app = Flask(__name__)

#업로드 HTML 렌더링
@app.route('/upload')
def render_file():
   return render_template('upload.html')

#파일 업로드 처리
@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      #저장할 경로 + 파일명
      dirname=os.path.dirname(__file__) + '/files/'+f.filename
      #print(dirname)
      f.save(dirname)
   return redirect('/files')


@app.route("/files")
def list_files():
    """Endpoint to list files on the server."""
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    #return jsonify(files)
    return render_template('list.html',files=files)


@app.route("/files/<path:path>")
def get_file(path):
    """Download a file."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


# @app.route("/files/<filename>", methods=["POST"])
# def post_file(filename):
#     """Upload a file."""

#     if "/" in filename:
#         # Return 400 BAD REQUEST
#         abort(400, "no subdirectories directories allowed")

#     with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
#         fp.write(request.data)

#     # Return 201 CREATED
#     return "", 201


if __name__ == '__main__':
    #서버 실행
   app.run(debug = True,host='0.0.0.0',port=8890)
