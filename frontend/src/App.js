import React, { Component } from "react";
import "./App.css";
import PersonList from "./components/PersonList";

class App extends Component {
  render() {
    return (
      <div>
        <div className="container-fluid">
          <PersonList />
        </div>
      </div>
    );
  }
}

export default App;
