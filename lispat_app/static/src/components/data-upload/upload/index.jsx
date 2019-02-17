import React, { PureComponent } from 'react';
import { Form } from 'react-bootstrap';
import PropTypes from 'prop-types';
import './file-upload.css';

const FileUpload = class extends PureComponent {
  handleFile = event => {
    const { handleStateChange } = this.props;
    handleStateChange(event.target.files[0]);
  };

  render() {
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
};

export default FileUpload;
