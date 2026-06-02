import Student from "./Student";
import UserGreeting from "./UserGreeting";
import List from "./List";
import Button from "./button";


function App(){
  
  const fruits = [
  { id: 1, name: "apple", calories: 95 },
  { id: 2, name: "orange", calories: 185 },
  { id: 3, name: "banana", calories: 175 },
  { id: 4, name: "coconut", calories: 65 },
  { id: 5, name: "pineapple", calories: 100 }
];

  const vegetables = [
  { id: 6, name: "carrot", calories: 41 },
  { id: 7, name: "broccoli", calories: 55 },
  { id: 8, name: "spinach", calories: 23 },
  { id: 9, name: "potato", calories: 77 },
  { id: 10, name: "cucumber", calories: 16 }
];


  return(
    <>
      
      <Student name="Spongebob" age={30} isStudent={false}/>
      <Student name="Patrick" age={15} isStudent={true}/>
      <Student name="Squidward" age={18} isStudent={true}/>
      <Student name="Sandy" age={17} isStudent={true}/>
      <Student/>
      <Student/>
      

      
      <UserGreeting isLoggedIn={true} username="Kurumi"/>
      <UserGreeting isLoggedIn={false} username="Kurumi"/>
      
      
      
      {fruits.length > 0 && (
      <List items={fruits} category="Fruits" />
       )}

      {vegetables.length > 0 && (
      <List items={vegetables} category="Vegetables" />
      )}
      

      <Button/>


    </>
  );
}

export default App;