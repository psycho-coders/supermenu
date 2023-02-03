<script>
import PostForm from "./components/PostForm.vue";
import PostList from "./components/PostList.vue";
import MyButton from "./components/UI/MyButton.vue";
import axios from "axios";

export default {
  components: {
    PostForm,
    PostList,
    MyButton,
  },
  data() {
    return {
      posts: [],
      dialogVisible: false,
    };
  },
  methods: {
    createPost(post) {
      this.posts.push(post);
      this.dialogVisible = false;
    },
    removePost(post) {
      this.posts = this.posts.filter((p) => p.creator !== post.creator);
    },
    showDialog() {
      this.dialogVisible = true;
    },
    addFile(img) {
      this.posts.push(img);
    },
    async sendPost() {
      const res = await axios.post(
        "http://localhost:5000/v1/create",
        {
          data: this.$data.posts,
        }
      );
      console.log(res);
    },
  },
};
</script>

<template>
  <div class="app">
    <h1>Menu</h1>
    <my-button @click="showDialog" style="margin: 15px 0"
      >Create menu</my-button
    >
    <my-dialog v-model:show="dialogVisible">
      <PostForm @create="createPost" />
    </my-dialog>
    <PostList :posts="posts" @remove="removePost" @file="addFile" />
    <my-button style="margin-top: 15px" @click="sendPost">Send</my-button>
  </div>
</template>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.app {
  padding: 20px;
}
</style>
