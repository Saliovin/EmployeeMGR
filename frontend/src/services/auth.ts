import type { User } from "@/interfaces/user";
import apiClient from "./base";

const login = (user: User) => {
  const response = apiClient.post("/users/login", user);
  return response;
};

const logout = () => {
  const response = apiClient.post("/users/logout");
  return response;
};

const isTokenVerified = async () => {
  let verified = false;
  await apiClient
    .get("/auth")
    .then((resp) => {
      verified = true;
    })
    .catch((error) => {
      console.log(error.message);
      verified = false;
    });

  return verified;
};

const service = {
  login,
  logout,
  isTokenVerified,
};

export default service;
