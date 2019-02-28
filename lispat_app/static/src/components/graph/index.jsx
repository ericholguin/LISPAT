import './graph.css';
import axios from 'axios';
import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { Col, Container, Row, Button } from 'react-bootstrap';

const endpoint = 'http://localhost:5000/graph';

class Graph extends Component {

  handleGraph = () => {
    axios.get(endpoint).then(res => {
      const resp = res.data;
    });
  };

  render() {
    return (
      <div>
        <Button type="button" className="button" onClick={this.handleGraph}>
          SHOW ME THE GRAPH
        </Button>
      </div>
    );
  }
}

export default Graph;
