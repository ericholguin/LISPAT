import React, { Component } from 'react';
import { hot } from 'react-hot-loader';
import TopNav from './components/top-navbar/index';
import DataUpload from './components/data-upload/index';
import './components/side-navbar/side-navbar.css';
import SideNavClass from './components/side-navbar/index';
import WelcomePage from './components/welcome-page/index';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      showHome: true,
      showData: false,
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

  render() {
    const { showHome, showData } = this.state;
    return (
      <div>
        <TopNav />
        {showHome ? <WelcomePage /> : null}
        {showData ? <DataUpload /> : null}
        <SideNavClass handleStateChange={this.switchView} />
      </div>
    );
  }
}

export default hot(module)(App);
