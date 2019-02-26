import React, { Component } from 'react';
import SideNav, { NavItem, NavIcon, NavText } from '@trendmicro/react-sidenav';
import propTypes from 'prop-types';
import '@trendmicro/react-sidenav/dist/react-sidenav.css';
import './side-navbar.css';
import ClickOutside from 'react-click-outside';

class SideNavClass extends Component {
  constructor(props) {
    super(props);
    this.state = {
      expanded: false,
      activeGraph: false,
      activeLispat: false,
      activeData: false,
      activeHome: true,
    };
  }

  componentWillReceiveProps(props) {
    if (props.onChange) {
      this.setState({
        activeGraph: false,
        activeLispat: true,
        activeData: false,
        activeHome: false,
      });
    }
  }

  handleSelect = eventKey => {
    const { handleStateChange } = this.props;
    if (eventKey === 'Data') {
      this.setState({
        activeGraph: false,
        activeLispat: false,
        activeData: true,
        activeHome: false,
      });
    }
    if (eventKey === 'Home') {
      this.setState({
        activeGraph: false,
        activeLispat: false,
        activeData: false,
        activeHome: true,
      });
    }
    if (eventKey === 'Lispat') {
      this.setState({
        activeGraph: false,
        activeLispat: true,
        activeData: false,
        activeHome: false,
      });
    }
    if (eventKey === 'Graph') {
      this.setState({
        activeGraph: true,
        activeLispat: false,
        activeData: false,
        activeHome: false,
      });
    }
    handleStateChange(eventKey);
  };

  render() {
    const { config, lispat, graph } = this.props;
    const { expanded, activeLispat, activeData, activeHome, activeGraph } = this.state;
    return (
      <div>
        <ClickOutside
          onClickOutside={() => {
            this.setState({ expanded: false });
          }}
        >
          <SideNav
            expanded={expanded}
            onToggle={expanded => {
              this.setState({ expanded });
            }}
            onSelect={selected => {
              this.handleSelect(selected);
            }}
            selected="Lispat"
            className="root-nav"
          >
            <SideNav.Toggle />
            <SideNav.Nav>
              <NavItem eventKey="Home" active={activeHome}>
                <NavIcon>
                  <i
                    className="fa fa-fw fa-home"
                    style={{ fontSize: '1.75em' }}
                  />
                </NavIcon>
                <NavText>Home</NavText>
              </NavItem>
              <NavItem eventKey="Data" active={activeData}>
                <NavIcon>
                  <i
                    className="fa fa-fw fa-cubes"
                    style={{ fontSize: '1.75em' }}
                  />
                </NavIcon>
                <NavText>Data</NavText>
              </NavItem>
              {lispat ? (
                <NavItem eventKey="Lispat" active={activeLispat}>
                  <NavIcon>
                    <i
                      className="fa fa-fw fa-book-open"
                      style={{ fontSize: '1.75em' }}
                    />
                  </NavIcon>
                  <NavText>Source</NavText>
                </NavItem>
              ) : null}
              {graph ? (
                <NavItem eventKey="Graph" active={activeGraph}>
                  <NavIcon>
                    <i
                      className="fa fa-fw fa-chart-area"
                      style={{ fontSize: '1.75em' }}
                    />
                  </NavIcon>
                  <NavText>Graph</NavText>
                </NavItem>
              ) : null}
            </SideNav.Nav>
          </SideNav>
        </ClickOutside>
      </div>
    );
  }
}

SideNavClass.propTypes = {
  handleStateChange: propTypes.func,
  config: propTypes.bool,
  lispat: propTypes.bool,
  graph: propTypes.bool,
  activeLispat: propTypes.bool,
  activeData: propTypes.bool,
  activeGraph: propTypes.bool,
  onChange: propTypes.bool,
};

export default SideNavClass;
