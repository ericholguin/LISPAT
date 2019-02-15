import React, { Component } from 'react';
import propTypes from 'prop-types';
import { Col, Container, Row, Button } from 'react-bootstrap';
import Highlighter from 'react-highlight-words';
import styles from './lispat-view.css';

class Lispat extends Component {
  constructor(props) {
    super(props);
    this.state = {
      submission: null,
      standard: null,
      date: null,
      keywords: [],
      phrases: [],
      submission_file_name: null,
      standard_file_name: null,
      activeIndex: -1,
    };
  }

  componentWillReceiveProps(props) {
    this.setData(props.data);
    // this.searchTerms(props.search);
  }

  setData = object => {
    if (object !== null && object !== undefined) {
      this.setState({
        submission: object.submission,
        standard: object.standard,
        date: object.date,
        keywords: object.keywords,
        phrases: object.keywords,
        submissionFileName: object.submission_file_name,
        standardFileName: object.standard_file_name,
      });
    }
  };

  searchTerms = () => {};

  sanitize = () => {};

  render() {
    const {
      submission,
      standard,
      submissionFileName,
      standardFileName,
      activeIndex,
      keywords,
    } = this.state;
    const margin = {
      position: 'fixed',
      left: '550px',
    };
    return (
      <div>
        <Row>
          <Col className="col-1" />
          <Col className="col-sm-4">
            <Row>
              <div className="doc-container move-left">
                <div className={styles['doc-header']}>{submissionFileName}</div>
                <hr className={styles.bar} />
                <div className={styles['doc-font']}>
                  <Highlighter
                    highlightClassName={styles.highlight}
                    searchWords={keywords}
                    autoEscape
                    textToHighlight={submission}
                  />
                </div>
              </div>
            </Row>
          </Col>
          <Col className="col" style={margin}>
            <div className="doc-container">
              <div className="doc-header">{standardFileName}</div>
              <hr className={styles.bar} />
              <div className={styles['doc-font']}>
                <Highlighter
                  highlightClassName={styles.highlight}
                  searchWords={keywords}
                  autoEscape
                  textToHighlight={standard}
                />
              </div>
            </div>
          </Col>
        </Row>
        <Row />
      </div>
    );
  }
}

Lispat.propTypes = {
  submission: propTypes.string,
  standard: propTypes.string,
  submissionFileName: propTypes.string,
  standardFileName: propTypes.string,
  date: propTypes.string,
  keywords: propTypes.instanceOf(Array),
  phrases: propTypes.instanceOf(Array),
  data: propTypes.instanceOf(Object),
  search: propTypes.string,
};

export default Lispat;
