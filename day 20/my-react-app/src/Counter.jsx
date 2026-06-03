import React, { useState } from "react";
import "./Counter.css";

function Counter() {
  const [number, setcount] = useState(0);

  const addnumber = () => {
    setcount(number + 1);
  };

  const minusnumber = () => {
    setcount(number - 1);
  };

  const resetnumber = () => {
    setcount(0);
  };

  return (
    <div className="counter-container">
      <p className="category">Age</p>

      <p className="text">{number}</p>

      <div className="btn-group">
        <button onClick={addnumber} className="add-btn">
          Add
        </button>

        <button onClick={resetnumber} className="add-btn">
          Reset
        </button>

        <button onClick={minusnumber} className="add-btn">
          Decrease
        </button>

      </div>
    </div>
  );
}

export default Counter;