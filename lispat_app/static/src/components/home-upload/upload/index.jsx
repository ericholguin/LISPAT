import React, { PureComponent } from 'react';
import PropTypes from 'prop-types';
import './file-upload.css';

const FileUpload = class extends PureComponent {
  handleFile = event => {
    const { handleStateChange } = this.props;
    handleStateChange(event.target.files[0]);
  };

  render() {
    return (
      <div className="ml-auto format">
        <label className="btn btn-primary btn-file upload">
          {' '}
          Upload
          <input
            type="file"
            className="input"
            name="Upload"
            id=""
            onChange={this.handleFile}
          />
        </label>
      </div>
    );
  }
};

FileUpload.propTypes = {
  handleStateChange: PropTypes.func,
};

export default FileUpload;
