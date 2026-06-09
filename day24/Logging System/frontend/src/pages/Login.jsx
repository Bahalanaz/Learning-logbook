import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import api from '../api/axios'

function Login() {
    const [formData, setFormData] = useState({
        email: '',
        password: ''
    })
    const [error, setError] = useState('')
    const navigate = useNavigate()

    function handleChange(e) {
        setFormData({ ...formData, [e.target.name]: e.target.value })
    }

    async function handleSubmit(e) {
        e.preventDefault()
        setError('')

        try {
            const response = await api.post('/auth/login/', formData)
            localStorage.setItem('access', response.data.access)
            localStorage.setItem('refresh', response.data.refresh)
            navigate('/dashboard')
        } catch (_err) {
            setError('Invalid email or password.')
        }
    }

    return (
        <div className="auth-container">
            <h2>Welcome Back</h2>
            <p className="auth-subtitle">Log in to your account</p>

            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label>Email</label>
                    <input
                        type="email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                        placeholder="you@example.com"
                    />
                </div>

                <div className="form-group">
                    <label>Password</label>
                    <input
                        type="password"
                        name="password"
                        value={formData.password}
                        onChange={handleChange}
                        placeholder="••••••••"
                    />
                </div>

                <button type="submit" className="btn-primary">Login</button>
            </form>

            {error && <p className="msg-error">{error}</p>}

            <div className="auth-footer">
                Don't have an account? <a href="/register">Sign up</a>
            </div>
        </div>
    )
}

export default Login