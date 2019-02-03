import React, { Component } from 'react';
import { hot } from 'react-hot-loader';
import TopNav from './components/top-navbar';
import HomeUpload from './components/home-upload';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <div>
        <TopNav />
        <HomeUpload />
      </div>
    );
  }
}

export default hot(module)(App);
