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
// import axios from 'axios';
import sileo from 'sileo';

sileo.defaults.baseUrl = 'http://127.0.0.1:8000';

const Todo = new sileo.Model('todos', 'todo');

export default {
  name: 'App',
  components: { TitleHeader, ToDos, AddToDo },
  data() {
    return {
      todos: [],
    };
  },
  methods: {
    deleteTodo(delTodo) {
      Todo.objects
        .delete({ pk: delTodo.pk })
        .then(
          () =>
            (this.todos = this.todos.filter(
              (todo) => todo.title !== delTodo.title
            ))
        )
        .catch((err) => console.log(err));
    },
    addTodo(newTodo) {
      const form = new FormData();
      form.append('title', newTodo.title);
      form.append('completed', newTodo.completed);

      Todo.objects
        .create(form)
        .then((data) => {
          this.todos = [...this.todos, data];
        })
        .catch((err) => console.log(err));
    },
    completeTodo(todo) {
      const todoItem = this.todos.find((item) => item.pk === todo.pk);

      if (todoItem) {
        const newCompletedStatus = !todoItem.completed;

        const form = new FormData();
        form.append('title', todoItem.title);
        form.append('completed', newCompletedStatus);

        Todo.objects
          .update({ pk: todoItem.pk }, form)
          .then((todoItem.completed = newCompletedStatus))
          .catch((err) => console.log(err));
      }
    },
  },
  mounted() {
    Todo.objects
      .filter()
      .then((data) => (this.todos = data))
      .catch((err) => console.log(err));
  },
};
</script>

<style></style>
