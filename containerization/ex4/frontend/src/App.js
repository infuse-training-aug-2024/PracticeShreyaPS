import logo from "./logo.svg";
import "./App.css";
import React, { useEffect } from "react";

function App() {
 
  const fetchData = async () => {
    try {
        const res = await fetch("http://localhost:4000/");
        if (!res.ok) {
            throw new Error(`HTTP error! status: ${res.status}`);
        }
        const data = await res.json();
        console.log('API response:', data);
         }
     catch (error) {
        console.error('Error fetching data:', error);
    }
};

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Open console and refresh to see response from backend 
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;