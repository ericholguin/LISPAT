import React, { Component } from 'react';
import axios from 'axios';
import { Col, Container, Row, Button } from 'react-bootstrap';
import PropTypes from 'prop-types';
import FileUpload from './upload';
import './home-upload.css';

const endpoint = 'http://localhost:5000/data-upload';

class DataUpload extends Component {
  constructor(props) {
    super(props);
    this.state = {
      file1: null,
      file2: null,
      loaded: 0,
      statusCode: 0,
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
        this.state.statusCode = res.statusText;
        const { statusCode, loaded } = this.state;
        stateChange(statusCode, loaded);
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
                <div className="font-home">Your current submission:</div>
                <FileUpload handleStateChange={this.setFileOne} />
                {file1 ? <div className="file-name">{file1.name}</div> : ''}
              </Col>
            </Row>
          </div>
          <div className="center-grid">
            <Row>
              <Col>
                <div className="font-home">The standard: </div>
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
                <Button
                  type="button"
                  className="go-button"
                  onClick={this.handleUpload}
                >
                  GO
                </Button>
                {loaded !== 0 ? (
                  <div className="progress">{Math.round(loaded)} %</div>
                ) : null}
              </Col>
            </div>
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
