import React, { Component } from 'react';
import { hot } from 'react-hot-loader';
import TopNav from './components/top-navbar/index';
import DataUpload from './components/data-upload/index';
import './components/side-navbar/side-navbar.css';
import SideNavClass from './components/side-navbar/index';
import WelcomePage from './components/welcome-page/index';
import Lispat from './components/lispat';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      showHome: true,
      showData: false,
      showLispat: false,
      showConfig: false,
    };
  }

  switchView = view => {
    if (view === 'Home') {
      this.setState({
        showHome: true,
        showData: false,
      });
    }
    if (view === 'Data') {
      this.setState({
        showHome: false,
        showData: true,
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

  showConfigNav = () => {
    const { showConfig } = this.state;
    return showConfig === true;
  };

  showLispatNav = () => {
    const { showLispat } = this.state;
    return showLispat === true;
  };

  render() {
    const { showHome, showData, showLispat } = this.state;
    return (
      <div>
        <TopNav />
        {showHome ? <WelcomePage /> : null}
        {showData ? <DataUpload stateChange={this.switchToLispat} /> : 'hide'}
        {showLispat ? <Lispat /> : 'hide'}
        <SideNavClass
          handleStateChange={this.switchView}
          config={this.showConfigNav()}
          lispat={this.showLispatNav()}
        />
      </div>
    );
  }
}

export default hot(module)(App);
