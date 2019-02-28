import React, { Component } from 'react';
import axios from 'axios';
import { Col, Row, Button } from 'react-bootstrap';
import PropTypes from 'prop-types';
import FileUpload from './upload';
import './home-upload.css';
import LoadingSpinner from './spinner';

const endpoint = 'http://localhost:5000/upload';

class DataUpload extends Component {
  constructor(props) {
    super(props);
    this.state = {
      file1: null,
      file2: null,
      loaded: 0,
      loading: false,
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
    const { stateChange, getData } = this.props;
    const data = new FormData();
    data.append('file1', file1, file1.name);
    data.append('file2', file2, file2.name);
    this.setState({
      loading: true,
    });
    axios
      .post(endpoint, data, {
        headers: { 'Content-Type': 'multipart/form-data' },
      })
      .then(res => {
        this.setState({
          loading: false,
        });
        stateChange(res.status);
        const resp = res.data;
        resp.submission_file_name =
          file1.name.substring(0, file1.name.lastIndexOf('.')) || file1.name;
        resp.standard_file_name =
          file2.name.substring(0, file2.name.lastIndexOf('.')) || file2.name;
        getData(resp);
      });
  };

  render() {
    const { file1, file2, loading } = this.state;
    return (
      <div>
        <br />
        <br />
        <div className="markdown-body body-upload">
          <div className="header-upload"> Upload Documents</div>
          <div className="sub-header-upload">.pdf .docx or .doc</div>
          <hr />
          <div className="center-grid">
            <Row>
              <Col>
                <div className="font-home">1st Document:</div>
                <FileUpload handleStateChange={this.setFileOne} />
                {file1 ? <div className="file-name">{file1.name}</div> : ''}
              </Col>
              <Col>
                <div className="font-home">2nd Document:</div>
                <FileUpload handleStateChange={this.setFileTwo} />
                {file2 ? <div className="file-name">{file2.name}</div> : ''}
              </Col>
            </Row>
          </div>
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
            {loading ? <LoadingSpinner /> : null}
          </Row>
        </div>
      </div>
    );
  }
}

DataUpload.propTypes = {
  stateChange: PropTypes.func,
  getData: PropTypes.func,
};

export default DataUpload;
