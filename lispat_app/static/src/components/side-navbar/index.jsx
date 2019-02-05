import React, { Component } from 'react';
import SideNav, { NavItem, NavIcon, NavText } from '@trendmicro/react-sidenav';
import propTypes from 'prop-types';
import './side-navbar.css';
import '@trendmicro/react-sidenav/dist/react-sidenav.css';
import Config from '../config';

class SideNavClass extends Component {
  handleSelect = eventKey => {
    const { handleStateChange } = this.props;
    handleStateChange(eventKey);
  };

  render() {
    const { config, lispat } = this.props;
    return (
      <div>
        <SideNav
          onSelect={selected => {
            this.handleSelect(selected);
          }}
          className="root-nav">
          <SideNav.Toggle />
          <SideNav.Nav defaultSelected="home">
            <NavItem eventKey="Home">
              <NavIcon>
                <i
                  className="fa fa-fw fa-home"
                  style={{ fontSize: '1.75em' }}/>
              </NavIcon>
              <NavText>Home</NavText>
            </NavItem>
            <NavItem eventKey="Data">
              <NavIcon>
                <i
                  className="fa fa-fw fa-cubes"
                  style={{ fontSize: '1.75em' }}/>
              </NavIcon>
              <NavText>Data</NavText>
            </NavItem>
            {config ? (
              <NavItem eventKey="Config">
                <NavIcon>
                  <i
                    className="fa fa-fw fa-cogs"
                    style={{ fontSize: '1.75em' }}/>
                </NavIcon>
                <NavText>Config</NavText>
              </NavItem>
            ) : null}
            {lispat ? (
              <NavItem eventKey="Lispat">
                <NavIcon>
                  <i
                    className="fa fa-fw fa-book-open"
                    style={{ fontSize: '1.75em' }}/>
                </NavIcon>
                <NavText>Source</NavText>
              </NavItem>
            ) : null}
          </SideNav.Nav>
        </SideNav>
      </div>
    );
  }
}

SideNavClass.propTypes = {
  handleStateChange: propTypes.func,
  config: propTypes.bool,
  lispat: propTypes.bool,
};

export default SideNavClass;
