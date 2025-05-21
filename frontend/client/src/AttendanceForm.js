import React, { useState, useEffect } from 'react';

function AttendanceForm() {
  const [students, setStudents] = useState([]);
  const [formData, setFormData] = useState({
    student: '',
    date: '',
    status: 'Present',
  });

  useEffect(() => {
    fetch('http://localhost:8000/api/students/')
      .then(response => response.json())
      .then(data => setStudents(data))
      .catch(error => console.error('Error:', error));
  }, []);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('http://localhost:8000/api/attendance/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData),
    })
      .then(response => response.json())
      .then(data => alert('Attendance saved!'))
      .catch(error => console.error('Error:', error));
  };

  return (
    <div className="p-4 bg-white rounded shadow">
      <h3 className="text-lg mb-2">Mark Attendance</h3>
      <form onSubmit={handleSubmit}>
        <div className="mb-4">
          <label className="block text-sm">Student</label>
          <select
            name="student"
            value={formData.student}
            onChange={handleChange}
            className="w-full p-2 border rounded"
            required
          >
            <option value="">Select Student</option>
            {students.map(student => (
              <option key={student.id} value={student.id}>
                {student.name} ({student.roll_no})
              </option>
            ))}
          </select>
        </div>
        <div className="mb-4">
          <label className="block text-sm">Date</label>
          <input
            type="date"
            name="date"
            value={formData.date}
            onChange={handleChange}
            className="w-full p-2 border rounded"
            required
          />
        </div>
        <div className="mb-4">
          <label className="block text-sm">Status</label>
          <select
            name="status"
            value={formData.status}
            onChange={handleChange}
            className="w-full p-2 border rounded"
          >
            <option value="Present">Present</option>
            <option value="Absent">Absent</option>
          </select>
        </div>
        <button
          type="submit"
          className="bg-blue-600 text-white p-2 rounded hover:bg-blue-700"
        >
          Submit
        </button>
      </form>
    </div>
  );
}

export default AttendanceForm;