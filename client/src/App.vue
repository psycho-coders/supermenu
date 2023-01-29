<script>
import PostForm from "./components/PostForm.vue";
import PostList from "./components/PostList.vue";

export default {
  components: {
    PostForm,
    PostList,
  },
  data() {
    return {
      posts: [
        {
          id: 1,
          title: "JS",
          body: "Description",
        },
        {
          id: 2,
          title: "JS elem",
          body: "Description 2",
        },
        {
          id: 3,
          title: "JS pro",
          body: "Description 3",
        },
        {
          id: 4,
          title: "JS proff",
          body: "Description 4",
        },
      ],
    };
  },
  methods: {
    createPost(post) {
      this.posts.push(post);
    },
    removePost(post) {
      this.posts = this.posts.filter((p) => p.id !== post.id);
    },
  },
};
</script>

<template>
  <div class="app">
    <PostForm @create="createPost" />
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
