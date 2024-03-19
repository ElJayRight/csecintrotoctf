from flask import Flask, render_template, request
import sys

app = Flask(__name__)

# Dummy data for demonstration
notes = [
    {"id": 1, "title": "Flag", "content": "You found me! CSEC{51mpl3_1d04_FTW!}"},
    {"id": 2, "title": "Note 1", "content": "My First Note!"},
    {"id": 3, "title": "Note 2", "content": "Is there a hidden note somewhere?"}
]

@app.route('/')
def index():
    return render_template('index.html', notes=notes[1:])

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
        if note['id'] == note_id:
            return render_template('note.html', note=note)
    return "Note not found", 404


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"[!] Error running server. Run as follows:\n[i]{sys.argv[0]} <port>")
        exit()
    app.run(host='0.0.0.0',port=int(sys.argv[1]))
