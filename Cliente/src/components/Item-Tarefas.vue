<template>
  <li>
        <span>
            {{ title }}
            <button class="btn btn-danger" @click="$emit('remove')">Remover</button>
        </span>
    </li>
</template>

<script>
export default {
    name: "item-tarefas",
    props: ['title'],
    emit: ['remove']
}
</script>
