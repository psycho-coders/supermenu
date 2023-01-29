<script>
import MyButton from "./UI/MyButton.vue";
export default {
  components: {
    MyButton,
  },
  data() {
    return {
      post: {
        title: "",
        body: "",
      },
    };
  },
  methods: {
    createPost() {
      this.post.id = Date.now();
      this.$emit("create", this.post);
      this.post = {
        title: "",
        body: "",
      };
    },
  },
};
</script>

<template>
  <form @submit.prevent>
    <h4>Creation</h4>
    <input
      v-model="post.title"
      class="input"
      type="text"
      placeholder="Postter"
    />
    <input
      v-model="post.body"
      class="input"
      type="text"
      placeholder="Description"
    />
    <MyButton
      class="btn"
      style="align-self: flex-end; margin-top: 15px"
      @click="createPost"
    >
      Add</MyButton
    >
  </form>
</template>

<style scoped>
form {
  display: flex;
  flex-direction: column;
}

.input {
  margin-top: 15px;
  width: 100%;
  border: 1px solid teal;
  padding: 10px 15px;
}
</style>
