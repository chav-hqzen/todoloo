<template>
  <div>
    <form @submit="addTodo">
      <input type="text" placeholder="Enter ToDoLoo..." v-model="title" />
      <input type="submit" value="ADD" class="add" />
    </form>
  </div>
</template>

<script>
export default {
  name: 'AddTodo',
  data() {
    return {
      title: '',
    };
  },
  methods: {
    addTodo(e) {
      e.preventDefault();
      if (this.title !== '') {
        const newTodo = {
          title: this.title,
          completed: false,
        };

        this.$emit('add-todo', newTodo);

        this.title = '';
      } else {
        return;
      }
    },
  },
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

input[type='submit'] {
  flex: 2;
  font-weight: bold;
  border-radius: 8px;
}
</style>
