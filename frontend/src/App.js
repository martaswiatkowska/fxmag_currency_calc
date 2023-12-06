import './App.css';
import {useState, useEffect, component, MouseEvent } from "react";
import Calculator from "./components/calculator";

const url = "http://127.0.0.1:8000/api/calculator/"
const submit_url = "http://127.0.0.1:8000/api/calculated_value/"

function  App() {
  return (
    <div className="App">
      <header className="App-header">
        <Calculator/>
     </header>
    </div>
  );
  
}

export default App;
