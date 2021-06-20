<template>
  <div class="">
    <Quote />
    <AnimeList />
  </div>
</template>

<script>

import Quote from "@/components/Quote"
import AnimeList from "@/components/AnimeList"

export default {
  name: 'Home',
  components: {
    Quote,
    AnimeList
  }
}
</script>
