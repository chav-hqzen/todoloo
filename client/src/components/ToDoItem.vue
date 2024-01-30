<template>
  <div class="todo-item" v-bind:class="{ 'is-completed': todo.completed }">
    <div>
      <input type="checkbox" />
      <span>{{ todo.title }}</span>
    </div>
    <button class="del">×</button>
  </div>
</template>

<script>
export default {
  name: 'TodoItem',
  props: ['todo'],
  data() {
    return {};
  },
};
</script>

<style scoped>
.todo-item {
  margin: 0 12px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: #ebebeb;
  padding: 18px;
  border-radius: 12px;
}

.todo-item div {
  display: flex;
  justify-content: center;
}

input {
  width: 16px;
  height: 20px;
}

span {
  margin-left: 24px;
}

.del {
  padding: 7px 10px;
  font-size: 16px;
  font-weight: bold;
  color: white;
  background-color: red;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  float: right;
}

.is-completed {
  text-decoration: line-through;
}
</style>
