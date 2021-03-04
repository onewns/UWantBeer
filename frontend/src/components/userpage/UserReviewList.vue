<template>
<div v-if="reviewArray">
  <beer-review-item
    v-for="(review, index) in reviewArray" :key="index"
    :review="review"
    >
  </beer-review-item>
</div>
</template>

<script>
import BeerReviewItem from '@/components/beer/BeerReviewItem'

export default {
  name: 'UserReviewList',

  components: {
    BeerReviewItem,
  },

  props: {
    reviewArray: Array
  },


}
</script>

<style>

</style>