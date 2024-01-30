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
import axios from 'axios';

export default {
  name: 'App',
  components: { TitleHeader, ToDos, AddToDo },
  data() {
    return {
      todos: [],
    };
  },
  methods: {
    deleteTodo(id) {
      axios
        .delete(`http://127.0.0.1:8000/api/todos/${id}`)
        .then(() => (this.todos = this.todos.filter((todo) => todo.id !== id)))
        .catch((err) => console.log(err));
    },
    addTodo(newTodo) {
      const { title, completed } = newTodo;
      axios
        .post('http://127.0.0.1:8000/api/todos/', { title, completed })
        .then((res) => (this.todos = [...this.todos, res.data]))
        .catch((err) => console.log(err));
    },
    completeTodo(todo) {
      const todoItem = this.todos.find((item) => item.id === todo.id);
      if (todoItem) {
        const newCompletedStatus = !todoItem.completed;

        axios
          .patch(`http://127.0.0.1:8000/api/todos/${todo.id}/`, {
            completed: newCompletedStatus,
          })
          .then((todoItem.completed = newCompletedStatus))
          .catch((err) => console.log(err));
      }
    },
  },
  mounted() {
    axios
      .get('http://127.0.0.1:8000/api/todos/')
      .then((res) => (this.todos = res.data))
      .catch((err) => console.log(err));
  },
};
</script>

<style></style>
