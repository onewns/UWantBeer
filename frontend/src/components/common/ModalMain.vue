<template>
  <div v-if="showModal">
    <!-- overlay -->
      <div
        @click="hideModal"
        class="modal-overlay">
      </div>

    <!-- modal -->
    <div
      class="modal-container">
        <!-- close button -->
        <i @click="hideModal" class="far fa-times-circle modal-close-btn"></i>

      <!-- body -->
      <div class="modal-body">
        <beer-list-item-detail></beer-list-item-detail>
      </div>
    </div>    
      
  </div>
</template>

<script>
import BeerListItemDetail from '@/components/beer/BeerListItemDetail'

export default {
  name: 'ModalMain',

  components: {
    'beer-list-item-detail': BeerListItemDetail,
  },

  computed: {
    showModal() {
      return this.$store.state.common.showModalMain
    },
  },

  methods: {
    hideModal() {
      this.$store.commit('common/toggleShowModal')
    },
  },
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/base';
$modal-width: 50vw;
$modal-height: 600px;

.modal {
  &-overlay {
    @include fixed-background;
    background-color: black;
    opacity: 0.8;
    z-index: 6;
  }

  &-container {
    position: fixed;
    top: 15vh;
    left: (100vw - $modal-width)/2;
    margin: auto;

    width: $modal-width;
    height: $modal-height;
    background-color: white;

    overflow: auto;
    z-index: 6; 

    animation: blend-in 400ms;

    &::-webkit-scrollbar {
      display: none;
    }
  }

  &-close-btn {
    position: absolute;
    top: 10px;
    right: 10px;
    transition: 200ms;
  
      &:hover {
        transform: rotateZ(180deg);
        color: crimson;
      }
  }

  &-body {
    padding: 0 3vw 15px;
  }
}

@media screen and (max-width: 768px) {
  .modal-container {
    top: 0;
    left: 0;
    width: 100vw;
    min-width: 100vw;
    height: 100vh;
  }
}

</style>