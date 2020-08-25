import React from "react";

class HelloWorld extends React.Component {
  render() {
    return (
      <h1>
        Hello {this.props.name} {this.props.laputa}
      </h1>
    );
  }
}

export default HelloWorld;
