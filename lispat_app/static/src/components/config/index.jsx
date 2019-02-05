import React, { Component } from 'react';
import './config.css';

class Config extends Component {
  render() {
    return (
      <div className="font-config">
        <select>
          <option>Nearest Neighbor</option>
        </select>
      </div>
    );
  }
}

export default Config;
