import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import API_URL from "../config";
import isAuthenticated from "../helpers";

function Signup() {
  const [email, setEmail] = useState("");
  const [password1, setPassword1] = useState("");
  const [password2, setPassword2] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [dateOfBirth, setDateOfBirth] = useState("");

  const navigate = useNavigate();
  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const response = await axios.post(`${API_URL}/accounts/register`, {
        email,
        password: password1,
        password_confirm: password2,
        first_name: firstName,
        last_name: lastName,
        date_of_birth: dateOfBirth,
      });
      localStorage.setItem("access_token", response.data.auth_token);
      if (isAuthenticated()) {
        navigate("/home", { replace: true });
      } else {
        navigate("/welcome", { replace: true });
      }
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          value={email}
          onChange={(event) => setEmail(event.target.value)}
        />
      </div>
      <div>
        <label htmlFor="firstName">First Name:</label>
        <input
          type="text"
          id="firstName"
          value={firstName}
          onChange={(event) => setFirstName(event.target.value)}
        />
      </div>
      <div>
        <label htmlFor="lastName">Last Name:</label>
        <input
          type="text"
          id="lastName"
          value={lastName}
          onChange={(event) => setLastName(event.target.value)}
        />
      </div>
      <div>
        <label htmlFor="dateOfBirth">Date of Birth:</label>
        <input
          type="date"
          id="dateOfBirth"
          value={dateOfBirth}
          onChange={(event) => setDateOfBirth(event.target.value)}
        />
      </div>
      <div>
        <label htmlFor="password1">Password:</label>
        <input
          type="password"
          id="password1"
          value={password1}
          onChange={(event) => setPassword1(event.target.value)}
        />
      </div>
      <div>
        <label htmlFor="password2">Confirm Password:</label>
        <input
          type="password"
          id="password2"
          value={password2}
          onChange={(event) => setPassword2(event.target.value)}
        />
      </div>

      <button type="submit">Signup</button>
    </form>
  );
}

export default Signup;
