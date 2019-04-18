import React, { Component } from 'react';
import propTypes from 'prop-types';
import chroma from 'chroma-js';
import { Col, Container, Row } from 'react-bootstrap';
import Highlighter from 'react-highlight-words';
import { invert, size } from 'lodash';
import Select from 'react-select';
import SearchBar from 'material-ui-search-bar';
import styles from './lispat-view.css';
import { colorStyles, colors } from './colors';

const selectStyles = {
  multiValue: (provided, { data }) => {
    const color = chroma(data.color);
    return {
      ...provided,
      backgroundColor: color.alpha(0.5).css(),
      fontSize: '10px',
    };
  },
  menu: provided => ({
    ...provided,
    height: '200px',
  }),
  menuList: provided => ({
    ...provided,
    height: '200px',
    backgroundColor: '#212121',
  }),
  option: (provided, { data, isDisabled, isFocused, isSelected }) => {
    const color = chroma(data.color);
    return {
      ...provided,
      backgroundColor: isDisabled
        ? null
        : isSelected
        ? data.color
        : isFocused
        ? color.alpha(0.1).css()
        : null,
      color: isDisabled
        ? '#ccc'
        : isSelected
        ? chroma.contrast(color, 'white') > 2
          ? 'white'
          : 'black'
        : data.color,
      cursor: isDisabled ? 'not-allowed' : 'default',
    };
  },
  multiValueLabel: (provided, { data }) => ({
    ...provided,
    color: data.color,
  }),
  multiValueRemove: (provided, { data }) => ({
    ...provided,
    color: data.color,
    ':hover': {
      backgroundColor: data.color,
      color: 'white',
    },
  }),
};

class Lispat extends Component {
  constructor(props) {
    super(props);
    this.state = {
      submission: '',
      standard: '',
      submissionKeywords: [{ label: '', value: '' }],
      standardKeywords: [{ label: '', value: '' }],
      selectedKeywordSubmission: [],
      selectedKeywordStandard: [],
      submissionFileName: null,
      standardFileName: null,
      stdColors: {},
      subColors: {},
      searchStandard: '',
      searchSubmission: '',
      ngrams: ['yup', 'allay', 'were', 'shall'],
    };
  }

  componentWillReceiveProps(props) {
    this.setData(props.data);
  }

  setColors = keyArray => {
    const keys = keyArray;
    let i = 0;
    keys.forEach(key => {
      if (i > keys.length) {
        i = 0;
      }
      key.color = colorStyles[i];
      i += 1;
    });
    return keys;
  };

  setColorsClass = keyArray => {
    const keys = keyArray;
    let i = 0;
    console.log(size(keys));
    Object.entries(keys).forEach(entry => {
      const [key] = entry;
      if (i > size(keys)) {
        i = 0;
      }
      keys[key] = colors[i];
      i += 1;
    });
    return keys;
  };

  setData = object => {
    if (object !== null && object !== undefined) {
      let subKey = object.submission_keywords.map(key => ({
        label: key,
        value: key,
      }));
      let stdKey = object.standard_keywords.map(key => ({
        label: key,
        value: key,
      }));

      subKey = this.setColors(subKey);
      stdKey = this.setColors(stdKey);

      let subKeyClass = invert({ ...object.submission_keywords });
      subKeyClass = this.setColorsClass(subKeyClass);
      let stdKeyClass = invert({ ...object.standard_keywords });
      stdKeyClass = this.setColorsClass(stdKeyClass);

      this.setState({
        submission: object.submission,
        standard: object.standard,
        date: object.date,
        submissionKeywords: subKey,
        standardKeywords: stdKey,
        phrases: object.keywords,
        submissionFileName: object.submission_file_name,
        standardFileName: object.standard_file_name,
        subColors: subKeyClass,
        stdColors: stdKeyClass,
      });
    }
  };

  selectKeywordSubmission = opt => {
    const keys = [];
    opt.forEach(key => {
      keys.push(key.value);
    });
    this.setState({
      selectedKeywordSubmission: keys,
    });
  };

  selectKeywordStandard = opt => {
    const keys = [];
    opt.forEach(key => {
      keys.push(key.value);
    });
    this.setState({
      selectedKeywordStandard: keys,
    });
  };

  updateSearchStandard = search => {
    const keys = [];
    keys.push(search);
    console.log(search);
    this.setState({
      selectedKeywordStandard: keys,
    });
  };

  updateSearchSubmission = search => {
    const keys = [];
    keys.push(search);
    this.setState({
      selectedKeywordSubmission: keys,
    });
  };

