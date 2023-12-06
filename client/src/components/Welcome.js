import React from 'react';
import '../App.css'; 
import InputField from './InputField'
import VerticalLine from './VerticalLine';


const Header = () => (
  <header className="header">
    <div className="logo">Project Mid</div>
    <ul className="navigation">
          {/* THROW IN NAVIGATION HERE */}
    </ul>
  </header>
);

function Welcome() {
  return (
    <div className="App">
      <Header />
      <InputField />
      <VerticalLine />
    </div>
  );
}

export default Welcome;
