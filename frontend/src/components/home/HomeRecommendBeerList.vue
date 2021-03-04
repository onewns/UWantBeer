<template>
  <div>
    <div class="beer-list-box">
      <div 
        v-for="(item, index) in recommendArray" :key="index">
        <beer-list-item :item="item" :beerId="item.id"></beer-list-item>
      </div>
    </div>
  </div>
</template>

<script>
// components
import BeerListItem from '@/components/beer/BeerListItem'

export default {
  name: 'BeerList',

  props: {
    recommendArray: Array
  },

  components: {
    'beer-list-item': BeerListItem,
  },
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';

.beer-list-box {
  @extend .flex-center;
  margin: 0 10vw;
  display: grid !important;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 20px;
}

@media screen and (max-width: 768px){
  .beer-list-box {
    margin: 0 10px;
    grid-template-columns: 1fr;
    grid-gap: 10px;
  }
}
</style>