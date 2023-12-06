import './App.css';
import Welcome from './components/Welcome';
import Loading from './components/Loading';
import { Routes, Route } from 'react-router-dom'

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path='/' element={<Welcome />} />
        <Route path='/loading' element={<Loading />} />
      </Routes>
    </div>
  );
}

export default App;
