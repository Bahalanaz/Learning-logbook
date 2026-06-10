import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import api from '../api/axios'

function Dashboard() {
    const [user, setUser] = useState(null)
    const [error, setError] = useState('')
    const navigate = useNavigate()

    useEffect(() => {
        const token = localStorage.getItem('access')

        if (!token) {
            navigate('/login')
            return
        }

        api.get('/auth/me/', {
            headers: {
                Authorization: `Bearer ${token}`
            }
        })
        .then(response => setUser(response.data))
        .catch(() => {
            setError('Session expired. Please log in again.')
            navigate('/login')
        })
    }, [navigate])

    function handleLogout() {
        const refresh = localStorage.getItem('refresh')
        const token = localStorage.getItem('access')

        api.post('/auth/logout/', { refresh }, {
            headers: { Authorization: `Bearer ${token}` }
        })
        .finally(() => {
            localStorage.removeItem('access')
            localStorage.removeItem('refresh')
            navigate('/login')
        })
    }

    return (
        <div className="dashboard-container">
            <h2>Dashboard</h2>
            {user ? (
                <>
                    <p>You are logged in as</p>
                    <span className="user-badge">{user.email}</span>
                    <br />
                    <button className="btn-danger" onClick={handleLogout}>Logout</button>
                </>
            ) : (
                <p>Loading...</p>
            )}
            {error && <p className="msg-error">{error}</p>}
        </div>
    )
}

export default Dashboard