<script setup lang="ts">
import Card from "@/components/Card.vue";
import Modal from "@/components/Modal.vue";
import { onMounted, ref, toRaw } from "vue";
import employeeService from "../services/employee";
import authService from "../services/auth";
import RegularEmployeeForm from "@/components/RegularEmployeeForm.vue";
import ContractualEmployeeForm from "@/components/ContractualEmployeeForm.vue";
import { clean_properties } from "@/utils/parse-employee";
import router from "@/router";
import type { Employee } from "@/interfaces/employee";

// Data declarations
const employees = ref<Employee[]>([]);
const isOpenSaveModal = ref(false);
const isOpenViewModal = ref(false);
const isOpenDeleteModal = ref(false);
const currentEmployee = ref({
  id: 0,
  first_name: "",
  last_name: "",
  email: "",
  employee_type: "",
  properties: {},
});
const modalTitle = ref("")

// Function declarations
const logoutUser = () => {
  authService
    .logout()
    .then((res) => {
      router.push("/login");
    })
    .catch((error) => console.log(error));
};
const addEmployee = (employee: Employee) => {
  employee.properties = clean_properties(
    employee.employee_type,
    employee.properties
  );
  employeeService
    .postEmployee(employee)
    .then((res) => {
      fetchEmployees();
      isOpenSaveModal.value = false;
    })
    .catch((error) => console.log(error.message));
};
const fetchEmployees = () => {
  employeeService
    .getEmployees()
    .then((res) => (employees.value = res.data))
    .catch((error) => console.log(error.message));
};
const updateEmployee = (employee: Employee) => {
  employee.properties = clean_properties(
    employee.employee_type,
    employee.properties
  );
  employeeService
    .putEmployee(currentEmployee.value.id, employee)
    .then((res) => {
      fetchEmployees();
      isOpenSaveModal.value = false;
    })
    .catch((error) => console.log(error.message));
};
const deleteEmployee = () => {
  employeeService
    .deleteEmployee(currentEmployee.value.id)
    .then((res) => {
      fetchEmployees();
      isOpenDeleteModal.value = false;
    })
    .catch((error) => console.log(error.message));
};
const saveEmployee = (employee: Employee) => {
  if (modalTitle.value.includes("Edit")) updateEmployee(employee)
  else addEmployee(employee)
}

// onEvent declarations
const onClickAddEmployee = () => {
  modalTitle.value = "Add Employee"
  currentEmployee.value = {
    id: 0,
    first_name: "",
    last_name: "",
    email: "",
    employee_type: "regular",
    properties: {},
  };
  isOpenSaveModal.value = true;
};
const onClickViewEmployee = (employee: Employee) => {
  currentEmployee.value = structuredClone(toRaw(employee));
  isOpenViewModal.value = true;
};
const onClickEditEmployee = (employee: Employee) => {
  modalTitle.value = "Edit Employee"
  currentEmployee.value = structuredClone(toRaw(employee));
  isOpenSaveModal.value = true;
};
const onClickDeleteEmployee = (employee: Employee) => {
  currentEmployee.value = structuredClone(toRaw(employee));
  isOpenDeleteModal.value = true;
};

onMounted(fetchEmployees);
</script>

<template>
  <main>
    <div class="main-button-set">
      <button class="add" @click="onClickAddEmployee">Add</button>
      <button class="logout" @click="logoutUser">Logout</button>
    </div>

    <div class="employee-deck">
      <Card v-for="employee in employees" :first_name="employee.first_name" :last_name="employee.last_name"
        @view="onClickViewEmployee(employee)" @edit="onClickEditEmployee(employee)"
        @delete="onClickDeleteEmployee(employee)" />
    </div>
    <Modal v-if="isOpenSaveModal" @close="isOpenSaveModal = false" :title="modalTitle">
      <!-- Add new Employee Type Forms here -->
      <ContractualEmployeeForm v-if="currentEmployee.employee_type == 'contractual'" :employee="currentEmployee"
        @submit="saveEmployee(currentEmployee)" />
      <RegularEmployeeForm v-else :employee="currentEmployee" @submit="saveEmployee(currentEmployee)" />
    </Modal>
    <Modal v-if="isOpenViewModal" @close="isOpenViewModal = false" title="View Employee">
      <p>First Name: {{ currentEmployee.first_name }}</p>
      <p>Last Name: {{ currentEmployee.last_name }}</p>
      <p>Email: {{ currentEmployee.email }}</p>
      <p>Employee Type: {{ currentEmployee.employee_type }}</p>
      <p v-for="(value, key) in currentEmployee.properties">
        {{ key }}: {{ value }}
      </p>
    </Modal>
    <Modal v-if="isOpenDeleteModal" @close="isOpenDeleteModal = false" title="Delete Employee">
      <div>
        <p>
          Delete employee {{ currentEmployee.first_name }}
          {{ currentEmployee.last_name }}
        </p>
        <button class="delete" @click="deleteEmployee()">Delete</button>
      </div>
    </Modal>
  </main>
</template>

<style>
main {
  display: flex;
  flex-direction: column;
  padding: 2rem;
  max-width: 60%;
  height: 100%;
  margin: 0 auto;
  background-color: #fff;
}

.main-button-set {
  align-self: flex-end;
}

.add,
.logout {
  margin: 0 0.3rem;
}

.employee-deck {
  display: flex;
  flex-wrap: wrap;
  margin-top: 1rem;
}

.employee-deck .card {
  margin: 0.5rem 1rem;
}

.input-group,
p {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.5rem;
}

form button,
.add {
  color: #fafafa;
  background-color: #6aa84f;
}

form button:hover,
.add:hover {
  background-color: #41964a;
  cursor: pointer;
}

.delete {
  background-color: #df6565;
}

.delete:hover {
  background-color: #c5544a;
}
</style>
