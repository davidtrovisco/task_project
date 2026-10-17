// Por agora as tarefas ficam guardadas no browser.
// Quando a API do backend estiver pronta, basta trocar estas funções por fetch().
const KEY = 'tasks'

function ler() {
  return JSON.parse(localStorage.getItem(KEY)) || []
}

function guardar(tasks) {
  localStorage.setItem(KEY, JSON.stringify(tasks))
}

export function getTasks() {
  return ler()
}

export function addTask(title, description) {
  const tasks = ler()
  const id = tasks.length ? Math.max(...tasks.map((t) => t.id)) + 1 : 1
  tasks.push({ id, title, description, done: false })
  guardar(tasks)
}

export function toggleTask(id) {
  guardar(ler().map((t) => (t.id === id ? { ...t, done: !t.done } : t)))
}

export function deleteTask(id) {
  guardar(ler().filter((t) => t.id !== id))
}
