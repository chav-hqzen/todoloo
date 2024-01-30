<template>
  <div id="app">
    <TitleHeader></TitleHeader>
    <AddToDo v-on:add-todo="addTodo"></AddToDo>
    <ToDos
      v-bind:todos="todos"
      @complete-todo="completeTodo"
      @del-todo="deleteTodo"
    ></ToDos>
  </div>
</template>

<script>
import TitleHeader from './components/TitleHeader.vue';
import AddToDo from './components/AddToDo.vue';
import ToDos from './components/ToDos.vue';

export default {
  name: 'App',
  components: { TitleHeader, ToDos, AddToDo },
  data() {
    return {
      todos: [
        {
          id: 1,
          title: 'eat',
          completed: false,
        },
        {
          id: 2,
          title: 'code',
          completed: false,
        },
        {
          id: 3,
          title: 'sleep',
          completed: false,
        },
      ],
    };
  },
  methods: {
    deleteTodo(id) {
      this.todos = this.todos.filter((todo) => todo.id !== id);
    },
    addTodo(todo) {
      this.todos = [...this.todos, todo];
    },
    completeTodo(todo) {
      const todoItem = this.todos.find((item) => item.id === todo.id);
      if (todoItem) {
        todoItem.completed = !todoItem.completed;
      }
    },
  },
};
</script>

<style></style>
