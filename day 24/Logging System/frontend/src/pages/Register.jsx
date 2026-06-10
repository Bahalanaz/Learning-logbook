import { useState } from 'react'
import api from '../api/axios'

function Register() {
    const [formData, setFormData] = useState({
        email: '',
        password: '',
        password2: ''
    })
    const [message, setMessage] = useState('')
    const [error, setError] = useState('')

    function handleChange(e) {
        setFormData({ ...formData, [e.target.name]: e.target.value })
    }

    async function handleSubmit(e) {
        e.preventDefault()
        setMessage('')
        setError('')

        try {
            await api.post('/auth/register/', formData)
            setMessage('Account created successfully. You can now log in.')
        } catch (err) {
            setError(err.response?.data?.email?.[0] || 'Registration failed. Please try again.')
        }
    }

    return (
        <div className="auth-container">
            <h2>Create Account</h2>
            <p className="auth-subtitle">Sign up to get started</p>

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

                <div className="form-group">
                    <label>Confirm Password</label>
                    <input
                        type="password"
                        name="password2"
                        value={formData.password2}
                        onChange={handleChange}
                        placeholder="••••••••"
                    />
                </div>

                <button type="submit" className="btn-primary">Register</button>
            </form>

            {message && <p className="msg-success">{message}</p>}
            {error && <p className="msg-error">{error}</p>}

            <div className="auth-footer">
                Already have an account? <a href="/login">Log in</a>
            </div>
        </div>
    )
}

export default Register
