import pytest
import requests

# CRUD
BASE_URL = 'http://127.0.0.1:5000'
tasks = []

def test_create_task():
  new_task_data = {
    "title": "Nova Tarefa",
    "description": "Descrição da Nova Tarefa"
  }
  response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
  assert response.status_code == 200 
  # para testar o status da response precisa dar 200 (sucesso)
  response_json = response.json()

  assert "message" in response_json 
  assert "id" in response_json
  # verifica se "message" e "id" estão na resposta
  tasks.append(response_json['id'])

  
