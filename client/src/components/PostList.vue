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
  <div>
    <div v-if="posts.length > 0">
      <h3>List</h3>
      <PostItem
        v-for="post in posts"
        :post="post"
        :key="post.creator"
        @remove="$emit('remove', post)"
      />
    </div>
    <h2 v-else style="color: red">List is empty</h2>
  </div>
</template>

<style scoped></style>
