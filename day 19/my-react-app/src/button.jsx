function Button(){
    let count = 0;

    const handleClick = (name) => {
        count++;
        console.log(`${name} you clicked me ${count} times`);
    };

    return(
        <button className = "button-test" onClick={() => handleClick("kurumi")}>Click me</button>
    );
}

export default Button;