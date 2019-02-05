import React, { Component } from 'react';

class Lispat extends Component {
  render() {
    return (
      <div>
        <p>yes</p>
      </div>
    );
  }
}

Lispat.defaultProps = {
  title: 'My card title',
  content: 'Bacon ipsum dolor amet pork chop pork shoulder.',
};

export default Lispat;
