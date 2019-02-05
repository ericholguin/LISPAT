import React, { Component } from 'react';
import axios from 'axios';
import { Col, Container, Row, Button } from 'react-bootstrap';
import PropTypes from 'prop-types';
import FileUpload from './upload';
import './home-upload.css';

const endpoint = 'http://localhost:5000/upload';

class DataUpload extends Component {
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
    const { stateChange } = this.props;
    const data = new FormData();
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
        stateChange(res.status);
      });
  };

  render() {
    const { file1, file2, loaded } = this.state;
    return (
      <div>
        <br />
        <br />
        <div className="markdown-body body-upload">
          <hr />
          <div className="center-grid">
            <Row>
              <Col>
                <div className="font-home">First Doc:</div>
                <FileUpload handleStateChange={this.setFileOne} />
                {file1 ? <div className="file-name">{file1.name}</div> : ''}
              </Col>
            </Row>
          </div>
          <div className="center-grid">
            <Row>
              <Col>
                <div className="font-home">Second Doc: </div>
                <FileUpload handleStateChange={this.setFileTwo} />
                {file2 ? <div className="file-name">{file2.name}</div> : ''}
              </Col>
            </Row>
          </div>
          <hr />
          <br />
          <Row>
            <div className="go-pos">
              <Col>
                {file1 !== null && file2 !== null ? (
                  <Button
                    type="button"
                    className="go-button"
                    onClick={this.handleUpload}
                  >
                    GO
                  </Button>
                ) : null}
              </Col>
            </div>
            {loaded !== 0 ? (
              <div className="progress">{Math.round(loaded)} %</div>
            ) : null}
          </Row>
        </div>
      </div>
    );
  }
}

DataUpload.propTypes = {
  stateChange: PropTypes.func,
};

export default DataUpload;
