<template>
  <div class="calendar-wrap">
    <v-calendar
    is-expanded
    :min-date='minDate'
    :attributes="attributes"
    />
  </div>
</template>

<script>
export default {
  name: 'UserCalendar',

  props: {
    reviewArray: Array,
  },
  
  data() {
    return {
      minDate: new Date(2020, 8, 1),
      attributes: [
        {
          key: 'today',
          highlight: true,
          popover: { label: '맥주와 함께하기 좋은 오늘입니다!' },
          dates: new Date(),
        }
      ]
    }
  },

  mounted() {
    function toAttributesFormat(review) {
      return {
        dates: review.created_date,
        dot: { color: 'red' },
        popover: { label: review.beer_name }
      }
    }
    
    this.attributes = [
      ...this.attributes,
      ...this.reviewArray.map(review => toAttributesFormat(review))
    ]
  }
}
</script>

<style lang="scss" scoped>
.calendar-wrap {
  width: 100vw;
  max-width: 650px;
}
</style>