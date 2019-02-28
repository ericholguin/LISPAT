import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Col, Container, Row, Button } from 'react-bootstrap';
import './help.css';

var GifPlayer = require('react-gif-player');

class HelpPage extends Component {
  constructor(props, context) {
    super(props, context);
  }

  render() {
    return (
      <GifPlayer
        gif="https://media.giphy.com/media/1i5Lj73Ff5IDtDaHfn/giphy.gif"
        autoplay
      />
    );
  }
}

export default HelpPage;
