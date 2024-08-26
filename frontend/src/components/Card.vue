<script setup lang="ts">
interface Props {
    first_name: string;
    last_name: string;
}

const props = defineProps<Props>();
const emit = defineEmits(["view", "edit", "delete"]);
</script>

<template>
    <div class="card">
        <p>{{ `${props.first_name} ${props.last_name}` }}</p>
        <div class="modal-set">
            <button class="view" @click="emit('view')">[View]</button>
            <button class="edit" @click="emit('edit')">[Edit]</button>
            <button class="delete" @click="emit('delete')">[Delete]</button>
        </div>
    </div>
</template>

<style scoped>
button {
    padding: 0;
    margin: 0 0.2rem;
}

.card {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background-color: #eeeeee;
    height: 10rem;
    width: auto;
    max-width: 13rem;
    padding: 0.5rem;
    border: 1px solid #555;
}

.modal-set {
    align-self: center;
    display: flex;
    width: 100%;
    justify-content: space-between;
}

.view {
    background-color: #9fc4e7;
}

.view:hover {
    background-color: #899fd7;
}

.edit {
    background-color: #fefe06;
}

.edit:hover {
    background-color: #d5e401;
}

.delete {
    background-color: #df6565;
}

.delete:hover {
    background-color: #c5544a;
}
</style>
