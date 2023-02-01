<script>
export default {
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
      if (this.post.body == "" && this.post.title == "") {
        return;
      }
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
    <my-input v-model="post.title" type="text" placeholder="Post" />
    <my-input v-model="post.body" type="text" placeholder="Description" />
    <my-button
      class="btn"
      style="align-self: flex-end; margin-top: 15px"
      @click="createPost"
    >
      Add</my-button
    >
  </form>
</template>

<style scoped>
form {
  display: flex;
  flex-direction: column;
}
</style>
