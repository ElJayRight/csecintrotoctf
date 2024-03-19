from flask import Flask, render_template, request, make_response
import sys
import base64

app = Flask(__name__)

# Dummy data for demonstration
notes = [
    {"id": 1, "title": "Flag", "content": "You found me! CSEC{C00k1e5_4r3_n0t_s3cur3}"},
    {"id": 2, "title": "Note 1", "content": "You wont be able to access the admin note now. :)"},
    {"id": 3, "title": "Note 2", "content": "Data encoding is the best."}
]

@app.route('/')
def index():
    response = make_response(render_template('index.html', notes=notes[1:]))
    cookie = 'admin=False'
    enc_cookie = base64.b64encode(cookie.encode())
    response.set_cookie('Authentication', enc_cookie.decode())
    return response

@app.route('/notes', methods=['GET','POST'])
def view_notes():
    if request.method == 'POST':
        new_note = {
            'id': len(notes)+1,
            'title': request.form['title'],
            'content': request.form['content']
        }
        notes.append(new_note)
    return render_template('notes.html', notes=notes[1:])

@app.route('/note/<int:note_id>')
def view_note(note_id):
    for note in notes:
        if note_id ==1:
            if 'Authentication' not in request.cookies:
                return "Unauthorised!", 401
            enc_cookie = request.cookies['Authentication']
            cookie = base64.b64decode(enc_cookie).decode()
            if cookie.lower() != 'admin=true':
                return "This note isnt for you. Go away now!", 401

        if note['id'] == note_id:
            return render_template('note.html', note=note)
    return "Note not found", 404

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"[!] Error running server. Run as follows:\n[i]{sys.argv[0]} <port>")
        exit()    
    app.run(host='0.0.0.0',port=int(sys.argv[1]))
