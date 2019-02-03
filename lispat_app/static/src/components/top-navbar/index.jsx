import React, { Component } from 'react';
import { Navbar, Nav } from 'react-bootstrap';
import style from './navbar.css';
import image from '../../../images/github-icon.png';

class TopNav extends Component {
  render() {
    return (
      <div>
        <Navbar bg="dark" expand="lg" className={style['background-color']}>
          <Navbar.Brand href="#home" className={style.logo}>
            <span className={style.font}>LISPAT</span>
          </Navbar.Brand>
          <Navbar.Toggle
            aria-controls="basic-navbar-nav"
            className={style['icon-bar']}
          />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="ml-auto">
              <Nav.Link href="#home">
                <span className={style['font-right']}>API</span>
              </Nav.Link>
              <Nav.Link href="#link">
                <span className={style['font-right']}>HELP</span>
              </Nav.Link>
              <Nav.Link href="#link">
                <span className={style['font-right']}>
                  <img
                    src={image}
                    alt="github"
                    className="img-responsive image-github"
                  />
                </span>
              </Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Navbar>
      </div>
    );
  }
}

export default TopNav;
