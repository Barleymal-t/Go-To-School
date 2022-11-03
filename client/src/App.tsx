import React from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import RegistrationPage from './pages/RegistrationPage';
import { Schedule } from '@syncfusion/ej2-react-schedule';

function App() {
  return (
    <div className="h-[100vh] flex flex-col justify-center items-center">


    <h1 className=''>Hello</h1>
    <p className='text-2xl font-bold'>Welcome to <span className='text-red-500 uppercase'>go to school</span></p>

      <Link className='bg-blue-500 p-2 m-1 rounded-md' to="schedule">Click here to continue</Link>
    </div>

  );
}

export default App;
