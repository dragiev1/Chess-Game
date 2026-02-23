import "../css/Login.css";
import LoginCard from "../components/LoginCard";
import KnightRookAnimation from "../components/KnightRookAnimation";

const Login = () => {
  return (
    <div className="login-bg">
      <KnightRookAnimation />
      <LoginCard />
    </div>
  );
};

export default Login;
