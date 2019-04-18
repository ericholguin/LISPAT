import React, { Component } from 'react';
import Markdown from 'react-markdown';
import { Col, Row, Button } from 'react-bootstrap';
import axios from 'axios/index';
import README from './README.md';
import './welcome-page.css';
import 'github-markdown-css';

const endpoint = 'http://localhost:5000/assets/samples.zip';

class WelcomePage extends Component {
  constructor(props, context) {
    super(props, context);
    this.ContentMarkdown = README;
  }

  handleDownload = () => {
    axios({
      url: endpoint,
      method: 'GET',
      responseType: 'blob', // important
    }).then(response => {
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('doswnload', 'samples.zip');
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
            <div className="download-container">
              <Button
                type="button"
                className="download-button"
                onClick={this.handleDownload}
              >
                Download Assets
              </Button>
            </div>
          </Col>
        </Row>
      </div>
    );
  }
}

export default WelcomePage;
