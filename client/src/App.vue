<template>
  <div id="app">
    <TitleHeader></TitleHeader>
    <AddToDo></AddToDo>
    <ToDos v-bind:todos="todos"></ToDos>
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
};
</script>

<style></style>
