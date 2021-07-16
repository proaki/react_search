import React from "react";

const Person = props => {
  return (
      <div className="drop-down" key={props.Key}>
            <select>
                { this.state.options.map((option, key) => <option key={key} >{option}</option>) }
            </select>
      </div>
  );
};

export default Person;
