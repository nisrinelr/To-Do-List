from flask import Flask, render_template, request, jsonify, url_for,redirect

app = Flask(__name__)

tasks = []
current_id = 1
status = False
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


#endpoint for adding tasks

@app.route('/add', methods=['POST'])
def add_task():
    global current_id
    if request.method == 'POST':
        task_name = request.form['task_name']
        new_task = {'id': current_id, 'task_name': task_name, 'status': False}
        tasks.append(new_task)
        current_id += 1
        print(tasks)
        return redirect(url_for('index'))



#endpoint for deleting tasks
@app.route('/delete/<int:task_id>')
def deleteTask(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('index'))



#endpoint for marking tasks as completed
@app.route('/complete/<int:task_id>')
def mark_completed(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        task['status'] = 'COMPLETED'
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
