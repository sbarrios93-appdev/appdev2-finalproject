import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import API_URL from "../config";
import { Card, Label, TextInput, Button } from "flowbite-react";
function Login({ setIsAuth }) {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const response = await axios.post(`${API_URL}/accounts/login`, {
        email,
        password,
      });
      localStorage.setItem("access_token", response.data.access);
      setIsAuth(true);
      navigate("/home", { replace: true });
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-12 px-4 sm:px-2 lg:px-8">
      <div className="max-w-md w-full space-y-8">
        <div>
          <h2 className="mt-6 text-center text-3xl font-extrabold text-sky-200">
            Log in
          </h2>
        </div>
      </div>
      <div className="max-w-lg mt-8">
        <Card>
          <form className="flex flex-col gap-4" onSubmit={handleSubmit}>
            <div className="mb-2 block">
              <Label htmlFor="email">Email:</Label>
              <TextInput
                type="email"
                id="email"
                value={email}
                onChange={(event) => setEmail(event.target.value)}
                required={true}
              />
            </div>
            <div>
              <Label htmlFor="password">Password:</Label>
              <TextInput
                type="password"
                id="password"
                value={password}
                required={true}
                onChange={(event) => setPassword(event.target.value)}
              />
            </div>
            <Button type="submit">Login</Button>
          </form>
        </Card>
      </div>
    </div>
  );
}

export default Login;
