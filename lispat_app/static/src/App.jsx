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
    if (statusCode === 200) {
      this.setState({
        showLispat: true,
        showData: false,
        showHome: false,
      });
    }
  };

  render() {
    const { showHome, showData, showLispat } = this.state;
    return (
      <div>
        <TopNav />
        {showHome ? <WelcomePage /> : null}
        {showData ? <DataUpload stateChange={this.switchToLispat} /> : null}
        {showLispat ? <Lispat /> : null}
        <SideNavClass handleStateChange={this.switchView} />
      </div>
    );
  }
}

export default hot(module)(App);
