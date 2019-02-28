import React, { Component } from 'react';
import { Form } from 'react-bootstrap';
import PropTypes from 'prop-types';
import { includes } from 'lodash';
import './file-upload.css';

const extensions = ['docx', 'pdf'];

const FileUpload = class extends Component {
  constructor(props) {
    super(props);
    this.state = {
      error: false,
    };
  }

  handleFile = event => {
    const { handleStateChange } = this.props;
    const file = event.target.files[0];
    const ext = this.getFileExtension(file.name);
    if (includes(extensions, ext)) {
      handleStateChange(file);
    } else {
      handleStateChange(false);
    }
  };

  getFileExtension = filename =>
    filename.slice(((filename.lastIndexOf('.') - 1) >>> 0) + 2);

  render() {
    const { error } = this.state;
    return (
      <Form>
        <label className="btn btn-primary btn-file upload">
          Upload
          <input
            type="file"
            className="input"
            name="Upload"
            id=""
            onChange={this.handleFile}
          />
        </label>
      </Form>
    );
  }
};

FileUpload.propTypes = {
  handleStateChange: PropTypes.func,
  error: PropTypes.func,
};

export default FileUpload;
