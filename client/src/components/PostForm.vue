<script>
export default {
  data() {
    return {
      post: {
        title: "",
        body: "",
        img: null,
      },
    };
  },
  methods: {
    createPost() {
      if (
        this.post.body == "" &&
        this.post.title == "" &&
        this.post.img == null
      ) {
        return;
      }
      this.post.id = Date.now();
      this.$emit("create", this.post);
      this.post = {
        title: "",
        body: "",
      };
    },
    onFileChange(e) {
      const file = e.target.files[0];
      this.post.img = URL.createObjectURL(file);
      this.$emit("file", this.post.img);
    },
  },
};
</script>

<template>
  <form @submit.prevent>
    <h4>Creation</h4>
    <my-input v-model.trim="post.title" type="text" placeholder="Post" />
    <my-input v-model.trim="post.body" type="text" placeholder="Description" />
    <label for="files">Choose file</label>
    <input
      id="files"
      type="file"
      @change="onFileChange"
      style="display: none"
    />
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
label {
  border: 1px solid teal;
  padding: 10px 15px;
  width: 50%;
  display: flex;
  margin-top: 15px;
  cursor: pointer;
  color: rgba(0, 0, 0, 0.5);
}
@media (max-width: 370px) {
  form {
    width: 370px;
  }
}
</style>
