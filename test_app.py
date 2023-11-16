import pytest
from app import app, tasks, current_id

@pytest.fixture
def clientA():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_addTask(clientA):
    response = clientA.post('/add', data={'task_name':'todo list'})
    assert response.status_code == 302
    assert tasks[-1]['task_name'] == 'todo list'



def test_markCompleted(clientA):
    global current_id
    tasks.append({'id':current_id, 'task_name': 'todo list', 'status':False})

    response = clientA.get(f'/complete/{current_id}')

    assert response.status_code == 302

    task = next((task for task in tasks if task['id'] == current_id), None)

    assert task is not None
    
    assert task['status'] == 'COMPLETED'

    
def test_deleteTask(clientA):
    global current_id
    tasks.append({'id':current_id, 'task_name':'todo list', 'status':False})
    current_id += 1

    response = clientA.get(f'/delete/{current_id - 1}')

    assert response.status_code == 302

    assert  any(task['task_name'] == 'todo list' for task in tasks)



