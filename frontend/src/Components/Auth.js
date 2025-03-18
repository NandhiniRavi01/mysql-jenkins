import React, { useState } from "react";
import axios from "axios";

function Auth() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [isLogin, setIsLogin] = useState(true);
  const [message, setMessage] = useState("");

  const handleAuth = async () => {
    try {
      const endpoint = isLogin ? "http://localhost:5000/login" : "http://localhost:5000/signup";
      const response = await axios.post(endpoint, { username, password });
      setMessage(response.data.message);
    } catch (error) {
      setMessage("Error: " + error.response.data.message);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100">
      <div className="bg-white p-6 rounded-lg shadow-md w-80">
        <h2 className="text-2xl font-bold mb-4">{isLogin ? "Login" : "Signup"}</h2>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          className="w-full p-2 border rounded mb-2"
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="w-full p-2 border rounded mb-2"
        />
        <button
          onClick={handleAuth}
          className="w-full bg-blue-500 text-white py-2 rounded"
        >
          {isLogin ? "Login" : "Signup"}
        </button>
        <p className="mt-2 text-sm">
          {isLogin ? "Don't have an account? " : "Already have an account? "}
          <button className="text-blue-500" onClick={() => setIsLogin(!isLogin)}>
            {isLogin ? "Signup" : "Login"}
          </button>
        </p>
        {message && <p className="text-red-500 mt-2">{message}</p>}
      </div>
    </div>
  );
}

export default Auth;
