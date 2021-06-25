<template>
  <div class="">
    <Quote />
    <Lister :tipe="tipe" />
  </div>
</template>

<script>
import Quote from "@/components/Quote";
import Lister from "../components/Listing.vue";
export default {
  name: "Home",
  components: {
    Quote,
    Lister,
  },
  data() {
    return {
      tipe: "Anime",
    };
  },
};
</script>
