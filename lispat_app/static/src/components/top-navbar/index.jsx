import React, { Component } from 'react';
import propTypes from 'prop-types';
import { Navbar, Nav } from 'react-bootstrap';
import style from './navbar.css';
import axios from 'axios/index';


class TopNav extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeHelp: false,
      activeApi: false,
    };
  }


  handleSelect = eventKey => {
    const { handleStateChange } = this.props;
    if (eventKey === 'Help') {
      this.setState({
        activeHelp: true,
        activeApi: false,
      });
    }
    if (eventKey === 'Api') {
      this.setState({
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
          <Navbar.Brand href="#home" className={style.logo}>
            <span className={style.font}>LISPAT</span>
          </Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
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
                <span className={style['font-right']}>
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
  activeHelp: propTypes.bool,
  activeApi: propTypes.bool,
};

export default TopNav;
