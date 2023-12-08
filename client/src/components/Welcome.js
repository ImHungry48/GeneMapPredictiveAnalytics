import React from 'react';
import '../App.css'; 
import InputField from './InputField'
import VerticalLine from './VerticalLine';
import About from './About';




function Welcome() {
  return (
    <div className="App">
      <InputField />
      <VerticalLine />
      <About />
    </div>
  );
}

export default Welcome;
