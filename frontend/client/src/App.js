// import logo from './logo.svg';
// import './App.css';

import React, { useState, useEffect } from 'react';
import AttendanceForm from './AttendanceForm';

function App() {
  const [students, setStudents] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/students/')
      .then(response => response.json())
      .then(data => setStudents(data))
      .catch(error => console.error('Error:', error));
  }, []);

  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-blue-600 text-white p-4">
        <h1 className="text-2xl">School ERP</h1>
      </header>
      <main className="p-4 max-w-4xl mx-auto">
        <h2 className="text-xl mb-4">Student Dashboard</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <h3 className="text-lg mb-2">Mark Attendance</h3>
            <AttendanceForm />
          </div>
          <div>
            <h3 className="text-lg mb-2">Student List</h3>
            <ul className="space-y-2">
              {students.map(student => (
                <li key={student.id} className="p-2 bg-white rounded shadow">
                  {student.name} ({student.roll_no}) - Grade: {student.grade}
                </li>
              ))}
            </ul>
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;