import React from "react";
import Person from "./Person";
import CZButton from "./CZButton";

// class PersonList extends React.Component {
//   state = {
//     this.state: null,
//     error: null,
//     isLoaded: false,
//     items: []
//   };

//   componentDidMount() {
//     fetch("data.json")
//       .then(res => res.json())
//       .then(
//         result => {
//           this.setState({
//             isLoaded: true,
//             items: result.results
//           });
//         },
//         // Note: it's important to handle errors here
//         // instead of a catch() block so that we don't swallow
//         // exceptions from actual bugs in components.
//         error => {
//           this.setState({
//             isLoaded: true,
//             error
//           });
//         }
//       );
//   }

//   render() {
//     const { error, isLoaded, items } = this.state;
//     if (error) {
//       return (
//         <div>
//           Error:{" "}
//           {error.message + " if json returned 0, error from randomuser.org"}
//           {console.log(items)}
//         </div>
//       );
//     } else if (!isLoaded) {
//       // Show loading gif
//       return (
//         <div>
//           <img
//             src="https://cdn.dribbble.com/users/597558/screenshots/1998465/comp-2.gif"
//             alt="loading"
//             height="100"
//           />
//         </div>
//       );
//     } else {
//       // After loading
//       return (
//         <div className="row">
//           {console.log(items)}
//           {items.map(item => (
//             <Person
//               className="person"
//               Key={item.id.name + item.name.first}
//               imgSrc={item.picture.large}
//               Title={item.name.title}
//               FName={item.name.first}
//             >
//               {" "}
//               <CZButton />
//             </Person>
//           ))}
//         </div>
//       );
//     }
//   }
// }

import "./styles.css";
import "bootstrap/dist/css/bootstrap.min.css";

export default function App() {
  const data = [
    {
      name: "parent1",
      url: "url1",
      child: [
        {
          name: "child1",
          url: "child_url1",
          grand_child: [
            {
              name: "some name",
              url: "some url"
            }
          ]
        },
        {
          name: "child2",
          url: "child_url2"
        },
        {
          name: "child3",
          url: "child_url3"
        }
      ]
    },
    {
      name: "parent2",
      url: "url2",
      child: [
        {
          name: "child22",
          url: "child_url22"
        }
      ]
    },
    {
      name: "parent3",
      url: "url3",
      child: [
        {
          name: "child33",
          url: "child_url33"
        },
        {
          name: "child44",
          url: "child_url44"
        },
        {
          name: "child55",
          url: "child_url55"
        }
      ]
    }
  ];

  const [selectedVal, selectionChange] = useState("");
  const [selectedChild, selectionChild] = useState("");

  return (
    <div className="App">
      <div className="row">
        {data &&
          data.map(p => {
            return (
              <div className="col-4 col-sm-4 col-md-4 col-lg-4 col-xl-4">
                <div onClick={() => selectionChange(p.name)}>{p.name}</div>

                <div
                  style={
                    selectedVal === p.name
                      ? { display: "block" }
                      : { display: "none" }
                  }
                  className="div-children"
                >
                  <hr />
                  {p.child &&
                    p.child.map(c => {
                      return (
                        <p>
                          {
                            <label onClick={() => selectionChild(c.name)}>
                              {c.name}
                            </label>
                          }
                          <div
                            className="div--grandchildren"
                            style={
                              selectedChild === c.name
                                ? { display: "block" }
                                : { display: "none" }
                            }
                          >
                            <hr />
                            {c.grand_child &&
                              c.grand_child.map(g => {
                                return <p>{g.name}</p>;
                              })}
                          </div>
                        </p>
                      );
                    })}
                </div>
              </div>
            );
          })}
      </div>
    </div>
  );
}


// export default DropDown;
// export default PersonList;
