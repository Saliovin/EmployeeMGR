import router from "@/router";
import axios from "axios";

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_BASE_API_URL,
  headers: {
    "Content-type": "application/json",
  },
  withCredentials: true,
});

apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (
      JSON.stringify(error.response.data.detail).toLowerCase().includes("token")
    ) {
      router.push("/login");
    }
    return Promise.reject(error);
  }
);

export default apiClient;
