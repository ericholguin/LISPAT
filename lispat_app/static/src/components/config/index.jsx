import React, { Component } from 'react';
import { Form } from 'react-bootstrap';
import './config.css';

class Config extends Component {
  constructor(props) {
    super(props);
    this.state = {
      keywords: false,
      phrases: false,
    };
  }

  // changeKeyword = () => {
  //   const { keywords } = this.state;
  //   const { keyword } = this.props;
  //   this.setState({
  //     keywords: !keywords,
  //   });
  //   keyword(keywords);
  // };

  render() {
    const { keywords, phrases } = this.state;
    return (
      <div className="font-config">
        <select>
          <option>Nearest Neighbor</option>
        </select>
<<<<<<< HEAD
        // <Form>
        //   <Form.Check
        //     className="font-color"
        //     type="radio"
        //     id="default-radio"
        //     label="Keywords"
        //     onChange={this.setState({
        //       keywords: !keywords,
        //     })}
        //   />
        //   <Form.Check
        //     className="font-color"
        //     type="radio"
        //     id="default-radio"
        //     label="Phrases"
        //     onChange={this.setState({
        //       phrases: !phrases,
        //     })}
        //   />
        // </Form>
=======
        {/*<Form>*/}
          {/*<Form.Check*/}
            {/*className="font-color"*/}
            {/*type="radio"*/}
            {/*id="default-radio"*/}
            {/*label="Keywords"*/}
            {/*onChange={this.setState({*/}
              {/*keywords: !keywords,*/}
            {/*})}*/}
          {/*/>*/}
          {/*<Form.Check*/}
            {/*className="font-color"*/}
            {/*type="radio"*/}
            {/*id="default-radio"*/}
            {/*label="Phrases"*/}
            {/*onChange={this.setState({*/}
              {/*phrases: !phrases,*/}
            {/*})}*/}
          {/*/>*/}
        {/*</Form>*/}
>>>>>>> 8a237f928ccca2352802cdc51adbb5534d3fd6ee
      </div>
    );
  }
}

export default Config;
