function TaskItem({ task, onToggle, onDelete }) {
  return (
    <li className={task.done ? 'feita' : ''}>
      <input
        type="checkbox"
        checked={task.done}
        onChange={() => onToggle(task.id)}
      />
      <div className="texto">
        <strong>{task.title}</strong>
        {task.description && <span>{task.description}</span>}
      </div>
      <button onClick={() => onDelete(task.id)}>Apagar</button>
    </li>
  )
}

export default TaskItem
