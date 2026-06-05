import React, { useEffect, useState } from "react";
import "./stopwatch.css";

function Stopwatch() {
    const [time, setTime] = useState(0); 
    const [isRunning, setIsRunning] = useState(false);

    useEffect(() => {
        let intervalId;

        if (isRunning) {
            intervalId = setInterval(() => {
                setTime(prev => prev + 10); // increase by 10ms
            }, 10);
        }

        return () => clearInterval(intervalId);
    }, [isRunning]);

    function start() {
        setIsRunning(true);
    }

    function stop() {
        setIsRunning(false);
    }

    function reset() {
        setIsRunning(false);
        setTime(0);
    }

    function formatTime(time) {
        const milliseconds = Math.floor((time % 1000) / 10);
        const seconds = Math.floor((time / 1000) % 60);
        const minutes = Math.floor((time / (1000 * 60)) % 60);
        const hours = Math.floor(time / (1000 * 60 * 60));

        return `${String(hours).padStart(2, "0")}:` +
               `${String(minutes).padStart(2, "0")}:` +
               `${String(seconds).padStart(2, "0")}.` +
               `${String(milliseconds).padStart(2, "0")}`;
    }

    return (
        <div className="stopwatch-container">
            <div className="stopwatch-box">

                <h1>Stopwatch</h1>

                <h2 className="time">{formatTime(time)}</h2>

                <button onClick={start}>Start</button>
                <button onClick={stop}>Stop</button>
                <button onClick={reset}>Reset</button>

            </div>
        </div>
    );
}

export default Stopwatch;