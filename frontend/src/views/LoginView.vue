<script setup lang="ts">
import type { User } from "@/interfaces/user";
import router from "@/router";
import service from "@/services/auth";
import { ref } from "vue";

const error_message = ref("")

const loginUser = (user: User) => {
  service
    .login(user)
    .then((res) => {
      router.push("/");
    })
    .catch((error) => {
      console.log(error)
      error_message.value = "Login Unsuccessful"
    });
};

const onSubmitLogin = (e: Event) => {
  error_message.value = ""
  const formData = new FormData(e.target as HTMLFormElement);
  const user = Object.fromEntries(formData);
  // @ts-ignore
  loginUser(user);
};
</script>

<template>
  <div class="login">
    <div class="panel">
      <h2>App Title</h2>
      <div class="error" v-if="error_message">{{ error_message }}</div>
      <form @submit.prevent="onSubmitLogin">
        <div class="input-group">
          <label>Username</label>
          <input name="username" />
        </div>
        <div class="input-group">
          <label>Password</label>
          <input name="password" type="password" />
        </div>
        <button type="submit">Login</button>
      </form>
    </div>
  </div>
</template>

<style scoped>
.login {
  display: flex;
  flex-direction: column;
  place-items: center;
  margin: 0 auto;
  padding: 2rem;
  max-width: 60%;
  height: 100%;
  background-color: #fff;
}

.panel {
  min-width: 15rem;
}

.input-group {
  display: flex;
  flex-direction: column;
}

h2 {
  text-decoration: underline;
  text-align: center;
  margin-bottom: 1rem;
}

button {
  width: 100%;
  margin-top: 0.5rem;
  background-color: #89b0de;
}

button:hover {
  background-color: #6678ba;
}
</style>
