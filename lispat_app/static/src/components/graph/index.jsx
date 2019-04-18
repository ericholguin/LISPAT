import './graph.css';
import axios from 'axios';
import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { Col, Container, Row, Button } from 'react-bootstrap';
import LoadingSpinner from './spinner';

const endpoint = 'http://localhost:5000/graph.html';

class Graph extends Component {
  constructor(props) {
    super(props);
    this.state = {
      keyword: null,
      loaded: 0,
      loading: false,
    };
  }

  setKeyword = keyword => {
    this.setState({
      keyword,
    });
  };

  handleGraph = () => {
    axios.get(endpoint).then(res => {
      const resp = res.data;
    });
  };

  handleKeyword = () => {
    const { keyword } = this.state;
    // const { stateChange, getData } = this.props;
    const data = new FormData();
    data.append('keyword', keyword);
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
      });
  };

  render() {
    const { keyword, loading } = this.state;
    return (
      <div>
        <br />
        <br />
        <div className="markdown-body body-graph">
          <div className="header-graph"> Graph Visuals</div>
          <hr />
          <div className="center-grid">
            <Row>
              <Col>
                <div className="font-home">Term Frequency Graph</div>
              </Col>
              <Col>
                <div className="font-home">Term Similarity Graph</div>
              </Col>
            </Row>
            <Row>
              <div>
                <Col>
                  <Button
                    type="button"
                    className="button"
                    onClick={this.handleGraph}
                  >
                    Open Graph
                  </Button>
                </Col>
                <Col>
                  <form>
                    <label>
                      Keyword:
                      <input type="text" name="keyword" className="input" />
                    </label>
                    <input type="submit" value="Submit" />
                  </form>
                  {keyword !== null ? (
                    <Button
                      type="button"
                      className="button"
                      onClick={this.handleKeyword}
                    >
                      Open Graph
                    </Button>
                  ) : null}
                </Col>
              </div>
              {loading ? <LoadingSpinner /> : null}
            </Row>
          </div>
        </div>
      </div>
    );
  }
}

export default Graph;
