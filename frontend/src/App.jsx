import { useState } from 'react'
import { getTasks, addTask, toggleTask, deleteTask } from './api'
import TaskForm from './components/TaskForm'
import TaskItem from './components/TaskItem'

function App() {
  const [tasks, setTasks] = useState(getTasks())

  function atualizar() {
    setTasks(getTasks())
  }

  function handleAdd(title, description) {
    addTask(title, description)
    atualizar()
  }

  function handleToggle(id) {
    toggleTask(id)
    atualizar()
  }

  function handleDelete(id) {
    deleteTask(id)
    atualizar()
  }

  return (
    <div className="container">
      <h1>Tarefas</h1>

      <TaskForm onAdd={handleAdd} />

      {tasks.length === 0 && <p className="vazio">Ainda não há tarefas.</p>}

      <ul>
        {tasks.map((task) => (
          <TaskItem
            key={task.id}
            task={task}
            onToggle={handleToggle}
            onDelete={handleDelete}
          />
        ))}
      </ul>
    </div>
  )
}

export default App
