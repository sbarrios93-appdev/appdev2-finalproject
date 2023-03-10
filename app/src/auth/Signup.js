import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import API_URL from "../config";
import { Card, Label, TextInput, Button } from "flowbite-react";

function Signup({ setIsAuth }) {
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
      setIsAuth(true);
      navigate("/home", { replace: true });
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <Card>
      <form onSubmit={handleSubmit}>
        <div>
          <Label htmlFor="email">Email:</Label>
          <TextInput
            type="email"
            id="email"
            value={email}
            onChange={(event) => setEmail(event.target.value)}
          />
        </div>
        <div>
          <Label htmlFor="firstName">First Name:</Label>
          <TextInput
            type="text"
            id="firstName"
            value={firstName}
            onChange={(event) => setFirstName(event.target.value)}
          />
        </div>
        <div>
          <Label htmlFor="lastName">Last Name:</Label>
          <TextInput
            type="text"
            id="lastName"
            value={lastName}
            onChange={(event) => setLastName(event.target.value)}
          />
        </div>
        <div>
          <Label htmlFor="dateOfBirth">Date of Birth:</Label>
          <TextInput
            type="date"
            id="dateOfBirth"
            value={dateOfBirth}
            onChange={(event) => setDateOfBirth(event.target.value)}
          />
        </div>
        <div>
          <Label htmlFor="password1">Password:</Label>
          <TextInput
            type="password"
            id="password1"
            value={password1}
            onChange={(event) => setPassword1(event.target.value)}
          />
        </div>
        <div>
          <Label htmlFor="password2">Confirm Password:</Label>
          <TextInput
            type="password"
            id="password2"
            value={password2}
            onChange={(event) => setPassword2(event.target.value)}
          />
        </div>

        <Button type="submit">Signup</Button>
      </form>
    </Card>
  );
}

export default Signup;
