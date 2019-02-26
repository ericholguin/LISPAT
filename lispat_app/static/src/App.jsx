import React, { Component } from 'react';
import propTypes from 'prop-types';
import { hot } from 'react-hot-loader';
import TopNav from './components/top-navbar/index';
import DataUpload from './components/data-upload/index';
import './components/side-navbar/side-navbar.css';
import SideNavClass from './components/side-navbar/index';
import WelcomePage from './components/welcome-page/index';
import Lispat from './components/lispat';
import Graph from './components/graph';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      showHome: true,
      showData: false,
      showLispat: false,
      showGraph: false,
      showConfig: false,
      data: null,
    };
  }

  switchView = view => {
    if (view === 'Home') {
      this.setState({
        showHome: true,
        showData: false,
        showLispat: false,
        showGraph: false,
      });
    }
    if (view === 'Data') {
      this.setState({
        showHome: false,
        showData: true,
        showLispat: false,
        showGraph: false,
      });
    }
    if (view === 'Lispat') {
      this.setState({
        showHome: false,
        showData: false,
        showLispat: true,
        showGraph: false,
      });
    }
    if (view === 'Graph') {
      this.setState({
        showHome: false,
        showData: false,
        showLispat: false,
        showGraph: true,
      });
    }
  };

  switchToLispat = statusCode => {
    console.log(statusCode);
    if (statusCode === 200) {
      this.setState({
        showLispat: true,
        showData: false,
        showHome: false,
        showConfig: true,
      });
    }
  };

  showGraphNav = () => {
    const { showGraph, data } = this.state;
    return showGraph === true  || data !== null;
  };

  showConfigNav = () => {
    const { showConfig } = this.state;
    return showConfig === true;
  };

  showLispatNav = () => {
    const { showLispat, data } = this.state;
    return showLispat === true || data !== null;
  };

  switchLispat = () => {
    const { showLispat } = this.state;
    if (showLispat === true) {
      return 'Lispat';
    }
    return null;
  };

  render() {
    const { showHome, showData, showLispat, showGraph, data } = this.state;
    return (
      <div>
        <TopNav />
        <div className={showHome ? 'show' : 'hide'}>
          <WelcomePage />
        </div>
        {showData ? (
          <DataUpload
            stateChange={this.switchToLispat}
            getData={d => {
              this.setState({ data: d });
            }}
          />
        ) : null}
        <div className={showLispat ? 'show' : 'hide'}>
          <Lispat data={data} />
        </div>
        <div className={showGraph ? 'show' : 'hide'}>
          <Graph />
        </div>
        <SideNavClass
          handleStateChange={this.switchView}
          graph={this.showGraphNav()}
          config={this.showConfigNav()}
          lispat={this.showLispatNav()}
          onChange={showLispat}
        />
      </div>
    );
  }
}

App.propTypes = {
  data: propTypes.instanceOf(Object),
};

export default hot(module)(App);
