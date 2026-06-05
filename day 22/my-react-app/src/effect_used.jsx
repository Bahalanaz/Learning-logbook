import React, { useEffect, useState } from "react";

function Counting(){
    const [count, setcount] = useState(0);
    
    useEffect(() => {
        document.title = `Count: ${count}`;
    }, [count]);

    function addcount(){
        setcount(c => c + 1);
    }
    function reducecount(){
        setcount(c => c-1)
    }

    return(
    <>
    <p>Count: {count}</p>
    <button onClick={addcount}>Add</button>
    <button onClick={reducecount}>subtract</button>
    </>

    )
}
export default Counting