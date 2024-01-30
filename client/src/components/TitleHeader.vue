<template>
  <div class="title-header">
    <h1>{{ title }}</h1>
    <p>{{ subtitle }}</p>
    <p class="subtext">{{ subtext }}</p>
  </div>
</template>

<script>
export default {
  name: 'TitleHeader',
  data() {
    return {
      title: '>>> ToDoLoo <<<',
      subtitle: '____ a todo list app _____',
      subtext: 'Here, your todos are todoloos',
    };
  },
};
</script>

<style scoped>
.title-header {
  margin: 0 auto;
  padding: 36px;
  text-align: center;
  background-color: lightgreen;
}

.subtext {
  font-style: italic;
  font-size: 85%;
}
</style>
