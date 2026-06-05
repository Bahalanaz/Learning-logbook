import React, {useState } from "react";
import "./TodoList.css"

function ToDoList(){
    const [tasks, SetTasks] = useState(["lol"]);
    const [newTask, SetNewTask] = useState("");

    function handleInputChange(event){
        SetNewTask(event.target.value)
    }

    function AddTask(){
        if(newTask.trim() !==""){
            SetTasks(t => [...t,newTask]);
        SetNewTask("");
        }
    }

    function DeleteTask(index){
        const updatedTasks = tasks.filter((_,i) => i !==index)
        SetTasks(updatedTasks);
    }

    function MoveTaskUp(index){
        if(index>0){
            const updatedTasks = [...tasks];
            [updatedTasks[index],updatedTasks[index - 1]]=
            [updatedTasks[index-1],updatedTasks[index]];
            SetTasks(updatedTasks);
        }
    }
    
    function moveTaskDown(index){
        if(index < tasks.length - 1){
            const updatedTasks = [...tasks];
            [updatedTasks[index],updatedTasks[index + 1]]=
            [updatedTasks[index + 1],updatedTasks[index]];
            SetTasks(updatedTasks);
        }
    }

    return(
    <>
    <div className="to-do-list">
        <h1>To-Do-List</h1>

        <div>
            <input type="text" placeholder="enter a task...." value={newTask} onChange={handleInputChange} />
            <button className="add-button" onClick={AddTask}>add</button>
        </div>
        
        <ol>
            {tasks.map((task,index) =>
            <li key={index}>
                <span className="text">{task}</span>
                <button className="delete-btn" onClick={() => DeleteTask(index)} >Delete</button>
                <button className="move-up-btn" onClick={() => MoveTaskUp(index)} >Up</button>
                <button className="move-down-btn" onClick={() => moveTaskDown(index)} >Down</button>
            </li>
        )}
        </ol>
    </div>
    </>
    );
}

export default ToDoList
