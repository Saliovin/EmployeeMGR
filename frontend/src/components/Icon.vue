<script setup lang="ts">
import BootstrapIcons from "bootstrap-icons/bootstrap-icons.svg";
import type { PropType } from "vue";

enum IconSizes {
    "sm",
    "md",
    "lg"
}

defineProps({
    icon: {
        type: String,
        required: true,
    },
    size: {
        type: String as PropType<keyof typeof IconSizes>,
        default: IconSizes.md,
    },
});
</script>

<template>
    <svg class="icon" :class="size">
        <g transform-origin="center">
            <use v-bind:xlink:href="`${BootstrapIcons}#${icon}`" />
        </g>
    </svg>
</template>

<style scoped>
.icon {
    width: 1em;
    height: 1em;
}

.sm {
    font-size: 0.75rem;
}

.md {
    font-size: 1rem;
}

.lg {
    font-size: 1.5rem;
}
</style>