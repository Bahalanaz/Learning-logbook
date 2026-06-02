function List(props){
    const category = props.category;
    const itemList = props.items;
    

    //fruits.sort((a,b) => a.name.localeCompare(b.name));
    //fruits.sort((a,b) => b.name.localeCompare(a.name));
    //fruits.sort((a,b) => a.calories - b.calories);
    //fruits.sort((a,b) => b.calories - a.calories);

    //const lowCalFruits = fruits.filter(fruit => fruit.calories < 100 )
    //const highCalFruits = fruits.filter(fruit => fruit.calories >= 100 )

    //const listItems = lowCalFruits.map(lowCalFruit => <li key = {lowCalFruit.id}>{lowCalFruit.name}:&nbsp;<b>{lowCalFruit.calories}</b></li>)
    //const listItems = highCalFruits.map(highCalFruit => <li key = {highCalFruit.id}>{highCalFruit.name}:&nbsp;<b>{highCalFruit.calories}</b></li>)

    const listItems = itemList.map(item => 
        <li key={item.id}>
            {item.name}:&nbsp;<b>{item.calories}</b>
        </li>
    );

    return (
        <>
            <h3 className="list-category">{category}</h3>
            <ol className="list-items">{listItems}</ol>
        </>
    );
}

List.defaultProps = {
    category : "Category",
}
export default List;