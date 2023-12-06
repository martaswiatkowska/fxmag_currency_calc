import { Label, Input} from "reactstrap";
import { useState, useEffect, component, MouseEvent } from "react";
import axios from "axios";
import CurrencyData from "./currency-data";
import React from "react";
import { Form, FormGroup } from "react-bootstrap";

const url = "http://127.0.0.1:8000/api/calculator/"
const submit_url = "http://127.0.0.1:8000/api/calculated_value/"

class Calculator extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      in_currency: 'PLN',
      out_currency: 'EUR',
      value_from: 1,
      result: 0,
      currency_data: { effective_date: "", mid: ""}
    };
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleOnChange = this.handleOnChange.bind(this);
  }

  handleOnChange(event) {
    this.setState({[event.target.name]: event.target.value}); 
  }
  
  handleSubmit = (event: MouseEvent) => {
    event.preventDefault();
    let data = { 
      params: { 
        in_currency: this.state.in_currency,
        out_currency: this.state.out_currency,
        value_from: this.state.value_from,
      }
    }
    
    axios.get(submit_url, data)
    .then(res => {
      this.setState({result: res.data.result})
    })

  }

  handleCurrencyData = (event: MouseEvent) => {
    const data = { params: { currency: event.target.value }}
    this.setState({[event.target.name]: event.target.value}); 
    
    axios.get(url, data)
    .then(res => {
      this.setState({ currency_data:  res.data});
    })
  }


  render() {
    return (
        <Form onSubmit={this.handleSubmit} className="form-inline">
          <FormGroup className="in-currency">
            <Label>
              Wejściowa waluta
            </Label>
            <select  name="in_currency" value={this.state.in_currency} onChange={this.handleOnChange}>
              <option value="USD">USD</option>
              <option value="EUR">EUR</option>
              <option value="PLN">PLN</option>
            </select>
          </FormGroup>
          <FormGroup className="value-from">
          <input type="text" name="value_from" className="value_from" value={this.state.value_from} onChange={this.handleOnChange}/>
        </FormGroup>  
        <FormGroup className="out-currency">
          <div className="out-currency-select">
            <Label>
              Wyjściowa waluta
            </Label>
            <select name="out_currency" value={this.state.out_currency} onChange={this.handleCurrencyData}>
              <option key="PLN" value="PLN">PLN</option>
              <option key="USD" value="USD">USD</option>
              <option key="EUR" value="EUR">EUR</option>
            </select>
          </div>    
          <CurrencyData data={this.state.currency_data}/>
          </FormGroup >
          <div className="result">
            <input type='submit' value="Przelicz"/>
            <Label>
              W przeliczeniu:
              <span>{this.state.result}</span>
            </Label>
          </div>
        </Form>
    );
  }
}


export default Calculator;
