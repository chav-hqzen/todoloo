<template>
  <div>
    <h2>All ToDoLoos:</h2>
    <ul>
      <li v-for="todo in todos" :key="todo.pk">
        <ToDoItem
          v-bind:todo="todo"
          @complete-todo="$emit('complete-todo', todo)"
          @del-todo="$emit('del-todo', todo)"
        />
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
  width: 100%;
  margin-top: 36px;
  padding: 16px;
}

h2 {
  text-align: center;
}

ul {
  display: flex;
  flex-direction: column;
  margin: 0 auto;
  gap: 24px;
  margin-top: 24px;
  max-width: 640px;
  width: 100%;
  list-style: none;
}
</style>
