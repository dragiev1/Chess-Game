const RegisterCard = () => {
  return (
    <div className="login-card">
        <div className="login-title">Register</div>
        <div>
          <input
            type="email"
            className="login-input"
            placeholder="Email"
          />
        </div>
        <div>
          <input
            type="first name"
            className="login-input"
            placeholder="First Name"
          />
        </div>
        <div>
          <input
            type="last name"
            className="login-input"
            placeholder="Last Name"
          />
        </div>
        <div className="mt-4">
          <input
            type="password"
            className="login-input"
            placeholder="Enter password"
          />
        </div>
        <div>
          <input
            type="password"
            className="login-input"
            placeholder="Re-enter password"
          />
        </div>

        {/* Google Button */}
        <button className="login-button">
          Register
        </button>
      </div>
  );
};

export default RegisterCard;