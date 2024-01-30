<template>
  <div>
    <h2>All ToDoLoos:</h2>
    <ul>
      <li v-for="todo in todos" v-bind:key="todo.id">
        <ToDoItem v-bind:todo="todo" />
      </li>
    </ul>
  </div>
</template>

<script>
import ToDoItem from './ToDoItem.vue';
export default {
  name: 'ToDos',
  props: ['todos'],
  components: { ToDoItem },
  data() {
    return {};
  },
};
</script>

<style scoped>
div {
  margin-top: 36px;
}

h2 {
  text-align: center;
}

ul {
  display: flex;
  flex-direction: column;
  gap: 24px;
  margin-top: 24px;
}
</style>
