import React, { Component } from "react";
import { Link } from "react-router-dom";

class SignIn extends Component {
  constructor() {
    super();

    this.state = {
      username:"",
      email: "",
      password: ""
    };

    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit(event) {
    event.preventDefault();

    console.log(this.state);
  }

  render() {
    return (
      <div className="formCenter">
        <form className="formFields" onSubmit={this.handleSubmit}>
          <div className="formField">
            <label className="formFieldLabel" htmlFor="username">
              Username
            </label>
            <input
              type="username"
              id="username"
              className="formFieldInput"
              placeholder="Enter your name"
              name="username"
            />
          </div>

          <div className="formField">
            <label className="formFieldLabel" htmlFor="email">
              E-MAIL
            </label>
            <input
              type="email"
              id="email"
              className="formFieldInput"
              placeholder="Enter your email"
              name="email"

            />
          </div>

          <div className="formField">
            <label className="formFieldLabel" htmlFor="password">
              Password
            </label>
            <input
              type="password"
              id="password"
              className="formFieldInput"
              placeholder="Enter your password"
              name="password"
            />
          </div>

          <div>
              <button type="submit" className="formFieldButton">Sign In</button>
          </div>
        </form>
      </div>
    );
  }
}

export default SignIn;