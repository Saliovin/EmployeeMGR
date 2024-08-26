import type { Employee } from "@/interfaces/employee";
import apiClient from "./base";

const postEmployee = (employee: Employee) => {
  const response = apiClient.post("/employees", employee);
  return response;
};
const getEmployees = () => {
  const response = apiClient.get("/employees");
  return response;
};
const putEmployee = (id: number, employee: Employee) => {
  const response = apiClient.put("/employees/" + id, employee);
  return response;
};
const deleteEmployee = (id: number) => {
  const response = apiClient.delete("/employees/" + id);
  return response;
};

const Service = {
  postEmployee,
  getEmployees,
  putEmployee,
  deleteEmployee,
};

export default Service;
