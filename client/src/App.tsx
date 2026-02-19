import { useState, useEffect } from 'react'
import axios from 'axios'
import './css/App.css' // or index.css where you added Tailwind

function App() {
  const [message, setMessage] = useState('Loading...')

  useEffect(() => {
    // Example call to your Express backend
    axios.get('http://localhost:3000/api/hello')
      .then(response => setMessage(response.data.message))
      .catch(error => {
        console.error('Error:', error)
        setMessage('Failed to connect to server')
      })
  }, [])

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="bg-white p-8 rounded-lg shadow-md text-center">
        <h1 className="text-3xl font-bold text-blue-600 mb-4">
          React + Express + Tailwind
        </h1>
        <p className="text-lg text-gray-700 mb-4">
          {message}
        </p>
        <button 
          className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
          onClick={() => alert('React is working!')}
        >
          Click me
        </button>
      </div>
    </div>
  )
}

export default App