import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Markdown from 'react-markdown';
import { Col, Container, Row, Button } from 'react-bootstrap';
import README from './README.md';
import './api-page.css';
import 'github-markdown-css';

class ApiPage extends Component {
  constructor(props, context) {
    super(props, context);
    this.ContentMarkdown = README;
  }

  render() {
    return (
      <div>
        <Col className="left-pull">
          <div className="markdown-body api-page-container">
            <Markdown escapeHtml={false} source={this.ContentMarkdown} />
          </div>
        </Col>
      </div>
    );
  }
}

export default ApiPage;
