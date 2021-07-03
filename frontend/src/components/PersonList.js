import React from "react";
import Person from "./Person";
import CZButton from "./CZButton";

class PersonList extends React.Component {
  state = {
    error: null,
    isLoaded: false,
    items: []
  };

  componentDidMount() {
    fetch("data.json")
      .then(res => res.json())
      .then(
        result => {
          this.setState({
            isLoaded: true,
            items: result.results
          });
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        error => {
          this.setState({
            isLoaded: true,
            error
          });
        }
      );
  }

  render() {
    const { error, isLoaded, items } = this.state;
    if (error) {
      return (
        <div>
          Error:{" "}
          {error.message + " if json returned 0, error from randomuser.org"}
          {console.log(items)}
        </div>
      );
    } else if (!isLoaded) {
      // Show loading gif
      return (
        <div>
          <img
            src="https://cdn.dribbble.com/users/597558/screenshots/1998465/comp-2.gif"
            alt="loading"
            height="100"
          />
        </div>
      );
    } else {
      // After loading
      return (
        <div className="row">
          {console.log(items)}
          {items.map(item => (
            <Person
              className="person"
              Key={item.id.name + item.name.first}
              imgSrc={item.picture.large}
              Title={item.name.title}
              FName={item.name.first}
            >
              {" "}
              <CZButton />
            </Person>
          ))}
        </div>
      );
    }
  }
}

export default PersonList;
