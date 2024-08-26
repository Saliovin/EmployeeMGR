<script setup lang="ts">
import Icon from './Icon.vue';

interface Props {
    title?: string;
}

const props = defineProps<Props>();
const emit = defineEmits(["close"]);
</script>

<template>
    <Teleport to="body">
        <div class="modal" @click="emit('close')">
            <div class="modal-main" @click.stop>
                <div class="modal-top">
                    <h2 v-if="props.title">{{ props.title }}</h2>
                    <Icon icon="x" size="lg" @click="emit('close')" clickable class="close" />
                </div>
                <slot />
            </div>
        </div>
    </Teleport>
</template>

<style scoped>
.modal {
    position: fixed;
    display: flex;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(49, 55, 60, 0.6);
    place-items: center;
}

.modal-main {
    margin: auto;
    min-width: 25rem;
    max-width: 50%;
    background-color: #fff;
    padding: 1rem;
}

.modal-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 1rem;
}

.close {
    transition-duration: 0.1s;
}

.close:hover {
    cursor: pointer;
    transform: scale(1.7);
}
</style>
