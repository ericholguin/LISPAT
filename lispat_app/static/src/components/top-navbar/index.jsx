import React, { Component } from 'react';
import propTypes from 'prop-types';
import { Navbar, Nav } from 'react-bootstrap';
// import axios from 'axios/index';
import style from './navbar.css';

// const endpoint = 'http://localhost:5000/assets/samples.zip';

class TopNav extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeHome: false,
      activeHelp: false,
      activeApi: false,
    };
  }

  /* handleDownload = () => {
    axios({
      url: endpoint,
      method: 'GET',
      responseType: 'blob', // important
    }).then(response => {
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', 'samples.zip');
      document.body.appendChild(link);
      link.click();
    });
  }; */

  handleSelect = eventKey => {
    const { handleStateChange } = this.props;
    if (eventKey === 'Home') {
      this.setState({
        activeHome: true,
        activeHelp: false,
        activeApi: false,
      });
    }
    if (eventKey === 'Help') {
      this.setState({
        activeHome: false,
        activeHelp: true,
        activeApi: false,
      });
    }
    if (eventKey === 'Api') {
      this.setState({
        activeHome: false,
        activeHelp: false,
        activeApi: true,
      });
    }
    handleStateChange(eventKey);
  };

  render() {
    const { activeHelp, activeApi } = this.state;
    return (
      <div>
        <Navbar
          bg="dark"
          expand="lg"
          className={style['background-color']}
          onSelect={selected => {
            this.handleSelect(selected);
          }}
        >
          <Navbar.Brand className={style.logo}>
            <span className={style.font}>LISPAT</span>
          </Navbar.Brand>
          <Navbar.Toggle
            aria-controls="basic-navbar-nav"
            className="navbar-light hamburger"
          />
          <Navbar.Collapse id="basic-navbar-nav pull-right">
            <Nav className="ml-auto">
              <Nav.Link eventKey="Api" active={false} href="#api">
                <span className={style['font-right']}>API</span>
              </Nav.Link>
              <Nav.Link eventKey="Help" active={false} href="#help">
                <span className={style['font-right']}>Help</span>
              </Nav.Link>
              <Nav.Link
                href="https://github.com/brummetj/LISPAT"
                target="_blank"
                active={false}
              >
                <span title="GitHub Link" className={style['font-right']}>
                  <i className="fab fa-github" />
                </span>
              </Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Navbar>
      </div>
    );
  }
}

TopNav.propTypes = {
  handleStateChange: propTypes.func,
  activeHome: propTypes.bool,
  activeHelp: propTypes.bool,
  activeApi: propTypes.bool,
};

export default TopNav;