  getSelectedTextSubmission = () => {
    const { selectedKeywordSubmission, submission } = this.state;
    if (selectedKeywordSubmission.length === 0) {
      return submission;
    }
    const chunks = submission
      .replace(/(\.+|:|!|\?)("*|'*|\)*|}*|]*)(\s|\n|\r|\r\n)/gm, '$1$2|')
      .split('|');
    let ret = '';
    chunks.forEach(sent => {
      selectedKeywordSubmission.forEach(key => {
        if (sent.indexOf(key) !== -1) {
          const selected = sent + '\n\n';
          ret += selected;
        }
      });
    });
    return ret;
  };

  getSelectedTextStandard = () => {
    const { selectedKeywordStandard, standard } = this.state;
    if (
      selectedKeywordStandard.length === 0 ||
      selectedKeywordStandard === null
    ) {
      return standard;
    }
    const chunks = standard
      .replace(/(\.+|:|!|\?)("*|'*|\)*|}*|]*)(\s|\n|\r|\r\n)/gm, '$1$2|')
      .split('|');
    let ret = '';
    chunks.forEach(sent => {
      selectedKeywordStandard.forEach(key => {
        if (sent.indexOf(key) !== -1) {
          const selected = sent + '\n\n';
          ret += selected;
        }
      });
    });
    return ret;
  };

  suggestionRenderer = (suggestion, searchTerm) => (
    <span>
      <span>{searchTerm}</span>
      <strong>{suggestion.substr(searchTerm.length)}</strong>
    </span>
  );

  render() {
    const {
      submissionFileName,
      standardFileName,
      submissionKeywords,
      standardKeywords,
      selectedKeywordSubmission,
      selectedKeywordStandard,
      stdColors,
      subColors,
      searchStandard,
      searchSubmission,
      ngrams,
      submission,
    } = this.state;
    return (
      <div>
        <Container className="container-fluid">
          <Row>
            <Col className="col-sm-4">
              <div className="doc-container">
                <div className={styles['doc-header']}>{submissionFileName}</div>
                <hr className={styles.bar} />
                <div className={styles['doc-font']}>
                  <Highlighter
                    highlightClassName={subColors}
                    searchWords={selectedKeywordSubmission}
                    autoEscape
                    textToHighlight={this.getSelectedTextStandard()}
                  />
                </div>
              </div>
            </Col>
            <Col className="col-sm-4">
              <div className="doc-container">
                <div className="doc-header">{standardFileName}</div>
                <hr className={styles.bar} />
                <div className={styles['doc-font']}>
                  <Highlighter
                    highlightClassName={stdColors}
                    searchWords={selectedKeywordStandard}
                    autoEscape
                    textToHighlight={this.getSelectedTextSubmission()}
                  />
                </div>
              </div>
            </Col>
            <Col className="col-sm-4">
              <Col className="col-sm-12">
                <div className="doc-container keyword-class">
                  <div className="key-header">
                    1st Document
                    <br /> Top Keywords
                  </div>
                  <hr className={styles.bar} />
                  <Select
                    className="keywords"
                    isMulti
                    isClearable
                    onChange={this.selectKeywordSubmission}
                    options={submissionKeywords}
                    theme={theme => ({
                      ...theme,
                      borderRadius: 0,
                      colors: {
                        ...theme.colors,
                        primary25: '#4DB6AC',
                        primary: '#1565C0',
                      },
                    })}
                    styles={selectStyles}
                  />
                  <SearchBar
                    title="Press Enter to clear terms on document"
                    className="search-bar"
                    onChange={change => {
                      if (change === '' || change === null) {
                        this.setState({
                          selectedKeywordSubmission: [],
                        });
                      }
                    }}
                    onRequestSearch={search => {
                      this.updateSearchSubmission(search);
                    }}
                    style={{
                      margin: '0 auto',
                      maxWidth: 800,
                      maxHeight: 45,
                    }}
                  />
                </div>
              </Col>
              <Col className="col-sm-12">
                <div className="doc-container keyword-class">
                  <div className="key-header">
                    2nd Document
                    <br /> Top Keywords
                  </div>
                  <hr className={styles.bar} />
                  <Select
                    className="keywords"
                    isMulti
                    isClearable
                    onChange={this.selectKeywordStandard}
                    options={standardKeywords}
                    theme={theme => ({
                      ...theme,
                      borderRadius: 0,
                      colors: {
                        ...theme.colors,
                        primary25: '#4DB6AC',
                        primary: '#1565C0',
                      },
                    })}
                    styles={selectStyles}
                  />
                  <SearchBar
                    title="Press Enter to clear terms on document"
                    className="search-bar"
                    onChange={change => {
                      if (change === '' || change === null) {
                        this.setState({
                          selectedKeywordStandard: [],
                        });
                      }
                    }}
                    onRequestSearch={search => {
                      this.updateSearchStandard(search);
                    }}
                    style={{
                      margin: '10px 0 20px 0',
                      maxWidth: 800,
                      maxHeight: 45,
                    }}
                  />
                </div>
              </Col>
            </Col>
          </Row>
        </Container>
      </div>
    );
  }
}

Lispat.propTypes = {
  data: propTypes.instanceOf(Object),
};

export default Lispat;
