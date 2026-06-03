import React, { useState } from "react";

function ReactingToReact() {
  const [name, setName] = useState("Guest");
  const [quantity, setQuantity] = useState(1);
  const [comment, setComment] = useState ("")
  const [payment, setpayment] = useState("")
  const [shipping,setShipping] = useState("")
 
  function handleNameChange(event) {
    setName(event.target.value);
  }

  function handleQuantityChange(event){
    setQuantity(event.target.value);
  }

  function handleCommentChange(event){
    setComment(event.target.value)
  }

  function handlePaymentChange(event){
    setpayment(event.target.value)
  }

  function handleShippingChange(event){
    setShipping(event.target.value)
  }


  return (
    <div>
      <input value={name} onChange={handleNameChange} />
      <p>Name: {name}</p>
      <input value={quantity} onChange={handleQuantityChange} type="number"/>
      <p>Quantity: {quantity}</p>

      <textarea value={comment} onChange={handleCommentChange}
      placeholder="Enter delivery instructions"/>
      <p>Comment: {comment}</p>

      <select value={payment} onChange={handlePaymentChange}>
        <option value="">select an option</option>
        <option value="Visa">Visa</option>
        <option value="MasterCard">MasterCard</option>
        <option value="GiftCard">GiftCard</option>
      </select>
      <p>payment: {payment}</p>

      <label>
        <input type="radio" value = "Pick up" checked={shipping === "pick up"} onChange={handleShippingChange}/>
        Pick up
      </label>

      <label>
        <input type="radio" value = "Delivery" checked={shipping === "delivery"} onChange={handleShippingChange}/>
        Delivery
      </label>
      <p>Shipping: {shipping}</p>
    </div>
    
  );
}

export default ReactingToReact;