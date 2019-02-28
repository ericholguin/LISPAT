import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Markdown from 'react-markdown';
import { Col, Container, Row, Button } from 'react-bootstrap';
import README from './README.md';
import './welcome-page.css';
import 'github-markdown-css';

class WelcomePage extends Component {
  constructor(props, context) {
    super(props, context);
    this.ContentMarkdown = README;
  }

  render() {
    return (
      <div>
        <Row>
          <Col className="left-pull">
            <div className="markdown-body welcome-page-container">
              <Markdown escapeHtml={false} source={this.ContentMarkdown} />
            </div>
          </Col>
        </Row>
      </div>
    );
  }
}

export default WelcomePage;
