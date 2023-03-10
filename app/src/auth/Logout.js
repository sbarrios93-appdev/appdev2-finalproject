import React from "react";
import { useNavigate } from "react-router-dom";
import isAuthenticated from "../helpers";
function Logout() {
  const navigate = useNavigate();
  const handleLogout = async () => {
    localStorage.removeItem("access_token");
    if (isAuthenticated()) {
      navigate("/home", { replace: true });
    } else {
      navigate("/welcome", { replace: true });
    }
  };

  return <button onClick={handleLogout}>Logout</button>;
}

export default Logout;
