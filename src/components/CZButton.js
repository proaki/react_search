import React from "react";
import Drawer from "react-drag-drawer";

class CZButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { open: false };
  }

  toggle = () => {
    let { toggle } = this.state;

    this.setState({ open: !this.state.open });
  };

  render() {
    const { open } = this.state;

    return (
      <div>
        {" "}
        <button onClick={this.toggle}>Show</button>
        <Drawer
          open={this.state.open}
          onRequestClose={this.toggle}
          onDrag={() => {}}
          onOpen={() => {}}
          allowClose={true}
          modalElementClass="modal"
          containerElementClass="my-shade"
          parentElement={document.body} // element to be appended to
          direction="bottom"
        >
          <div>Hey Im inside a drawer!</div>
        </Drawer>
      </div>
    );
  }
}

export default CZButton;
