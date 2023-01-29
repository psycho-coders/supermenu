<script>
import PostItem from "./PostItem.vue";
export default {
  components: {
    PostItem,
  },
  props: {
    posts: {
      type: Array,
      required: true,
    },
  },
};
</script>

<template>
  <div v-show="posts.length > 0">
    <h3>List</h3>
    <PostItem
      v-for="post in posts"
      :post="post"
      :key="post.id"
      @remove="$emit('remove', post)"
    />
  </div>
  <h2 v-show="posts.length === 0" style="color: red">List is empty</h2>
</template>

<style scoped></style>
