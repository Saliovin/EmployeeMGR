<script setup lang="ts">
import type { Employee } from "@/interfaces/employee";

interface Props {
    employee: Employee;
}

const props = defineProps<Props>();
const emit = defineEmits(["submit"]);
</script>

<template>
    <form @submit.prevent="(e: Event) => emit('submit', e)">
        <div class="input-group">
            <label>First Name</label>
            <input type="text" name="first_name" v-model="props.employee.first_name" />
        </div>
        <div class="input-group">
            <label>Last Name</label>
            <input type="text" name="last_name" v-model="props.employee.last_name" />
        </div>
        <div class="input-group">
            <label>Email</label>
            <input type="email" name="email" v-model="props.employee.email" />
        </div>
        <div class="input-group">
            <label>Employee Type</label>
            <select v-model="props.employee.employee_type">
                <option selected>regular</option>
                <option>contractual</option>
            </select>
        </div>
        <div class="input-group">
            <label>Number of Leaves</label>
            <input type="number" name="number_of_leaves" v-model="props.employee.properties.number_of_leaves" />
        </div>
        <div class="input-group">
            <label>Benefits</label>
            <input type="text" name="benefits" v-model="props.employee.properties.benefits" />
        </div>
        <button type="submit">Submit</button>
    </form>
</template>
