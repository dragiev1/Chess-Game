import "../css/Login.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faChessKnight } from "@fortawesome/free-solid-svg-icons";
import { faChessRook } from "@fortawesome/free-solid-svg-icons";
const Login = () => {
  return (
    <div className="login-bg">
      <FontAwesomeIcon icon={faChessRook} className="rook-icon" />
      <FontAwesomeIcon icon={faChessKnight} className="knight-icon" />
      <div className="login-card">
        <div className="login-title">Login</div>
        <div>
          <input
            type="email"
            className="login-input"
            placeholder="Enter email"
          />
        </div>

        <div className="mt-4">
          <input
            type="password"
            className="login-input"
            placeholder="Enter password"
          />
        </div>

        <button className="login-button">Sign In</button>

        {/* Divider */}
        <div className="divider">
          <span>OR</span>
        </div>

        {/* Google Button */}
        <button className="google-button">
          <img
            src="https://www.svgrepo.com/show/475656/google-color.svg"
            alt="Google"
            className="google-icon"
          />
          Sign in with Google
        </button>
      </div>
    </div>
  );
};

export default Login;
