<script>
import PostForm from "./components/PostForm.vue";
import PostList from "./components/PostList.vue";
import MyButton from "./components/UI/MyButton.vue";

export default {
  components: {
    PostForm,
    PostList,
    MyButton,
  },
  data() {
    return {
      posts: [
        {
          id: 1,
          title: "1",
          body: "Description",
        },
        {
          id: 2,
          title: "2",
          body: "Description 2",
        },
        {
          id: 3,
          title: "3",
          body: "Description 3",
        },
        {
          id: 4,
          title: "4",
          body: "Description 4",
        },
      ],
      dialogVisible: false,
    };
  },
  methods: {
    createPost(post) {
      this.posts.push(post);
      this.dialogVisible = false;
    },
    removePost(post) {
      this.posts = this.posts.filter((p) => p.id !== post.id);
    },
    showDialog() {
      this.dialogVisible = true;
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
    <PostList :posts="posts" @remove="removePost" />
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
