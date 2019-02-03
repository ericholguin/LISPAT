import React, { Component } from 'react';
import axios from 'axios';
import { Col, Container, Row, Button } from 'react-bootstrap';
import FileUpload from './upload';
import './home-upload.css';

const endpoint = 'http://localhost:5000/upload';

class HomeUpload extends Component {
  constructor(props) {
    super(props);
    this.state = {
      file1: null,
      file2: null,
      loaded: 0,
    };
  }

  setFileOne = file => {
    this.setState({
      file1: file,
    });
  };

  setFileTwo = file => {
    this.setState({
      file2: file,
    });
  };

  handleUpload = () => {
    const { file1, file2 } = this.state;
    const data = new FormData();
    console.log(file1);
    console.log(file2);
    data.append('file1', file1, file1.name);
    data.append('file2', file2, file2.name);
    axios
      .post(endpoint, data, {
        onUploadProgress: ProgressEvent => {
          this.setState({
            loaded: (ProgressEvent.loaded / ProgressEvent.total) * 100,
          });
        },
        headers: { 'Content-Type': 'multipart/form-data' },
      })
      .then(res => {
        console.log(res.statusText);
      });
  };

  render() {
    const { file1, file2, loaded } = this.state;
    return (
      <div>
        <br />
        <br />
        <Container>
          <div className="center-grid">
            <Row>
              <Col>
                <div className="font-home">1.&nbsp;&nbsp;Proposal</div>
                <br />
                <FileUpload handleStateChange={this.setFileOne} />
                {file1 ? <div className="file-name">{file1.name}</div> : ''}
              </Col>
            </Row>
          </div>
          <br />
          <br />
          <div className="center-grid">
            <Row>
              <Col>
                <div className="font-home">2.&nbsp;&nbsp;Standard</div>
                <br />
                <FileUpload handleStateChange={this.setFileTwo} />
                {file2 ? <div className="file-name">{file2.name}</div> : ''}
              </Col>
            </Row>
          </div>
          <br />
          <div className="go-pos">
            <Row>
              <Col>
                {loaded !== 0 ? (
                  <div className="progress">{Math.round(loaded)} %</div>
                ) : (
                  ''
                )}
              </Col>
              <Col>
                <Button
                  type="button"
                  className="go-button"
                  onClick={this.handleUpload}
                >
                  GO
                </Button>
              </Col>
            </Row>
          </div>
        </Container>
      </div>
    );
  }
}

export default HomeUpload;
