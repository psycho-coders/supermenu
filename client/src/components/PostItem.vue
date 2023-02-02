<script>
export default {
  props: {
    post: {
      type: Object,
      required: true,
    },
  },
};
</script>

<template>
  <div class="post">
    <div>
      <div class="post__img">
        <strong>Изображение: </strong> <img :src="post.img" alt="" />
        <div><strong>Название:</strong> {{ post.title }}</div>
        <div><strong>Описание:</strong> {{ post.body }}</div>
      </div>
    </div>
    <div class="post__btns">
      <my-button @click="$emit('remove', post)">Delete</my-button>
    </div>
  </div>
</template>

<style scoped>
.post {
  padding: 15px;
  border: 2px solid teal;
  margin-top: 15px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

img {
  width: 100px;
  height: 100px;
}
.post__img {
  display: flex;
  flex-direction: column;
}
</style>
