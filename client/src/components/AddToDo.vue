<template>
  <div>
    <form>
      <input type="text" placeholder="Enter ToDoLoo..." />
      <input type="button" value="ADD" class="add" />
    </form>
  </div>
</template>

<script>
export default {
  name: 'AddTodo',
};
</script>

<style scoped>
form {
  display: flex;
  gap: 24px;
  margin: 5% 10%;
}

input[type='text'] {
  flex: 10;
  padding: 14px;
  border-radius: 8px;
}

input[type='button'] {
  flex: 2;
  font-weight: bold;
  border-radius: 8px;
}
</style>
