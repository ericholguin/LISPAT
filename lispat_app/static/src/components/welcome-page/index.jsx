import React, { Component } from 'react';
import Markdown from 'react-markdown';
import { Col, Row, Button } from 'react-bootstrap';
import README from './README.md';
import './welcome-page.css';
import 'github-markdown-css';
import axios from 'axios/index';

class WelcomePage extends Component {
  constructor(props, context) {
    super(props, context);
    this.ContentMarkdown = README;
  }

  handleDownload = () => {
    axios({
      url: 'http://localhost:5000/assets/samples.zip',
      method: 'GET',
      responseType: 'blob', // important
    }).then(response => {
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', 'samples.zip');
      document.body.appendChild(link);
      link.click();
    });
  };

  render() {
    return (
      <div>
        <Row>
          <Col className="left-pull">
            <div className="markdown-body welcome-page-container">
              <Markdown escapeHtml={false} source={this.ContentMarkdown} />
            </div>
          </Col>
          <Col>
            <Button
              type="button"
              className="download-button"
              onClick={this.handleDownload}
            >
              Download Assets
            </Button>
          </Col>
        </Row>
      </div>
    );
  }
}

export default WelcomePage;
